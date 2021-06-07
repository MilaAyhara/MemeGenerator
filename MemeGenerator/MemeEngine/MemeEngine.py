"""An Engine to load an image file, tranform and add text."""

import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
from Exceptions import InvalidFileFormat, InvalidFilePath


class MemeEngine():
    """A class to create Memes."""

    def __init__(self, output_path):
        """Initialize the variable."""
        self.output_path = output_path

    def make_meme(self, img_path, body, author, width=500) -> str:
        """Create an Image With a Text Greeting.

          Arguments:
          img_path {str} -- the file location for the input image.
          text -- the text to be added to the input image.
          author -- the author of the text.
          width {int} -- The pixel width value. Default=500.
          Returns:
          str -- the file path to the output image.
          """
        try:
            img = Image.open(img_path)
        except Exception:
            raise InvalidFilePath("Invalid File Path for the Image")

        if width is not None:
            if width > 500:
                width = 500
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if body is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/Roboto-Bold.ttf',
                                      size=18)
            text = textwrap.fill(f'"{body}" \n- {author}', width=35)
            draw.text((15, 15), text, font=font, fill='white')

        out_path = os.path.join(self.output_path,
                                f'./{random.randint(0,100000)}.jpg')
        img.save(out_path)
        return out_path
