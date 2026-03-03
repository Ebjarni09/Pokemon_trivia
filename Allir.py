import random
import neopixel
from machine import Pin
import time
from buzzer_music import music



NUM_LEDS = 35
pin = Pin(8, Pin.OUT)
np = neopixel.NeoPixel(pin, NUM_LEDS)  

takki = Pin(16, Pin.IN, Pin.PULL_UP)
takki1 = Pin(21, Pin.IN, Pin.PULL_UP)
takki2 = Pin(6, Pin.IN, Pin.PULL_UP)
takki3 = Pin(36, Pin.IN, Pin.PULL_UP)

reed = Pin(42, Pin.IN, Pin.PULL_UP)    



song = '64 E5 6 26;70 E5 7 26;80 C5 4 26;80 G5 4 26;84 F#5 4 26;88 C#5 4 26;88 E5 4 26;92 B5 4 26;96 E5 3 26;96 C#5 16 26;100 C5 7 26;104 B4 3 26;108 E5 4 26;112 E5 12 26;112 G5 6 26;118 G5 6 26;128 E5 6 26;128 D5 13 26;134 E5 7 26;144 G5 4 26;148 F#5 4 26;152 C#5 4 26;152 E5 4 26;156 B5 4 26;160 E5 3 26;160 C#5 16 26;164 C5 7 26;168 B4 3 26;172 E5 4 26;160 E5 3 26;48 E5 12 26;54 G5 6 26;64 D5 13 26;144 C5 4 26;16 C7 1 26;20 G7 1 26;24 B7 1 26;28 F#7 1 26;32 C7 1 26;36 G7 1 26;40 B7 1 26;44 F#7 1 26;48 C7 1 26;52 G7 1 26;56 B7 1 26;60 F#7 1 26;64 C7 1 26;68 G7 1 26;72 B7 1 26;76 F#7 1 26;92 F#7 1 26;88 B7 1 26;84 G7 1 26;80 C7 1 26;96 C7 1 26;100 G7 1 26;104 B7 1 26;108 F#7 1 26;112 C7 1 26;116 G7 1 26;120 B7 1 26;124 F#7 1 26;128 C7 1 26;132 G7 1 26;136 B7 1 26;140 F#7 1 26;144 C7 1 26;148 G7 1 26;152 B7 1 26;156 F#7 1 26;160 C7 1 26;164 G7 1 26;168 B7 1 26;172 F#7 1 26;176 C7 1 26;180 G7 1 26;184 B7 1 26;188 F#7 1 26;0 C7 1 26;4 G7 1 26;8 B7 1 26;12 F#7 1 26;48 G5 6 26'
mySong = music(song, pins=[Pin(4)])


while True:
    if takki.value() == 0:
        if random.random() < 0.15:
            color = (0, 100, 0)
        else:
            color = (100, 0, 0)
        
        for i in range(NUM_LEDS):
            np[i] = color
        np.write()

        time.sleep(1)

  
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)
        np.write()
       


    if takki1.value() == 0:
        if random.random() < 0.30:
            color = (0, 100, 0)
        else:
            color = (100, 0, 0)
        
        for i in range(NUM_LEDS):
            np[i] = color
        np.write()

        time.sleep(1)

  
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)
        np.write()
    
    if takki2.value() == 0:
        if random.random() < 0.50:
            color = (0, 100, 0)
        else:
            color = (100, 0, 0)
        
        for i in range(NUM_LEDS):
            np[i] = color
        np.write()

        time.sleep(1)

  
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)
        np.write()
    
    if takki3.value() == 0:
        if random.random() < 100.0:
            color = (0, 100, 0)
        else:
            color = (100, 0, 0)
        
        for i in range(NUM_LEDS):
            np[i] = color
        np.write()

        time.sleep(1)

  
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)
        np.write()

    if reed.value():
        print("Reed..." , reed.value())
    if not reed.value():
        print(mySong.tick())
        

