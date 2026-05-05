# PixelsSuite PNG Preview Test

This project contains a simple Python Playwright automation script for **IT3040 ITPM Assignment 1 - Option 2**.

The script tests the PNG preview behavior on:

`https://www.pixelssuite.com/convert-to-png`

## What the script does

1. Opens the target URL.
2. Uploads a PNG image from the project folder.
3. Verifies that the uploaded image appears in the preview area.
4. Saves the execution result to `execution_results.csv`.
5. Saves a screenshot in the `results` folder.

## Files

- `image_preview_test.py` - main Playwright automation script
- `requirements.txt` - Python dependency list
- `sample_image.png` - test image created automatically on first run if it does not exist
- `execution_results.csv` - result log created when the script runs
- `results/preview_pass.png` - screenshot saved when preview is detected

## Setup on Windows

Open the project folder in the VS Code terminal and run:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run the test

Use the assignment command format:

```powershell
python image_preview_test.py --url "https://www.pixelssuite.com/convert-to-png" --slow-mo-ms 2000
```

Optional headless mode:

```powershell
python image_preview_test.py --url "https://www.pixelssuite.com/convert-to-png" --slow-mo-ms 2000 --headless
```

## CSV columns

The script records these useful columns in `execution_results.csv`:

- `timestamp`
- `url`
- `http_status`
- `file_type`
- `file_path`
- `preview_detected`
- `status`
- `screenshot`
- `error_message`

## Notes

- The script uses the default PNG file path `sample_image.png`.
- If `sample_image.png` does not exist, the script creates a small valid PNG automatically in the project folder.
- The target URL currently renders the converter interface even when the HTTP response status is `404`. The script records that status in the CSV but still validates the visible browser preview.
