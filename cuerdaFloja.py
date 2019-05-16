#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#Path must be from a color
y = [255, 255, 0]

#Not path is defined by this color
x = [0, 0, 0]

#Character goes here
#color of the character
b = [0, 0, 255]

#Position of the character
charx = 0
chary = 0

#This is added after choosing color and 

#Draw the path in pixels
path = [
  y,y,y,x,x,x,x,x,
  x,x,y,x,x,x,x,x,
  x,x,y,x,x,x,x,x,
  x,x,y,y,y,y,y,x,
  x,x,x,x,x,x,y,x,
  x,x,x,x,x,x,y,x,
  x,x,x,x,y,y,y,x,
  x,x,x,x,y,x,x,x
]

while True:
    #Show the path
    sense.set_pixels(path)

    #Place character
    sense.set_pixel(charx, chary, b)

    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']

    print('Pitch:', pitch)
    print('Roll:', roll)

    if 270 < pitch < 315 and charx < 7:
        charx += 1

    if 45 < pitch < 90 and charx > 0:
        charx -= 1

    if 270 < roll < 315 and chary > 0:
        chary -= 1

    if 45 < roll < 90 and chary < 7:
        chary += 1

    current = sense.get_pixel(charx, chary)
        
    if current == x:
        charx = 0
        chary = 0
        
    #sleep(0.4)

