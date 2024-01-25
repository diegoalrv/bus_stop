from scripts.Poster.MyDraw import MyDraw
from scripts.Poster.BusPoster import BusPoster
from scripts.Poster.TimeAnnouncement import TimeAnnouncement
import numpy as np
from datetime import datetime, timedelta
from import_data import export_data
from PIL import Image
from getData import Paradero

def reescalar_imagen(input_path, output_path, nuevo_ancho, nuevo_alto):
    try:
        # Abrir la imagen original
        imagen = Image.open(input_path)

        # Reescalar la imagen
        imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

        # Guardar la imagen redimensionada en el nuevo archivo
        imagen_redimensionada.save(output_path)
        print("Imagen redimensionada y guardada con éxito en", output_path)

    except Exception as e:
        print("Ocurrió un error:", str(e))

def aprox(n):
    return int(np.round(n))

def approx_km(data):
    distance_meters = data["distance"]
    distance_km = distance_meters / 100  # Convert meters to kilometers
    approx_km = int(np.round(distance_km))  # Take only the integer part of the distance in kilometers
    approx_km = approx_km/10.0
    return approx_km

def calc_remaining_time(data):
    arrival_time = data["timeLabel"][:-3]
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
    
###################################################################
# Parametros para generar la imagen
# "direction": "R", Indicador de la dirección en la que va el bus
# "distance": 1948.575483806973. Distancia en m
# "licensePlate": "LJHA57", Patente del bus
# "route": "401", Linea de bus
# "timeLabel": "09:49", Hora de llegada al paradero

# theme: Tema de la pantalla "day/night"
# 'number_background_color': 'yellow', Color del fondo para el numero
# 'letter_background_color': 'green', Color del fondo para la letra

def main():
    bus_stop = Paradero()

    data = bus_stop.get_data()
    data1 = data[0]
    data2 = data[1]

    print(data)

    # Calcula el tiempo restante a la llegada
    remaining_time1 = data1['timeRemaining']
    remaining_time2 = data2['timeRemaining']
    # Obtiene valores máximos y mínimo de rangos para desplegar en pantalla
    min_time1, max_time1 = obtain_min_max_time(remaining_time1)
    min_time2, max_time2 = obtain_min_max_time(remaining_time2)

    # Selecciona el tema
    theme = 'night'

    # Alto y ancho de la imagen en pixeles
    #height, width = 40, 160
    height, width = 200, 800

    # Inicia el dibujo y setea el tema
    full_panel = MyDraw(height=height, width=width)
    full_panel.set_theme(theme)
    full_panel.start_draw()

    # Agrega el anuncio de los minutos restante al arribo
    time_anmc1 = TimeAnnouncement(aprox((2/5)*height), aprox((1/3)*width))
    time_anmc1.set_theme(theme)
    time_anmc1.start_draw()
    # time_anmc1.set_background()
    # time_anmc1.set_base_text()
    time_anmc1.set_min_max_text(min_time=min_time1, max_time=max_time1)

    # Agrega el anuncio de los minutos restante al arribo
    time_anmc2 = TimeAnnouncement(aprox((2/5)*height), aprox((1/3)*width))
    time_anmc2.set_theme(theme)
    time_anmc2.start_draw()
    # time_anmc2.set_background()
    # time_anmc2.set_base_text()
    time_anmc2.set_min_max_text(min_time=min_time2, max_time=max_time2)

    # Genera la imagen de la linea del bus
    poster1 = BusPoster(aprox(1.1*(1/3)*height), aprox(1.1*(1/3)*width))
    poster1.set_theme(theme)
    poster1.start_draw()

    bus_announcement_1 = {
        'proportion': 0.6,
        'width_border': 3,
        # 'font_size': 11,
        'font_size': 80,
        'number_background_color': 'yellow',
        'letter_background_color': 'green',
    }

    # Se setean los parametros
    poster1.set_params(bus_announcement_1)
    poster1.load_barlow()
    poster1.set_colors()

    # Se setea la ruta y la direccion en la que va
    poster1.set_bus_number(bus_number=data1["route"])
    poster1.set_bus_letter(bus_letter=data1["direction"])

    # Genera la imagen de la linea del bus
    poster2 = BusPoster(aprox(1.1*(1/3)*height), aprox(1.1*(1/3)*width))
    poster2.set_theme(theme)
    poster2.start_draw()

    bus_announcement_2 = {
        'proportion': 0.6,
        'width_border': 3,
        # 'font_size': 11,
        'font_size': 80,
        'number_background_color': 'yellow',
        'letter_background_color': 'blue',
    }

    # Se setean los parametros
    poster2.set_params(bus_announcement_2)
    poster2.load_barlow()
    poster2.set_colors()
    # Se setea la ruta y la direccion en la que va
    poster2.set_bus_number(bus_number=data2["route"])
    poster2.set_bus_letter(bus_letter=data2["direction"])

    # Se agregan todas las imagenes al canvas
    full_panel.add_image(time_anmc1, (aprox((0.6)*width), aprox(0.05*height)))
    full_panel.add_image(time_anmc2, (aprox((0.6)*width), aprox(0.45*height)))
    full_panel.add_image(poster1, (aprox((0.05)*width), aprox((0.1)*height)))
    full_panel.add_image(poster2, (aprox((0.05)*width), aprox((0.5)*height)))
    #full_panel.add_image(bm, (aprox(0.02*width),aprox((1/6)*height)))
    full_panel.get_image()
    full_panel.save_image('/app/example/poster.png')

    nuevo_alto = 40  # Reemplaza con el alto deseado en píxeles
    nuevo_ancho = 160  # Reemplaza con el ancho deseado en píxeles
    input_path = f'/app/example/poster.png'
    output_path = f'/app/example/poster_{nuevo_alto}_{nuevo_ancho}.png'

    reescalar_imagen(input_path, output_path, nuevo_ancho, nuevo_alto)

if __name__ == '__main__':
    main()
