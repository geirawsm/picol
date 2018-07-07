#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import colorgram
import argparse
from PIL import Image, ImageDraw, ImageFont
import os


# The font directory is one level higher than this file.
FONT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'fonts'
)


def get_font(fontname, size):
    try:
        font_object = ImageFont.truetype(
            os.path.join(FONT_DIR, fontname),
            size
        )
        return font_object
    except(OSError):
        print('Couldn\'t find font \'{}\''.format(fontname))
        print('Searched {}'.format(FONT_DIR))
        sys.exit()


def rgb_to_hex(value1, value2, value3):
    """
    Convert RGB color to hex color
    """
    for value in (value1, value2, value3):
        if not 0 <= value <= 255:
            raise ValueError('Value each slider must be ranges from 0 to 255')
    return {'hex_color': '#{0:02X}{1:02X}{2:02X}'.format(value1, value2,
            value3), 'link': 'http://www.color-hex.com/color/{0:02X}{1:02X}'
            '{2:02X}'.format(value1, value2, value3)}


def get_center_position_hor(canvas_height, image_in_h):
    """
    Get the correct position for an image to center it horizontally
    """
    if image_in_h < canvas_height:
        _canvas_mid = int(canvas_height / 2)
        _image_in_mid = int(image_in_h / 2)
        return _canvas_mid - _image_in_mid
    else:
        return 0


def get_center_position_ver(canvas_width, canvas_height, image_h_in):
    """
    Get the correct position for an image to center it vertically
    """
    _canvas_mid = int(canvas_height / 2)
    _image_in_mid = int(image_h_in / 2)
    return _canvas_mid - _image_in_mid


def write_out(out, filename):
    """
    Write 'out' to 'filename'
    """
    with open(filename, 'w') as fout:
        fout.write(out)


def main():
    parser = argparse.ArgumentParser()
    parser.prog = 'piccol'
    parser.description = 'Extract the ten most used colors in an image.'
    parser.add_argument('image', action='store')
    parser.add_argument('-s', '--save-image', help='Save image to a given file',
                        action='store_true', dest='save_image')
    parser.add_argument('-d', '--do-not-show', help='Do not show the image that '
                        'is made', action='store_false', dest='do_not_show_image')
    parser.add_argument('-st', '--save-text', help='Save text to a given file',
                        action='store_true', dest='save_text')
    args = parser.parse_args()

    # Get filename of input file
    _file_name = args.image.split('/')
    file_name = _file_name[len(_file_name) - 1]

    # Extract colors from an image.
    colors = colorgram.extract(args.image, 10)

    # Make a smaller version of the received image
    image_in = Image.open(args.image)
    image_in.thumbnail((500, 500))
    image_in_w, image_in_h = image_in.size

    # Set height for canvas. This is dynamic, but has no effect until one can
    # increase/decrease the number of colors to output
    canvas_height = int(len(colors)) * 50
    # ...but if the canvas height is smaller than image_in height, set canvas
    # height to image_in height
    if canvas_height < image_in_h:
        canvas_height = image_in_h

    # Testing shows that 750px wide should be enough
    canvas_width = 750
    img = Image.new('RGB', (canvas_width, canvas_height), 'white')
    # Paste image_in into canvas and find out center position
    center_hor = get_center_position_hor(canvas_height, image_in_h)
    img.paste(image_in, (0, center_hor))
    out = ImageDraw.Draw(img)

    # Get fonts
    title_fnt = get_font('OpenSans-Bold.ttf', 30)
    hex_fnt = get_font('OpenSans-Semibold.ttf', 24)

    # Write header
    title_w, title_h = title_fnt.getsize(file_name)
    center_ver = get_center_position_ver(canvas_width, canvas_height, title_w)
    out.text((center_ver, 7), file_name, font=title_fnt, fill=(0, 0, 0))

    write_output = 'Colors for \'{}\':'.format(file_name)

    hor = 0
    ver = 120

    i = 0
    for color in colors:
        color_out = rgb_to_hex(color.rgb.r, color.rgb.g, color.rgb.b)
        if i == 0:
            pass
        else:
            hor += 50
            ver += 50
        # rectangle(())
        out.rectangle((550, hor, 600, ver), fill=color_out['hex_color'])
        out.text((610, 7 + hor), color_out['hex_color'], font=hex_fnt,
                 fill=(0, 0, 0))
        i += 1
        if args.save_text:
            write_output += '\n{} - {}'.format(color_out['hex_color'],
                                               color_out['link'])
    out_file_name = file_name.split('.')[0]
    out_file_name = 'colors_{}'.format(out_file_name)
    if args.save_text:
        out_file_name += '.txt'
        write_out(write_output, out_file_name)
    if args.save_image:
        out_file_name += '.jpg'
        img.save(out_file_name)
    if args.do_not_show_image is not False:
        img.show()


if __name__ == '__main__':
    main()
