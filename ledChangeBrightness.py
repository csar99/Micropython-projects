from machine import Pin, PWM
from time import sleep

# Suitable frequency to change a brightness of a led 5000Hz
frequency = 5000

# Creates a PWM Object
# GPIO 5 = D1
led = PWM(Pin(5), frequency)

while True:
    for duty_cycle in range (0, 1024):
        led.duty(duty_cycle)
        print(duty_cycle)
        sleep(0.001)
    
    for duty_cycle in range (1024, 0, -1):
        led.duty(duty_cycle)
        print(duty_cycle)
        sleep(0.001)
    
    