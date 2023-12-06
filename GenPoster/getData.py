#!/usr/bin/env python3

import requests
import json


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

    def __serialize_data(self, response):
        data = response.json()
        data = data["GetInfoDeviceResponse"]["DetalleLineas"][0]

        bus_info = {}
        bus_info["distance"] = data["Llegadas"][0]["DistanciaGPS"] if data["Llegadas"][0]["DistanciaGPS"] is not None else "-"
        bus_info["timeLabel"] = data["Llegadas"][0]["EstimadaGPS"][:-3] if data["Llegadas"][0]["EstimadaGPS"] is not None else "-"
        bus_info["route"] = data["Descripcion"][:-1] if data["Descripcion"] is not None else "-"
        bus_info["direction"] = data["Descripcion"][-1] if data["Descripcion"] is not None else "-"

        return bus_info