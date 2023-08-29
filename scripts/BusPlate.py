import requests
import io
from io import BytesIO
from PIL import ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
from MyDraw import MyDraw

class BusPlate(MyDraw):
    def __init__(self, url=None) -> None:
        if url is None:
            self.url = "https://matriculasdelmundo.com/gRCH1.php"
        pass

    def set_url(self, url):
        self.url = url
        pass

    def get_image(self):
        if hasattr(self, 'image'):
            return self.image
        else:
            print("Error: No se ha generado ninguna imagen aún.")
            return None

    def request_bus_plate(self, bus_plate=None):
        if bus_plate is None:
            self.bus_plate = "AABB11"
        else:
            self.bus_plate = bus_plate

        params = {
            "textRCH1": self.bus_plate[0:2],
            "textRCH1A": self.bus_plate[2:4],
            "textRCH1B": self.bus_plate[4:],
            "textRCH1C": ""
        }

        self.response = requests.get(self.url, params=params)
        pass

    def save_bus_plate_image(self):
        if self.response.status_code == 200:
            filename = f"/app/data/output/plate_{self.bus_plate}.png" 
            with open(filename, "wb") as f:
                f.write(self.response.content)
            print(f"Imagen generada guardada como '{filename}'")
        else:
            print("Error al guardar la imagen generada")
        pass

    def generate_image(self):
        image_bytes = io.BytesIO(self.response.content)
        self.image = Image.open(image_bytes)
        self.image = self.image.convert("RGBA")  # Convertir a formato RGBA
        pass

    # def resize_image(self, new_size):
    #     proportion = np.min([self.image.size[0]/new_size[0], self.image.size[1]/new_size[1]])
    #     nx, ny = int(np.round(self.image.size[0]/proportion)), int(np.round(self.image.size[1]/proportion))
    #     self.image = self.image.resize((nx, ny))
    #     pass

    def preview(self):
        plt.imshow(self.image)
        plt.axis('off')
        plt.show()
        pass