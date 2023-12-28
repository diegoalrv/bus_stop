#!/bin/bash

IMAGE=$HOME/pantallas-led/GenPoster/example/poster.png

#sudo python3 testapi_full.py
cd pantallas-led/GenPoster
#docker build -t bus_poster .
./run_container.sh

cd $HOME/rpi-rgb-led-matrix/bindings/python/samples/

sudo python3 image-viewer.py $IMAGE