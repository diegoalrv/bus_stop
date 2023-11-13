#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

import os

def resize_image(input_path, output_path):
    try:
        # Abrir la imagen de entrada
        image = Image.open(input_path)
        # Obtener el tamaño original de la imagen
        original_width, original_height = image.size
        # Calcular el nuevo alto (mitad del ancho)
        new_height = original_width // 2
        # Redimensionar la imagen
        resized_image = image.resize((original_width, new_height))
        # Guardar la imagen redimensionada en la carpeta img_processed
        resized_image.save(output_path)
        print("Imagen redimensionada y guardada correctamente.")
        return resized_image
    except Exception as e:
        print("Error:", e)

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]
    image = resize_image(image_file, image_file.replace(".jpeg","_r.jpeg"))


# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 40
options.cols = 80
options.chain_length = 3
options.parallel = 3
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.multiplexing = 1
options.brightness = 30

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
