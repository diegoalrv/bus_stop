#!/bin/bash

# Rutas absolutas a las carpetas locales
project_folder_path=$(pwd)
data_path=$project_folder_path/data
scripts_path=$project_folder_path/scripts
assets_path=$project_folder_path/assets

# Ejecuta el contenedor con el enlace de carpeta local
# docker run --rm -d -p 8888:8888 --name make_poster -v $data_path:/app/data -v $assets_path:/app/assets -v $scripts_path:/app/scripts -v $project_folder_path:/app bus_poster
docker run --rm -d --name make_poster -v $project_folder_path:/app bus_poster