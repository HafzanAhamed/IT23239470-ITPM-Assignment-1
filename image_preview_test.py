import argparse
import csv
import struct
import sys
import zlib
from datetime import datetime
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


DEFAULT_URL = "https://www.pixelssuite.com/convert-to-png"
PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_IMAGE_PATH = PROJECT_DIR / "sample_image.png"
RESULTS_DIR = PROJECT_DIR / "results"
CSV_PATH = PROJECT_DIR / "execution_results.csv"

CSV_HEADERS = [
    "timestamp",
    "url",
    "http_status",
    "file_type",
    "file_path",
    "preview_detected",
    "status",
    "screenshot",
    "error_message",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Playwright test for PixelsSuite PNG preview validation."
    )
    parser.add_argument("--url", default=DEFAULT_URL, help="Target URL to test.")
    parser.add_argument(
        "--file-path",
        default=str(DEFAULT_IMAGE_PATH),
        help="PNG file path to upload. Defaults to sample_image.png in this project.",
    )
    parser.add_argument(
        "--slow-mo-ms",
        type=int,
        default=0,
        help="Delay between Playwright actions in milliseconds.",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run the browser in headless mode.",
    )
    return parser.parse_args()


def create_sample_png(file_path: Path, width: int = 80, height: int = 80) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Simple solid-color PNG created with only the Python standard library.
    row = b"\x00" + (b"\x1E\x90\xFF" * width)
    raw_data = row * height

    def chunk(chunk_type: bytes, data: bytes) -> bytes:
        return (
            struct.pack("!I", len(data))
            + chunk_type
            + data
            + struct.pack("!I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
        )

    png_bytes = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack("!IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw_data))
        + chunk(b"IEND", b"")
    )
    file_path.write_bytes(png_bytes)


def ensure_png_file(file_path: Path) -> Path:
    if not file_path.exists():
        create_sample_png(file_path)

    if file_path.suffix.lower() != ".png":
        raise ValueError(f"Only PNG files are allowed for this test: {file_path}")

    return file_path.resolve()


def preview_is_visible(page) -> bool:
    return page.evaluate(
        """
        () => {
            const isVisible = (element) =>
                !!(element && (element.offsetWidth || element.offsetHeight || element.getClientRects().length));

            const hasVisibleCanvas = Array.from(document.querySelectorAll('canvas'))
                .some((canvas) => isVisible(canvas) && canvas.width > 0 && canvas.height > 0);

            const hasVisibleImage = Array.from(document.querySelectorAll('img'))
                .some((image) => isVisible(image) && image.naturalWidth > 0 && image.naturalHeight > 0);

            return hasVisibleCanvas || hasVisibleImage;
        }
        """
    )


def wait_for_preview(page, timeout_ms: int = 30000) -> bool:
    page.wait_for_function(
        """
        () => {
            const isVisible = (element) =>
                !!(element && (element.offsetWidth || element.offsetHeight || element.getClientRects().length));

            const canvasReady = Array.from(document.querySelectorAll('canvas'))
                .some((canvas) => isVisible(canvas) && canvas.width > 0 && canvas.height > 0);

            const imageReady = Array.from(document.querySelectorAll('img'))
                .some((image) => isVisible(image) && image.naturalWidth > 0 && image.naturalHeight > 0);

            return canvasReady || imageReady;
        }
        """,
        timeout=timeout_ms,
    )
    return True


def append_result(row: dict) -> None:
    write_header = not CSV_PATH.exists()
    with CSV_PATH.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_HEADERS)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def run_test(args: argparse.Namespace) -> int:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    upload_file = ensure_png_file(Path(args.file_path))
    pass_screenshot = RESULTS_DIR / "preview_pass.png"
    fail_screenshot = RESULTS_DIR / "preview_fail.png"

    result = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "url": args.url,
        "http_status": "",
        "file_type": upload_file.suffix.lower().lstrip("."),
        "file_path": str(upload_file),
        "preview_detected": False,
        "status": "FAIL",
        "screenshot": "",
        "error_message": "",
    }

    browser = None

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=args.headless,
                slow_mo=args.slow_mo_ms,
            )
            context = browser.new_context()
            page = context.new_page()
            page.set_default_timeout(30000)

            response = page.goto(args.url, wait_until="load", timeout=90000)
            result["http_status"] = response.status if response else ""

            if response and response.status >= 400:
                print(
                    f"Warning: the page returned HTTP {response.status}, "
                    "but the browser still rendered the tool UI."
                )

            file_input = page.locator("input[type='file']").first
            file_input.wait_for(state="attached")
            file_input.set_input_files(str(upload_file))

            wait_for_preview(page)

            result["preview_detected"] = preview_is_visible(page)
            if not result["preview_detected"]:
                raise AssertionError("Preview area was not detected after uploading the PNG file.")

            page.screenshot(path=str(pass_screenshot), full_page=True)
            result["status"] = "PASS"
            result["screenshot"] = str(pass_screenshot)

            print("Preview detected successfully.")
            print(f"Screenshot saved to: {pass_screenshot}")

            context.close()

    except (PlaywrightTimeoutError, AssertionError, ValueError, FileNotFoundError) as exc:
        result["error_message"] = str(exc)
        if browser is not None:
            try:
                page = locals().get("page")
                if page is not None:
                    page.screenshot(path=str(fail_screenshot), full_page=True)
                    result["screenshot"] = str(fail_screenshot)
            except Exception:
                pass
        print(f"Test failed: {exc}")

    except Exception as exc:
        result["error_message"] = f"Unexpected error: {exc}"
        if browser is not None:
            try:
                page = locals().get("page")
                if page is not None:
                    page.screenshot(path=str(fail_screenshot), full_page=True)
                    result["screenshot"] = str(fail_screenshot)
            except Exception:
                pass
        print(f"Unexpected failure: {exc}")

    finally:
        append_result(result)
        if browser is not None:
            try:
                browser.close()
            except Exception:
                pass

    print(f"Execution result saved to: {CSV_PATH}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(run_test(parse_args()))
