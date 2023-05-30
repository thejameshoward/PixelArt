from pathlib import Path
from PIL import Image
import string
import numpy as np

def GenMonomerRepresentation(
    base_representation: list[int]) -> list:
    '''
    Takes a list of ints which represent a number in some base.
    Generates a list of ASCII characters which represent the base_representation
    '''
    # Map each letter to a number
    conversion_dict = {str(i): letter for i, letter in enumerate(string.ascii_uppercase)}

    # for each of the numbers in the higher base representation, 
    # convert those numbers into the base 26, convert with dict, 
    # join as string
    monomer_representation = []
    for n in base_representation:
        conversion_to_26 = numberToBase(n, 26)
        monomer_representation.append(''.join([conversion_dict[str(x)] for x in conversion_to_26]))
    return monomer_representation

def numberToBase(n, b) -> list[int]:
    '''
    Encodes a number into a different base
    '''
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def EncodeNumber(
    number: int, 
    base: int = 16, 
    verbose = False
    ):
    base_representation = numberToBase(number, base)
    
    monomer_represenation = GenMonomerRepresentation(base_representation)

    if verbose:
        print(f'{number} represented in base-{base} looks like: {" ".join(str(z) for z in base_representation)}')
    if verbose:
        print(f'When represented as monomer codes, it looks like {" ".join(x for x in monomer_represenation)}')
    
    return ' '.join(str(x) for x in monomer_represenation)

def ImgToMonomer(
    img: Image.Image, 
    n_monomers: int = 4, 
    print_data: bool = True, 
    divide_by_16 = True,
    ):
    '''
    Array work
    '''
    #TODO Figure out the divide by 16 issue (remove argument)

    img = img.convert('RGB')
    pixels = np.array(img)
    encoding = pixels.copy().astype(dtype=object)
    encoding = encoding[:, :, 0] # Remove 3rd dimension so we can put strings in there
    for i, col in enumerate(pixels):
        for j, row in enumerate(col):
            s = []
            for k, color in enumerate(row):
                if divide_by_16:
                    color = int(color / 16)
                s.append(EncodeNumber(number = int(color), base=n_monomers))
            encoding[i][j] = f'{s[0]}, {s[1]}, {s[2]}'
    return encoding

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def _format(s):
    return str(s).replace(' ', '').rjust(2, ' ')

if __name__ == "__main__":
    """
    import sys

    p = Path(sys.argv[1])
    img = Image.open(p)

    pixels = ImgToMonomer(img, n_monomers=int(sys.argv[2]), print_data=False)

    with open('out.txt', 'w') as o:
        for item in pixels:
            o.write(str(item))
            o.write(' ')
            o.write('\n')
    """
    EncodeNumber(0, 16, verbose=True)