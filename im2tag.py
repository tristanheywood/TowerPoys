import base64
import io

import pyperclip
from PIL import Image, ImageGrab


def run():

    im = ImageGrab.grabclipboard()
    if im is None:
        raise SystemExit("Failed to extract image from clipboard. Does the clipboard contain an image?")

    im.thumbnail(
        (1000, 1000), Image.ANTIALIAS
    )  # Resize image to fit in (1000 x 1000 box).
    bio = io.BytesIO()

    # Quality 4 (on a scale of 0-100) - very high compression. Method 6 - slowest algorithm.
    im.convert("RGB").save(bio, format="webp", quality=4, method=6)

    im_b64 = base64.b64encode(bio.getvalue()).decode("utf-8")
    im_tag = f'<img src="data:image/webp;base64,{im_b64}" height="400px">'

    print(f"Successfully created HTML image tag ({len(im_tag)} characters long).")
    pyperclip.copy(im_tag)


def main():

    # TODO: add command line arguments.
    run()


if __name__ == "__main__":
    main()
