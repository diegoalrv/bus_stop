#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 40
options.cols = 80
options.chain_length = 2
options.parallel = 1
options.gpio_slowdown = 4
#options.row_address_type = 0

options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.multiplexing = 1
options.brightness = 20
#options.pwm_lsb_nanoseconds = 300
#options.pwm_bits = 11


matrix = RGBMatrix(options = options)

# Make image fit our screen.
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'))

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
