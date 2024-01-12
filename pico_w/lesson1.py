import machine
import time
from machine import Pin

led = Pin('LED', Pin.OUT)
while True:
    print(machine.freq())
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    
    