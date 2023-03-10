from cmath import pi
from pathlib import Path
from PIL import Image
import numpy as np
from collections import Counter

def ReduceBitsPerColorChannel(
    img: Image, 
    bits_per_channel: int) -> Image:
    '''
    Shifts the binary representation of the RGB color channels (which
    are normally 8-bits) to the right and then converts them back to
    8-bit. This effectively reduces the color pallette but it may
    not be true reduction of color depth.
    '''
    conversion = 8 - bits_per_channel

    pixels = np.array(img)
    pixels = (np.right_shift(pixels, conversion) / (2 ** bits_per_channel)) * 256

    return Image.fromarray((pixels).astype(np.uint8))
