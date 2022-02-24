from machine import Pin, ADC
from time import sleep

pot = ADC(0)

# return int
def mapValue(value, in_min, in_max, out_min, out_max):
    return max(min(out_max, (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min), out_min)

while True:
    pot_val = pot.read()
    mappedVal = mapValue(pot_val, 0, 1024, -180, 180)
    print(mappedVal)
    sleep(0.2)


