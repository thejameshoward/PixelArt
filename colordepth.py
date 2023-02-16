from cmath import pi
from pathlib import Path
from PIL import Image
import numpy as np
from collections import Counter

def ReduceBitsPerColorChannel(
    img: Image, 
    bits_per_channel: int) -> Image:
    '''
    Shifts the binary representation of the RGB color channels which
    are normally 8-bits to the right and then converts them back to
    8-bit. This effectively reduces the color pallette.
    '''
    conversion = 8 - bits_per_channel

    pixels = np.array(img)
    pixels = (np.right_shift(pixels, conversion) / (2 ** bits_per_channel)) * 256

    return Image.fromarray((pixels).astype(np.uint8))

if __name__ == "__main__":
    p = Path('./images/fish.webp')
    img = Image.open(p)
    img.show()

    bits_per_channel = 5
    conversion = 8 - bits_per_channel

    pixels = np.array(img)
    pixels = (np.right_shift(pixels, conversion) / (2 ** bits_per_channel)) * 25788.01 # Change this to a crazy number for cool pictures. Also try left_shift
    #pixels = np.array(Image.fromarray((pixels).astype(np.uint8)))
    #pixels = (np.right_shift(pixels, conversion) / (2 ** bits_per_channel)) * 256776.01 # Change this to a crazy number for cool pictures. Also try left_shift
    #pixels = np.array(Image.fromarray((pixels).astype(np.uint8)))
    #pixels = (np.right_shift(pixels, conversion) / (2 ** bits_per_channel)) * 256776.01 # Change this to a crazy number for cool pictures. Also try left_shift
    #pixels = np.array(Image.fromarray((pixels).astype(np.uint8)))
    #pixels = (np.right_shift(pixels, conversion) / (2 ** bits_per_channel)) * 256776.01 # Change this to a crazy number for cool pictures. Also try left_shift
    #pixels = np.array(Image.fromarray((pixels).astype(np.uint8)))
    #pixels = (np.left_shift(pixels, conversion) / (2 ** bits_per_channel)) * 2567736.01 # Change this to a crazy number for cool pictures. Also try left_shift
    #pixels = (np.left_shift(pixels, conversion) / (2 ** bits_per_channel)) * 256.01
    #pixels = (np.right_shift(pixels, conversion) / (2 ** bits_per_channel)) * 256776.01
    t = Image.fromarray((pixels).astype(np.uint8))
    t.save('images/crazy.png')
    t.show()