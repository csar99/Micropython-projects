from machine import Pin, ADC
from time import sleep

# A0 pin
pot = ADC(0)

while True:
    pot_val = pot.read()
    
    # mappedVal = map(pot_val, 0, 1024, -180, 180)
    print(pot_val)
    sleep(0.1)



