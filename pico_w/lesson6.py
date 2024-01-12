from machine import Pin
import time

start_ticks = time.ticks_ms()
led = Pin('LED', Pin.OUT)
led_status = False
while True:
    var_ticks = time.ticks_ms()
    if var_ticks - start_ticks >= 1000:
        start_ticks = time.ticks_ms()
        led_status = not led_status
        led.value(led_status)
        print('過1秒')