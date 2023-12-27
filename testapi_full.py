#!/usr/bin/env python3

import requests
import json
from datetime import datetime, timedelta

# URL de la API para "autentificación"
url_auth = 'https://transporte.hz.kursor.cl/api/auth/'

# Datos para autentificar
auth = '''{
    "username": "usuario1",
    "password": "usuario1"
}'''

# Request
token = requests.post(url_auth, data=auth)

# Estado de la respuesta
if token.status_code == 200:
    # solicitud exitosa
    print('Respuesta de token exitosa!')
else:
    # Error en la solicitud
    print('Error en la solicitud del token:', token.status_code, token.text)

token = token.json()['token']

print('-----------------------------------------------------')
print('Token Obtenido: ' + token)
print('-----------------------------------------------------')

#--------------------------------------------------------

# URL de la API para info del paradero
url_whoami = 'https://transporte.hz.kursor.cl/api/dispositivos/whoami/'

# Datos de la solicitud
data_whoami = {
    "whoami": {
        "idDispositivo": "pled30-gtr", #Aquí dejaron esta id por defecto....
        "KeyAuthorizacion": "token" #Autentificacion de mentira sisisi (la real está comenta después de esta variable
    }
}

#Aquí se ingresa el token obtenido anteriormente
headers_whoami = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json' 
}

# Request
response_whoami = requests.post(url_whoami, json=data_whoami, headers=headers_whoami)

# Estado de la respuesta
if response_whoami.status_code == 200:
    # Solicitud exitosa
    print('Respuesta API "whoami" exitosa')
else:
    # Error en la solicitud
    print('Error en la solicitud de API "whoami": ', response_whoami.status_code, response_whoami.text)


Paradero = response_whoami.json()
#print(json.dumps(Paradero, indent=4, ensure_ascii=False, sort_keys=True))

print('-----------------------------------------------------')


# URL de la API para obtener los datos de los recorridos
url_getinfodevice = 'https://transporte.hz.kursor.cl/api/dispositivos/getInfoDevice/'

# Datos para la solicitud
data_getinfodevice = {
    "GetInfoDevice": {
        "idDispositivo": "00000000160f3b42b8:27:eb:0f:3b:42", #Para esta solicitud, pusieron la id del equipo que les dimos
        "KeyAuthorizacion": "tokenSinUso"  #Autentificacion de mentira sisisi
    }
}

#Aquí se ingresa el token obtenido anteriormente
headers_getinfodevice = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'  
}

# Request
response_getinfodevice = requests.post(url_getinfodevice, json=data_getinfodevice, headers=headers_getinfodevice)

# Estado de la respuesta
if response_getinfodevice.status_code == 200:
    # Solicitud exitosa
    print('Respuesta API "GetInfoDevice" exitosa')
else:
    # Error en la solicitud
    print('Error en la solicitud de API "GetInfoDevice": ', response_getinfodevice.status_code, response_getinfodevice.text)

info = response_getinfodevice.json()
#print(json.dumps(info, indent=4, ensure_ascii=False, sort_keys=True))

print("----------------------------------------------------------")
print("Cantidad de buses con llegada registrada en este paradero:", len(info["GetInfoDeviceResponse"]["DetalleLineas"]))
print("----------------------------------------------------------")

#Haciendo una lista de todos los buses de este paradero

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
    diff = timedelta(hours = datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().hour - hora_actual.hour,minutes = datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().minute - hora_actual.minute,seconds = datetime.strptime(bus_info["timeLabel"], "%H:%M:%S").time().second - hora_actual.second)
    bus_info["timeRemaining"] = int(abs(diff.total_seconds() // 60))
    data_main.append(bus_info)

#Cálculo del tiempo estimado de llegada para cada bus

data_time = sorted(data_main, key=lambda x: x['timeRemaining'])
#data_time = data_main

print("Buses ordenados según hora de llegada:\n")
print("Hora Actual (CL): ", datetime.now().strftime("%H:%M:%S"))
print("Paradero N°", Paradero["WhoamiResponse"]["NroParadero"], Paradero["WhoamiResponse"]["NombreParadero"],"\n")

for n in data_time:
    #print(n)
    print("Recorrido:",n["route"],n["direction"],"| Patente:",n["patente"],"| Tiempo restante de llegada:", n["timeRemaining"],"minutos.")

print("--------------------------------------------------------------")

#Exportando datos

#def export_data():
#    data_x = (data_time[0],data_time[1])
#    return data_x

#data_x = (data_time[0],data_time[1])
#print(data_x)


