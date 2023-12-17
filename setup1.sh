# Install the driver 
sudo apt install nvidia-driver-535

# Reboot your system
sudo reboot now

# Check the driver installation
nvidia-smi

# Install GCC
sudo apt install gcc
gcc -v

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-3

sudo apt-get install python3.9.16

sudo reboot now

# chmod +x setup.sh
# ./setup.sh