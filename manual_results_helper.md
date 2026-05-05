# Manual Results Helper

Use this file to fill the `Actual output` and `Status` columns in `IT23239470.xlsx` after you verify each test manually.

Rule:
- If the real behavior matches the expected output, use the suggested `Pass` text and set `Status` to `Pass`.
- If the real behavior does not match the expected output, use the suggested `Fail` text and set `Status` to `Fail`.

## Document Conversion

`Pos_0001`
- Pass actual output: `The PPTX file was accepted, converted successfully, and a downloadable PDF was generated.`
- Fail actual output: `The PPTX file upload or conversion did not complete successfully, and a valid downloadable PDF was not generated.`

`Neg_0002`
- Pass actual output: `After cancelling the file picker, no file was selected and the conversion action did not become available.`
- Fail actual output: `After cancelling the file picker, the page still showed conversion controls or allowed the conversion flow without a selected file.`

`Neg_0003`
- Pass actual output: `The ZIP archive was rejected or not processed, and no converted PDF output was generated.`
- Fail actual output: `The ZIP archive was accepted unexpectedly or the page attempted to process it without a clear unsupported file response.`

`Neg_0004`
- Pass actual output: `The large PPTX file was either processed within a reasonable time or the system displayed a clear size or processing message without freezing.`
- Fail actual output: `The large PPTX file caused endless loading, freezing, or an unclear failure response during conversion.`

## PDF Editing

`Pos_0005`
- Pass actual output: `The PDF loaded correctly, the annotation appeared on page 2, and the edited PDF was available for download.`
- Fail actual output: `The PDF did not load correctly, the annotation was not applied as expected, or the edited PDF could not be downloaded.`

`Neg_0006`
- Pass actual output: `Before loading a PDF, the editor did not produce any saved or exported file.`
- Fail actual output: `The editor exposed a save or export action that behaved as if a PDF was loaded even though no file had been selected.`

`Neg_0007`
- Pass actual output: `The DOCX file did not load as editable PDF content, and no PDF editing workflow was applied to it.`
- Fail actual output: `The DOCX file was handled incorrectly as if it were a PDF, or the page showed confusing PDF editing behavior for the unsupported file.`

`Neg_0008`
- Pass actual output: `The encrypted PDF content was not exposed for editing unless valid access was provided, and the page handled the locked file safely.`
- Fail actual output: `The encrypted PDF handling was unclear, unsafe, or allowed editing behavior without properly resolving access restrictions.`

## Image Resizing

`Pos_0009`
- Pass actual output: `The WEBP image was resized using the entered height while keeping its aspect ratio, and a downloadable result was produced.`
- Fail actual output: `The WEBP image did not resize correctly, the aspect ratio was not preserved, or no valid downloadable result was produced.`

`Neg_0010`
- Pass actual output: `The tool rejected decimal dimensions or handled them clearly by rounding without producing an unexpected output.`
- Fail actual output: `The tool accepted decimal dimensions in an unclear way and produced confusing or incorrect resize behavior.`

`Neg_0011`
- Pass actual output: `The SVG file was either supported clearly or rejected without showing a broken preview or invalid resized output.`
- Fail actual output: `The SVG file caused a broken preview, unclear behavior, or an invalid output in the resize workflow.`

`Neg_0012`
- Pass actual output: `The extreme resize dimensions were handled safely, and the tool avoided creating a broken or blank output.`
- Fail actual output: `The extreme resize dimensions caused broken preview behavior, blank output, or another unsafe result.`

## Cropping

`Pos_0013`
- Pass actual output: `The selected vertical crop area appeared correctly in the preview, and the cropped file was available for download.`
- Fail actual output: `The crop selection did not behave correctly in the preview or the cropped file was not produced as expected.`

`Neg_0014`
- Pass actual output: `The tool either allowed a valid tiny crop or prevented an invalid crop area with a clear response.`
- Fail actual output: `The tool handled the tiny crop poorly and produced broken output or unclear crop behavior.`

`Neg_0015`
- Pass actual output: `The animated GIF was either rejected clearly or handled without freezing and without producing a confusing crop result.`
- Fail actual output: `The animated GIF caused freezing, broken preview behavior, or an unclear crop result.`

`Neg_0016`
- Pass actual output: `The zero-byte PNG file did not load as a valid image, and the tool avoided showing a broken crop workspace.`
- Fail actual output: `The zero-byte PNG file was treated as if it were a valid image or caused a broken crop interface.`

## Compression

`Pos_0017`
- Pass actual output: `The JPG photo was previewed correctly, the compression controls were available, and a downloadable compressed file was generated.`
- Fail actual output: `The JPG photo did not preview correctly, the compression controls did not work as expected, or no valid compressed file was generated.`

`Neg_0018`
- Pass actual output: `After rapid quality changes, the page remained responsive and the final output matched the last selected quality setting.`
- Fail actual output: `Rapid quality changes caused the page to become unstable or the final output did not match the last selected setting.`

`Neg_0019`
- Pass actual output: `The TIFF file was handled consistently by either being supported properly or being rejected with a clear response.`
- Fail actual output: `The TIFF file produced inconsistent behavior, unclear messaging, or broken preview or output handling.`

`Neg_0020`
- Pass actual output: `The fake JPG file was not processed as a real image, and the tool did not create a misleading compressed output.`
- Fail actual output: `The fake JPG file was accepted unexpectedly or the tool behaved as if the invalid content were a valid image.`

## Image Format Conversion

`Pos_0021`
- Pass actual output: `The WEBP image uploaded successfully, a preview was displayed, and the conversion workflow allowed the image to be prepared for JPG output.`
- Fail actual output: `The WEBP image did not preview correctly or the conversion workflow for JPG output did not behave as expected.`

`Neg_0022`
- Pass actual output: `After changing the output format multiple times, the final conversion respected the last selected output format.`
- Fail actual output: `The final conversion did not follow the last selected output format and instead used an earlier or incorrect selection.`

`Neg_0023`
- Pass actual output: `The HEIC image was either supported clearly or rejected without broken preview behavior or endless loading.`
- Fail actual output: `The HEIC image caused broken preview behavior, endless loading, or another unclear response in the conversion workflow.`

`Neg_0024`
- Pass actual output: `The large PNG image was either converted successfully or the tool displayed a clear size or processing failure message without freezing.`
- Fail actual output: `The large PNG conversion caused freezing, endless loading, or an unclear failure response.`

## Meme Generation

`Pos_0025`
- Pass actual output: `The meme preview displayed both captions clearly on the uploaded image, and a downloadable meme was generated.`
- Fail actual output: `The meme preview did not render the captions correctly or the generated meme could not be downloaded as expected.`

`Neg_0026`
- Pass actual output: `The caption fields handled the special characters safely and displayed supported characters without breaking the meme generator.`
- Fail actual output: `Entering special characters caused incorrect text rendering or broke the meme generation workflow.`

`Neg_0027`
- Pass actual output: `The unsupported SVG file was rejected clearly or the tool avoided generating a broken meme output.`
- Fail actual output: `The unsupported SVG file caused broken preview behavior or an invalid meme generation result.`

## Color Picker

`Pos_0028`
- Pass actual output: `The selected color was displayed correctly, and the HEX, RGB, and other visible values matched the chosen blue color.`
- Fail actual output: `The selected color values did not match the chosen blue color or the display was inconsistent across the color formats.`

`Neg_0029`
- Pass actual output: `The invalid HEX value was rejected or prevented from replacing the current valid color value.`
- Fail actual output: `The invalid HEX value was accepted incorrectly or caused inconsistent color picker behavior.`

`Neg_0030`
- Pass actual output: `For the selected black color, the visible RGB, HSL, HSV, and CMYK values remained consistent across the available formats.`
- Fail actual output: `The displayed values for the selected black color were inconsistent across the available color formats.`

## Image Rotation

`Pos_0031`
- Pass actual output: `The preview showed the image rotated by 180 degrees, and the downloaded output preserved the same rotation.`
- Fail actual output: `The rotation preview or the downloaded output did not preserve the expected 180-degree rotation.`

`Neg_0032`
- Pass actual output: `The tool handled the out-of-range rotation angle clearly by normalizing, rejecting, or otherwise processing it predictably.`
- Fail actual output: `The out-of-range rotation angle caused unclear behavior, incorrect rotation, or another inconsistent result.`

`Neg_0033`
- Pass actual output: `The animated GIF was either supported clearly or rejected without producing a misleading static or broken rotation result.`
- Fail actual output: `The animated GIF caused broken rotation behavior, misleading output, or an unclear preview or download result.`

## Image Flipping

`Pos_0034`
- Pass actual output: `The preview and downloaded result showed the image flipped vertically as selected.`
- Fail actual output: `The preview or downloaded file did not match the selected vertical flip operation.`

`Neg_0035`
- Pass actual output: `After switching between flip options several times, the final preview and downloaded file matched the last selected flip option.`
- Fail actual output: `After switching between flip options, the final preview or downloaded file did not match the last selected operation.`

`Neg_0036`
- Pass actual output: `The file with invalid PDF content was rejected, and the tool did not generate a broken flipped output.`
- Fail actual output: `The file with invalid PDF content was handled incorrectly as an image or caused broken preview or output behavior.`
