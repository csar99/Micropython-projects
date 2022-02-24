from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(0), freq = 50)
servo.duty(20)


while True:
    for x in range(20, 135):
        servo.duty(x)
        print(x)
        sleep(0.01)
        
    
    for x in range (135, 20, -1):
        servo.duty(x)
        print(x)
        sleep(0.01)
        
