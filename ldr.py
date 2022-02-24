from machine import Pin, ADC
from time import sleep

ldr = ADC(0)

while True:
    ldrVal = ldr.read()
    print(ldrVal)
    sleep(0.1)