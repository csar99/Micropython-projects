from machine import Pin, PWM

pwm0 = PWM(Pin(0)) # create PWM object from a pin
print(pwm0.freq()) # get current frequency
 
pwm0.freq(1000)    # set frequency
print(pwm0.freq()) 

print(pwm0.duty()) # get current duty cycle

pwm0.duty(400)     # set duty cycle
print("Duty: ",pwm0.duty())

pwm0.deinit()      # turn off PWM on the pin

print("New duty: ",pwm0.duty())

pwm2 = PWM(Pin(2), freq=500, duty=512) # create and configure in one go
print("freq: ", pwm2.freq(), " duty: ", pwm2.duty())
