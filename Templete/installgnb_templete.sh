#!/bin/bash

echo yyyyy | sudo -S apt install -y git
echo yyyyy | sudo -S apt install -y libboost-all-dev libusb-1.0-0-dev doxygen python3-docutils python3-mako python3-numpy python3-requests python3-ruamel.yaml python3-setuptools cmake build-essential
git clone https://github.com/EttusResearch/uhd.git
cd ~/uhd
git checkout v4.0.0.0
cd host
mkdir build
cd build
cmake ../
make -j 4
make test
echo yyyyy | sudo -S make install
echo yyyyy | sudo -S ldconfig
echo yyyyy | sudo -S uhd_images_downloader

cd
git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git
cd ~/openairinterface5g
git checkout develop
cd ~/openairinterface5g
source oaienv
cd cmake_targets
echo yyyyy | ./build_oai -S -I
cd ~/openairinterface5g
source oaienv
cd cmake_targets
echo yyyyy | ./build_oai -S -w USRP --gNB --build-lib all -c
cd
echo feito > finalizadognb.txt

