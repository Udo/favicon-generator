#!python3

import sys
from PIL import Image, ImageDraw, ImageFont

def generate_favicon(letter, bg_color, fg_color, size=64, font_size=48, output='favicon.ico'):
    img = Image.new('RGBA', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Warning: 'arial.ttf' not found. Using default font; appearance may vary.")

    if hasattr(draw, "textbbox"):
        bbox = draw.textbbox((0, 0), letter, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    else:
        text_width, text_height = font.getsize(letter)

    text_x = (size - text_width) / 2
    text_y = (size - text_height) / 2
    draw.text((text_x, text_y-8), letter, font=font, fill=fg_color)
    img.save(output, format='ICO')
    print(f"Favicon saved as {output}")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <letter> <background_color> <foreground_color> [optional: file name]")
        sys.exit(1)
    generate_favicon(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
