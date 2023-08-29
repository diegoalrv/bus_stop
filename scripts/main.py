from MyDraw import MyDraw
from BusPoster import BusPoster
from TimeAnnouncement import TimeAnnouncement
from DistanceAnnouncement import DistanceAnnouncement
from BusPlate import BusPlate
from BusImage import BusImage

import numpy as np
from datetime import datetime, timedelta


def aprox(n):
    return int(np.round(n))

def load_data():
    data = {
        "direction": "R",
        "distance": 1948.575483806973,
        "epochTime": 1674650956,
        "latitude": -33.43729782104492,
        "licensePlate": "LJHA57",
        "longitude": -70.52730560302734,
        "realtime": True,
        "route": "401",
        "routeId": "401",
        "timeLabel": "09:49",
        "tripId": "401-I-L-005"
    }
    return data

def approx_km(data):
    distance_meters = data["distance"]
    distance_km = distance_meters / 100  # Convert meters to kilometers
    approx_km = int(np.round(distance_km))  # Take only the integer part of the distance in kilometers
    approx_km = approx_km/10.0
    return approx_km

def calc_remaining_time(data):
    arrival_time = data["timeLabel"]
    target_time = datetime.strptime(arrival_time, "%H:%M").time()
    current_time = datetime.now().time()

    if current_time < target_time:
        remaining_time = datetime.combine(datetime.today(), target_time) - datetime.combine(datetime.today(), current_time)
    else:
        remaining_time = datetime.combine(datetime.today() + timedelta(days=1), target_time) - datetime.combine(datetime.today(), current_time)

    remaining_minutes = int(remaining_time.total_seconds() // 60)
    return remaining_minutes

def obtain_min_max_time(remaining_time):
    if remaining_time == 1:
        return 0, 1
    elif remaining_time == 2:
        return 1, 2
    elif 2 <= remaining_time <= 5:
        return 2, 5
    elif remaining_time > 5 and remaining_time <= 7:
        return 5, 7
    elif remaining_time > 7 and remaining_time <= 10:
        return 7, 10
    else:
        return 10, remaining_time

data = load_data()

distance = approx_km(data)

remaining_time = calc_remaining_time(data)
min_time, max_time = obtain_min_max_time(remaining_time)

theme = 'day'

# panel_height, panel_width = 40, 80
# n_panels = 3
# height, width = n_panels*panel_height, n_panels*panel_width

height, width = 120, 240

full_panel = MyDraw(height=height, width=width)
full_panel.set_theme(theme)
full_panel.start_draw()
# full_panel.preview()

bp = BusPlate()
plate = data["licensePlate"]
bp.request_bus_plate(bus_plate=plate)
bp.generate_image()
bp.resize_image(target_height=aprox((3/10)*height))

dist_anmc = DistanceAnnouncement(aprox((2/5)*height), aprox((1/3)*width))
dist_anmc.set_theme(theme)
dist_anmc.start_draw()
# dist_anmc.set_background()
dist_anmc.set_base_text()
dist_anmc.set_distance_text(distance=distance)

time_anmc = TimeAnnouncement(aprox((2/5)*height), aprox((1/3)*width))
time_anmc.set_theme(theme)
time_anmc.start_draw()
# time_anmc.set_background()
time_anmc.set_base_text()
time_anmc.set_min_max_text(min_time=min_time, max_time=max_time)

poster = BusPoster(aprox((1/4)*height), aprox((1/4)*width))
poster.set_theme(theme)
poster.start_draw()

poster_params = {
    'proportion': 0.6,
    'width_border': 1,
    'font_size': 25,
    'number_background_color': 'yellow',
    'letter_background_color': 'green',
}

poster.set_params(poster_params)
poster.load_barlow()
poster.set_colors()
poster.set_bus_number(bus_number=data["route"])
poster.set_bus_letter(bus_letter=data["direction"])

bm = BusImage()
bm.set_theme(theme)
bm.load_image_from_url()
bm.crop_image(top_cut=165, bottom_cut=165)
bm.resize_image(target_width=aprox((1/3)*width))

full_panel.add_image(bp, (aprox(0.5*width), aprox((2/3)*height)))
full_panel.add_image(dist_anmc, (aprox((3/8)*width), aprox(0.1*height)))
full_panel.add_image(time_anmc, (aprox((2/3)*width), aprox(0.1*height)))
full_panel.add_image(poster, (aprox((1/6)*width), aprox((2/3)*height)))
full_panel.add_image(bm, (aprox(0.02*width),aprox((1/6)*height)))
full_panel.get_image()
full_panel.save_image('/app/data/output.png')

