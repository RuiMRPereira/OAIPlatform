#!/bin/bash

echo yes | sudo apt install git
sudo apt install -y libboost-all-dev libusb-1.0-0-dev doxygen python3-docutils python3-mako python3-numpy python3-requests python3-ruamel.yaml python3-setuptools cmake build-essential
git clone https://github.com/EttusResearch/uhd.git 
cd ~/uhd
git checkout v4.0.0.0
cd host
mkdir build
cd build
cmake ../
make -j 4
make test 
echo rmarcelo | sudo -S make install
echo rmarcelo | sudo -S ldconfig
echo rmarcelo | sudo -S uhd_images_downloader

cd

git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git
cd ~/openairinterface5g
git checkout develop
cd ~/openairinterface5g
source oaienv
cd cmake_targets
./build_oai -I
cd ~/openairinterface5g
source oaienv
cd cmake_targets
./build_oai -w USRP --nrUE --build-lib all -c
cd
echo feito > finalizadooaiue.txt


