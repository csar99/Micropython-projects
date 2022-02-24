import dht
import machine

d = dht.DHT11(machine.Pin(4))

print("temp ", d.temperature()) # eg. 23 (°C)

print("humadity ",d.humidity()) # eg. 41 (% RH)
