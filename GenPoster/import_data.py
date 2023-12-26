#!/usr/bin/env python3

import requests
import json
from datetime import datetime, timedelta

def api_request():
    # URL de la API para "autentificación"
    url_auth = 'https://transporte.hz.kursor.cl/api/auth/'

    # Datos para autentificar
    auth = '''{
        "username": "usuario1",
        "password": "usuario1"
    }'''

    # Request
    token = requests.post(url_auth, data=auth)
    token = token.json()['token']

    # URL de la API para info del paradero
    url_whoami = 'https://transporte.hz.kursor.cl/api/dispositivos/whoami/'

    # Datos de la solicitud
    data_whoami = {
        "whoami": {
            "idDispositivo": "pled30-gtr",
            "KeyAuthorizacion": "token"
        }
    }

    #Aquí se ingresa el token obtenido anteriormente
    headers_whoami = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response_whoami = requests.post(url_whoami, json=data_whoami, headers=headers_whoami) #Request
    Paradero = response_whoami.json()

    url_getinfodevice = 'https://transporte.hz.kursor.cl/api/dispositivos/getInfoDevice/' # URL de la API para obtener los datos de los recorridos

    # Datos para la solicitud
    data_getinfodevice = {
        "GetInfoDevice": {
        "idDispositivo": "00000000160f3b42b8:27:eb:0f:3b:42",
        "KeyAuthorizacion": "tokenSinUso"
        }
    }

    #Aquí se ingresa el token obtenido anteriormente
    headers_getinfodevice = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Request
    response_getinfodevice = requests.post(url_getinfodevice, json=data_getinfodevice, headers=headers_getinfodevice)
    info = response_getinfodevice.json()

    return info

#--------------------------------------------------------------------------------------------------------------------------

#Haciendo una lista de todos los buses de este paradero

def lista_buses(info):
    data_main = []
    hora_actual = datetime.now().time()

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
        diff = timedelta(hours = datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().hour - hora_actual.hour,minutes = datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().minute - hora_actual.minute,seconds=datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().second - hora_actual.second)
        bus_info["timeRemaining"] = int(abs(diff.total_seconds() // 60))
        data_main.append(bus_info)

    return data_main

#--------------------------------------------------------------------------------------------------------------------------------

#Exportando datos
def export_data():
    X = api_request()
    data_main = lista_buses(X)
    data_time = sorted(data_main, key=lambda x: x['timeRemaining'],reverse=True)

    data_x = (data_time[0],data_time[1])
    return data_x
