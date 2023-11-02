import requests
import io
from io import BytesIO
from PIL import ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

class MyDraw():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        pass

    def save_image(self, filename):
        self.image.save(filename)
        pass

    def start_draw(self, background_color=None):
        if background_color is None:
            background_color = self.theme_params['background_color']

        self.image = Image.new("RGB", (self.width, self.height), background_color)
        self.draw = ImageDraw.Draw(self.image)
        pass

    def add_image(self, obj, position):
        image_to_add = obj.get_image()  # Obtiene la imagen del objeto pasado como argumento
        if image_to_add:
            self.image.paste(image_to_add, position)
        pass

    def get_draw(self):
        return self.draw
    
    def get_image(self):
        return self.image

    def set_params(self,params):
        self.prms = params
        pass

    def set_theme(self,mode='day'):
        if(mode=='day'):
            self.start_day_mode()
        else:
            self.start_night_mode()
        pass

    def start_day_mode(self):
        self.theme_params = {
            'background_color': 'white',
            'text_color': 'black',
            'poster_line_color': 'black',
        }
        pass

    def start_night_mode(self):
        self.theme_params = {
            'background_color': 'black',
            'text_color': 'white',
            'poster_line_color': 'gray',
        }
        pass
    
    def load_barlow(self, font_size=None):
        # Ruta a la fuente TTF personalizada
        font_path = "/app/data/Barlow-Medium.ttf"
        # Carga la fuente
        if font_size is None:
            self.font = ImageFont.truetype(font_path, self.prms['font_size'])
        else:
            self.font = ImageFont.truetype(font_path, font_size)
        pass

    def preview(self):
        plt.imshow(self.image)
        plt.axis('off')
        plt.show()

    def crop_image(self, top_cut, bottom_cut):
        width, height = self.image.size
        self.image = self.image.crop((0, top_cut, width, height - bottom_cut))
        pass

    def resize_image(self, target_width=None, target_height=None):
        """
        Ajusta el tamaño de la imagen mientras mantiene las proporciones.
        
        Args:
            image (PIL.Image.Image): La imagen a redimensionar.
            target_width (int, opcional): El ancho objetivo deseado.
            target_height (int, opcional): La altura objetivo deseada.
            
        Returns:
            PIL.Image.Image: La imagen redimensionada.
        """
        width, height = self.image.size
        aspect_ratio = width / height
        
        if target_width is None and target_height is None:
            raise ValueError("Debes proporcionar al menos una de las dimensiones objetivo.")
        
        if target_width is not None and target_height is None:
            new_width = target_width
            new_height = int(target_width / aspect_ratio)
        elif target_width is None and target_height is not None:
            new_width = int(target_height * aspect_ratio)
            new_height = target_height
        else:
            new_width = target_width
            new_height = target_height
        
        self.image = self.image.resize((new_width, new_height))
        pass
