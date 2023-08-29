import requests
import io
from io import BytesIO
from PIL import ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
from MyDraw import MyDraw

class DistanceAnnouncement(MyDraw):

    def start_draw(self):
        super().start_draw()
        self.border = 1

    def set_background(self):
        self.draw.rounded_rectangle(
            (0, 0, self.width-0.5*self.border, self.height-0.5*self.border),
            fill="#dcdcdc",
            outline="gray",
            width=self.border,
            radius=1)
        pass

    def set_base_text(self):
        text = "Distancia"
        text_color = self.theme_params['text_color']
        self.load_barlow(font_size=11)
        text_bbox = self.font.getbbox(text)
        font_width, font_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        # print(font_width, font_height)
        offset_width = (np.round((self.width-self.border)) - np.round(font_width))/2
        text_position = (offset_width,5)
        # text_position = (0, 0)
        self.draw.text(
            text_position,
            text,
            fill=text_color,
            font=self.font,
            align ="center"
        )
        pass

    def set_distance_text(self, distance):

        text = "Distancia"
        text_color = self.theme_params['text_color']
        self.load_barlow(font_size=11)
        text_bbox = self.font.getbbox(text)
        base_font_width, base_font_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]


        text = f'{distance} km'
        self.load_barlow(font_size=18)
        text_bbox = self.font.getbbox(text)
        font_width, font_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        # print(font_width, font_height)
        offset_width = (np.round((self.width-self.border)) - np.round(font_width))/2
        offset_height = (np.round((self.height-self.border)) - np.round(base_font_height))/2
        text_position = (offset_width,5+offset_height)
        # text_position = (0, 0)
        self.draw.text(
            text_position,
            text,
            fill=text_color,
            font=self.font,
            align ="center"
        )
