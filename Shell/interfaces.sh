#!/bin/bash

/sbin/ip -4 -o a | cut -d ' ' -f 2 | cut -d '/' -f 1 > ocupadas.txt
ls /sys/class/net > todas.txt

