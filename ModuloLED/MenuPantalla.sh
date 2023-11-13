#!/bin/bash

cd samples
echo "Este es un Menú para controlar Módulos LED"
echo "¿Que acción desea realizar?:"
echo "1. Editar código base"
echo "2. Desplegar Imagen"
read N

if [ $N -eq 1 ]
then

nano image-viewer.py

else

ls
echo "Ingrese el nombre del archivo que desea desplegar:"
read filename

sudo python3 image-viewer.py $filename

fi
