# For converting images from a video to 
import cv2
from PIL import Image, ImageChops, ImageFont, ImageDraw, ImageOps
from pathlib import Path
import PIL
import os
from math import ceil
import re

def NaturalSortPaths(paths: list):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    paths.sort(key=lambda x: [ convert(c) for c in re.split('([0-9]+)', x.name) ])
    return paths

def extract(vid: Path):
    vidcap = cv2.VideoCapture(str(vid.absolute()))
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f"./vidframes/{count}.jpg", image)
        success, image = vidcap.read()
        print(count)
        count += 1

def convert(img_path: Path, name: str = None, resize: tuple = None) -> str:
    '''
    Converts an image to an ascii str
    '''
    gradient = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    # Optional arguments
    invert = False
    maxSet = False
    maxSize = 450

    if isinstance(img_path, Path):
        img = Image.open(img_path)
        name = img_path.stem
    elif isinstance(img_path, PIL.PngImagePlugin.PngImageFile):
        if name is None:
            raise Exception('Name cannot be none if using an Image object')
    else:
        raise Exception

    # Resize
    #if(maxSize > 0):
    #    img.thumbnail((maxSize / 2, maxSize / 2))
    if resize is not None:
        img = img.resize(resize)

    # Convert to greyscale and invert if needed
    img = img.convert("L")
    if invert:
        img = ImageChops.invert(img)

    # Generate output
    output = ""
    width, height = img.size
    for y in range(height):
        for x in range(width):
            colour = img.getpixel((x, y))
            output += gradient[round((colour / 255) * (len(gradient) - 1))] + " "
        output += "\n"

    return output

def text_to_image(text: Path, invert = True) -> Image:
    """Convert text to a grayscale image.

    arguments:
    textfile_path - the content of this file will be converted to an image
    font_path - path to a font file (for example impact.ttf)
    """
    lines = txt.split('\n')

    # choose a font (you can see more detail in the linked library on github)
    font = None
    large_font = 25  # get better resolution with larger size

    PIL_GRAYSCALE = 'L'
    PIL_WIDTH_INDEX = 0
    PIL_HEIGHT_INDEX = 1

    font = ImageFont.truetype('Courier', size=large_font)

    # make a sufficiently sized background image based on the combination of font and lines
    font_points_to_pixels = lambda pt: round(pt * 96.0 / 72)
    margin_pixels = 5

    # height of the background image
    tallest_line = max(lines, key=lambda line: font.getsize(line)[PIL_HEIGHT_INDEX])
    max_line_height = font_points_to_pixels(font.getsize(tallest_line)[PIL_HEIGHT_INDEX])
    realistic_line_height = max_line_height * 0.8  # apparently it measures a lot of space above visible content
    image_height = int(ceil(realistic_line_height * len(lines) + 2 * margin_pixels))

    # width of the background image
    widest_line = max(lines, key=lambda s: font.getsize(s)[PIL_WIDTH_INDEX])
    max_line_width = font_points_to_pixels(font.getsize(widest_line)[PIL_WIDTH_INDEX])
    image_width = int(ceil(max_line_width + (2 * margin_pixels)))

    # draw the background
    background_color = 255  # white
    image = Image.new(PIL_GRAYSCALE, (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(image)

    # draw each line of text
    font_color = 0  # black
    horizontal_position = margin_pixels
    for i, line in enumerate(lines):
        vertical_position = int(round(margin_pixels + (i * realistic_line_height)))
        draw.text((horizontal_position, vertical_position), line, fill=font_color, font=font)

    if invert:
        return ImageOps.invert(image)
    return image

def MakeVideo(path: Path):
    os.system("ffmpeg -r 24 -i ./converted_images/%01d.png -vcodec mpeg4 -y movie.mp4")

if __name__ == "__main__":
    #vid = Path('./videos/outofmyleague.mp4')
    #extract(vid)
    i = Path('./images/IMG_4535.png')
    txt = convert(i, name='tmp.png', resize=(102,138))
    i = text_to_image(txt, invert=True)
    i.save('./love.png')

    exit()
    frames = [x for x in Path('./vidframes/').glob('*.jpg')]
    frames = NaturalSortPaths(frames)
    print(frames[:3])

    for i, f in enumerate(frames):
        print(i)
        file = convert(f, resize = (120,76))#(480,270)
        img = textfile_to_image(file, invert=False)
        img.save(f'./converted_images/{i}.png')
#
#
    MakeVideo(Path('./converted_images/'))    

    #image = Image.open('./images/IMG_4535.png')
#
    #txtfile = convert(image, name = 'test')
    #img = textfile_to_image(textfile_path=txtfile)
    #img.save('./converted_images/test.png')