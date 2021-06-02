import os
import random

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """ The engine behind meme generation ."""
    def __init__(self, op_dir):
        """ Save and create the output directory path. """
        self.op_dir = op_dir
        self.count = 1
        if not os.path.exists(op_dir):
            os.makedirs(op_dir)

    def make_meme(self, img_path, text, author, width=500):
        """ Create a meme using the given image, text and author """
        img = Image.open(img_path)
        outfile = os.path.join(self.op_dir, f"temp-{self.count}.jpg")
        self.count += 1
        ori_w, ori_h = img.size
        height = int(ori_h * width / ori_w)
        img.thumbnail((width, height))

 # Select font-family, font-size, color and position to draw text
        font1 = ImageFont.truetype("./_data/Fonts/Roboto-Bold.ttf", 22)
        font2 = ImageFont.truetype("./_data/Fonts/Roboto-Medium.ttf", 18)
        text_pos = random.choice(range(30, height - 50))
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)

        # Draw the text on image
        draw = ImageDraw.Draw(img)
        draw.text((30, text_pos), text, fill, font1,
                  stroke_width=1, stroke_fill=stroke_fill)
        draw.text((40, text_pos + 25), f"- {author}", fill, font2,
                  stroke_width=1, stroke_fill=stroke_fill)

        img.save(outfile, "JPEG")
        return outfile
