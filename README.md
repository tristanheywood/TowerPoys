
# Utilities

## im2tag

Takes the image currently on the clipboard, heavily compresses it, converts it into
an HTML tag, and puts the tag text on the clipboard.

I built this for adding images and especially screenshots to Colab notebooks. Colab lets
you paste images directly into the notebook, and converts them to base64 for you, but
the resulting base64 strings are huge, especially for screenshots on high-DPI displays.

### Usage

Copy an image to the clipboard (or use win+shift+s to take a screenshot).

Run `poetry run python .\im2tag.py`

Paste into your Markdown/HTML document.