#!/bin/bash

# My Hello, World! script
echo "Hello, World!"

# Upgrade Ubuntu
sudo apt update
sudo apt upgrade 

# List the recommended NVIDIA drivers
sudo apt install ubuntu-drivers-common
sudo ubuntu-drivers devices
