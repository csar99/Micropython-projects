import machine
# machine.freq(80000000) # default 80 MHz
# machine.freq(160000000) # Overclocked to 160 MHz; When the code does heavy processing
# we can switch to this frequency then change back when finished
print(machine.freq())
