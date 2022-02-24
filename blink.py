from machine import Pin
import time

led = Pin(0, Pin.OUT)

while(1):
    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.05)