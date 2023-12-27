#!/bin/bash


#sudo python3 testapi_full.py
cd pantallas-led/GenPoster
#docker build -t bus_poster .
./run_container.sh
cd example
sleep 4
feh poster.png


