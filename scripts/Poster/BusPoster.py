import requests
import io
from io import BytesIO
from PIL import ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
from MyDraw import MyDraw

class BusPoster(MyDraw):

    def start_draw(self):
        return super().start_draw()

    def set_colors(self):
        width_border = self.prms['width_border']
        proportion = self.prms['proportion']
        fill_color_l = self.prms['letter_background_color']
        fill_color_n = self.prms['number_background_color']


        self.draw.rounded_rectangle(
            (0, 0, self.width-width_border, self.height-width_border),
            fill=fill_color_l,
            outline=self.theme_params['poster_line_color'],
            width=width_border,
            radius=5)
        
        self.draw.rounded_rectangle(
            (0, 0, proportion*self.width-width_border, self.height-width_border),
            fill=fill_color_n,
            outline=self.theme_params['poster_line_color'],
            width=width_border,
            radius=5)
        pass

    def set_bus_number(self, bus_number="11"):
        text_color = 'black'
        width_border = self.prms['width_border']
        text_bbox = self.font.getbbox(str(bus_number))
        font_width, font_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        offset_width = np.round((self.prms['proportion']*self.width-width_border)/2) - np.round(font_width/2)
        text_position = (offset_width,0)
        self.draw.text(
            text_position,
            bus_number,
            fill=text_color,
            font=self.font,
            # align ="center"
        )
        pass

    def set_bus_letter(self, bus_letter="E"):
        proportion = self.prms['proportion']
        width_border = self.prms['width_border']
        text_color = 'white'
        text_bbox = self.font.getbbox(str(bus_letter))
        font_width, font_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        offset_width = np.round((proportion*self.width-width_border)) + 0.75*np.round(font_width/2)
        text_position = (offset_width,0)
        self.draw.text(
            text_position,
            bus_letter,
            fill=text_color,
            font=self.font,
            # align ="center"
        )
        pass
