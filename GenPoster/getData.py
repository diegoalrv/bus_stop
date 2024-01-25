#!/usr/bin/env python3

import requests
import pytz
from datetime import datetime, timedelta


class Paradero:
    def __init__(self):
        # Dispositivo 
        self.id = "00000000160f3b42b8:27:eb:0f:3b:42"

        # Autentificación data
        self.url_auth = 'https://transporte.hz.kursor.cl/api/auth/'
        self.username = "usuario1"
        self.password = "usuario1"

        # Token obtenido luego del 'login'
        self.token = self.__get_token()
        print(self.token)

        # URL de la API para obtener los datos de los recorridos
        self.url_getinfodevice = 'https://transporte.hz.kursor.cl/api/dispositivos/getInfoDevice/'
        self.data = None
        self.bus_list = []


    def __get_token(self):
        auth = '''{
            "username": "usuario1",
            "password": "usuario1"
        }'''

        response = requests.post(self.url_auth, data=auth)

        # Estado de la respuesta
        if response.status_code == 200:
            return response.json()['token']
        else:
            return None

    def get_data(self):
        # Datos para la solicitud
        data_getinfodevice = {
            "GetInfoDevice": {
                "idDispositivo": self.id,
                "KeyAuthorizacion": "tokenSinUso"  #Autentificacion de mentira sisisi
            }
        }

        if self.token is not None:
            #Aquí se ingresa el token obtenido anteriormente
            headers_getinfodevice = {
                'Authorization': f'Bearer {self.token}',
                'Content-Type': 'application/json'  
            }

            # Request
            response = requests.post(self.url_getinfodevice, json=data_getinfodevice, headers=headers_getinfodevice)

            self.data = self.__serialize_data(response)
            return self.data

    def __generate_bus_list(self, info):
        data_main = []
        zona_horaria_santiago = pytz.timezone('America/Santiago')
        hora_actual_santiago = datetime.now(zona_horaria_santiago).time()

        for i in range(len(info["GetInfoDeviceResponse"]["DetalleLineas"])):

            data = info["GetInfoDeviceResponse"]["DetalleLineas"][i]

            bus_info = {}
            bus_info["distance"] = data["Llegadas"][0]["DistanciaGPS"] if data["Llegadas"][0]["DistanciaGPS"] is not None else "-"
            bus_info["timeLabel"] = data["Llegadas"][0]["EstimadaGPS"] if data["Llegadas"][0]["EstimadaGPS"] is not None else "-"
            bus_info["route"] = data["Descripcion"][:-1] if data["Descripcion"] is not None else "-"
            bus_info["direction"] = data["Descripcion"][-1] if data["Descripcion"] is not None else "-"
            bus_info["number_background_color"] = data["colorFondo"]
            bus_info["letter_background_color"] = data["colorTexto"]
            bus_info["patente"] = data["Llegadas"][0]["patente"]
            bus_hour = datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().hour if datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().hour != 0 else 24
            print(bus_hour, hora_actual_santiago.hour)
            diff = timedelta(
                hours = bus_hour - hora_actual_santiago.hour,
                minutes = datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().minute - hora_actual_santiago.minute,
                seconds=datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().second - hora_actual_santiago.second
            )
            print(diff.total_seconds())
            bus_info["timeRemaining"] = int(abs(diff.total_seconds() // 60))
            data_main.append(bus_info)

        data_main = sorted(data_main, key=lambda x: x['timeRemaining'])
        self.bus_list = data_main

        for d in data_main:
            print(d['timeRemaining'], d['timeLabel'])

    def __serialize_data(self, response):
        data = response.json()
        self.__generate_bus_list(data)
        data = self.bus_list[:2]

        return data