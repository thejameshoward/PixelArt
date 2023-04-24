# PixelArt
## A Simple GUI tool for generating pixelated images

<br>

## Installation
1. Clone the repository into a folder<br><br>

        git clone https://github.com/thejameshoward/PixelArt

2. Enter the directory and initalize the GUI

        cd PixelArt
        python3 gui.py

## Using as a bit-depth reducer
Outputs a file in the same directory as the input file except with the correct number of bits.

        python3 colordepth.py all-colors-raw.png 2


![input image](https://github.com/thejameshoward/PixelArt/blob/main/images/all-color-raw.png?raw=true)

![resulting image](https://github.com/thejameshoward/PixelArt/blob/main/images/all-colors-raw-converted.png?raw=true)

## Outputing encoding
To convert an image into RGB representations and encode them as monomors, use the following code.

        python3 encoder.py MorganSmall-converted.png 4

This will create an output file "out.txt" and contain the encoded information in base 4.

