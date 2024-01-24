import time
import urequests
from machine import Pin
from tools import connect, reconnect

red_led = Pin(15,mode=Pin.OUT)
while True:
    red_led.value(0)