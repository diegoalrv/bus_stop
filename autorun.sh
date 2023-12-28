#!/bin/bash

IMAGE=$HOME/pantallas-led/GenPoster/example/poster.png

#sudo python3 testapi_full.py
cd pantallas-led/GenPoster
#docker build -t bus_poster .
./run_container.sh

cd rpi-rgb-led-matrix/bindings/python/samples/

python3 image-viewer.py $IMAGE

