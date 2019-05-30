from NeuroPy.NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy() 
neuropy.start()

while True:
    print(neuropy.blinkStrength)
    if neuropy.blinkStrength > 1: # Access data through object
        print(".")
        print(neuropy.blinkStrength)
        neuropy.stop() 
    sleep(0.2) # Don't eat the CPU cycles