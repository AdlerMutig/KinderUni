#!/bin/python3

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

#Define colors
R = [255, 0, 0] #Red
O = [255, 165, 0]
# Individual step could be add the rest of the colors
# Yellow
# Green
# Blue
# Indigo
# violet
Y = [255, 255, 0]
G = [0, 128, 0]
B = [0, 0, 255]
I = [75, 0, 130]
V = [238, 130, 238]
# Test each color with
# sense.clear(X) #sets entire screen one color
#Empty color
X = [0, 0, 0]

#Rainbow matrix
rainbow = [
    R, R, R, R, R, R, R, R,
    R, O, O, O, O, O, O, O,
    R, O, Y, Y, Y, Y, Y, Y,
    R, O, Y, G, G, G, G, G,
    R, O, Y, G, B, B, B, B,
    R, O, Y, G, B, I, I, I,
    R, O, Y, G, B, I, V, V,
    R, O, Y, G, B, I, V, X]



while True:
    print("Humidity: ")
    print(sense.humidity)
    print("Temperature: ")
    print(sense.temp)
    if sense.humidity > 80 and sense.temp > 20 :
        sense.set_pixels(rainbow)
    else:
        sense.clear()



