from cmath import pi
from pathlib import Path
from PIL import Image
import numpy as np
from collections import Counter

def ReduceBitsPerColorChannel(
    img: Image, 
    bits_per_channel: int) -> Image.Image:
    '''
    Shifts the binary representation of the RGB color channels (which
    are normally 8-bits) to the right and then converts them back to
    8-bit. This effectively reduces the color pallette but it may
    not be true reduction of color depth.
    '''
    conversion = 8 - bits_per_channel

    pixels = np.array(img)
    #pixels = np.right_shift(pixels, conversion) # This gives us values 0 - 15
    pixels = np.right_shift(pixels, conversion)
    pixels = pixels.astype(np.uint8)
    pixels = (pixels / ((2 ** bits_per_channel - 1))) * 255

    return Image.fromarray((pixels).astype(np.uint8))

if __name__ == "__main__":
    import sys
    im = Image.open(str(sys.argv[1]))
    im = ReduceBitsPerColorChannel(im, int(sys.argv[2]))
    p = Path(sys.argv[1])
    im.save(str(Path(p.parent / (p.stem + "-converted.png"))))
