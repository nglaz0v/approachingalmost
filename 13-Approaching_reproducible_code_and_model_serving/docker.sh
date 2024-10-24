#!/bin/sh

# install docker
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker

sudo groupadd docker
sudo usermod -aG docker $USER

# build docker container
docker build -f Dockerfile -t bert:train .

# log into docker container
docker run -ti bert:train /bin/bash

# run script inside docker container
docker run -ti bert:train python3 train.py

# install the NVIDIA docker runtime
# taken from: https://github.com/NVIDIA/nvidia-docker/
# Add the package repositories
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

# start training process
docker run --gpus 1 -v /home/abhishek/workspace/approaching_almost/input/:/home/abhishek/data/ -ti bert:train python3 train.py

# a sample cURL request
curl $'http://192.168.86.48:5000/predict?sentence=this%20is%20the%20best%20book%20ever'
firefox "http://127.0.0.1:5000/predict?sentence=this%20book%20is%20too%20complicated%20for%20me"

# build a new docker container
docker build -f Dockerfile -t bert:api .

# run a new docker container
docker run -p 5000:5000 -v /home/abhishek/workspace/approaching_almost/input/:/home/abhishek/data/ -ti bert:api /home/abhishek/.local/bin/gunicorn api:app --bind 0.0.0.0:5000 --workers 4

# install docker-compose
pip3 install docker-compose
# run docker-compose
docker-compose up

