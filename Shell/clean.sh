#!/bin/bash


docker rmi -f 1d944d6be08c 476c64862aa8 9ce860831f20 f0f409088626 daff57b7d2d1 b1d0c95000bc fcfc4be7b807 4eec9f6b1651 bd704e547e4e e6037618a0d9
sudo apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-c
sudo rm -rf /var/lib/docker /etc/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/run/docker.sock
sudo rm -r oai-cn5g-fed
sudo rm installcorefirst.sh
sudo rm installcoresecond.sh
sudo rm finalizado.txt
