# PixelArt
## A Simple GUI tool for generating pixelated images

<br>

## Installation
1. Clone the repository into a folder<br><br>

        git clone https://github.com/thejameshoward/PixelArt

2. Enter the directory and install requirements

        cd PixelArt
        pip install -r requirements.txt

3. Initialize the gui

        python3 gui.py

## Using as a bit-depth reducer and Encoder
Run the bitmap_gui.py and select your image. You can reduce the number of colors by changing the "color depth" and pressing the enter key. This will round the colors in your image to the nearest color in the lower bitdepth space.

        python3 bitmap_gui.py

16,777,216 colors
![input image](https://github.com/thejameshoward/PixelArt/blob/main/images/all-colors-raw.png?raw=true)

4,096 colors
![resulting image](https://github.com/thejameshoward/PixelArt/blob/main/images/all-colors-raw-converted.png?raw=true)

## Outputing encoding (Not recommended - use GUI)
To convert an image into RGB representations and encode them as monomors, use the following code.

        python3 encoder.py MorganSmall-converted.png 4

This will create an output file "out.txt" and contain the encoded information in base 4.

