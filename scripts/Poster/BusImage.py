import requests
import io
from io import BytesIO
from PIL import ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
from MyDraw import MyDraw

class BusImage(MyDraw):
    def __init__(self):
        pass
    
    def load_image_from_url(self, url=None):
        if(url is None):
            # URL de la imagen en línea
            url = "https://img.freepik.com/iconos-gratis/autobus_318-574563.jpg"

        # Descarga la imagen desde la URL
        response = requests.get(url)
        image_data = response.content
        # Crea un objeto Image desde los datos descargados
        self.image = Image.open(BytesIO(image_data))
        # Crear una imagen en blanco del mismo tamaño que loaded_image con fondo blanco
        background = Image.new("RGB", self.image.size, self.theme_params['background_color'])

        # Pega la loaded_image en la imagen en blanco
        background.paste(self.image, (0, 0), self.image)
        
        self.image = background

        # Calcula la posición para agregar la imagen cargada
        image_position = (0, 0)  # Cambia esto según tu diseño

        # Agrega la imagen a la imagen creada
        self.image.paste(background, image_position)
        pass