#!/usr/bin/python
# -*- coding: utf-8 -*-
# Inport modules

from gpiozero import Button
from time import sleep
from datetime import datetime

# Variables

door = Button(26)
now = datetime.now()
current_time = now.strftime('%H:%M:%S')

# open and read the file after the appending:

f = open('log.txt', 'r')
print f.read()

print "It's working!"

while True:
    if door.is_pressed:
        # File handling
        f = open('log.txt', 'w')
        f = open('log.txt', 'a')
        f.write('Your door was opened at', current_time)
        f.close()
    sleep(1)
