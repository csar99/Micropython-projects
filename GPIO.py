from machine import Pin
from time import sleep

pin0 = Pin(0, Pin.IN); # can only read 1 or 0
# pin0.on() = pin0.value(1)
# pin0.off() = pin0.value(0)
while True:
    print(pin0.value())
    sleep(0.2)
    
# p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation