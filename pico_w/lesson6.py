from machine import Pin
import time

start_ticks = time.ticks_ms()
led = Pin('LED', Pin.OUT)
led_status = False


start1 = time.ticks_ms()
start2 = time.ticks_ms()
start3 = time.ticks_ms()
while True:
    for start, second, text in [(start1, 1000, '過1秒'), (start2, 5000, '過5秒'), (start3, 10000, '過10秒')]:
        if time.ticks_diff(time.ticks_ms(), start) >= second:
            print(start, second, text)
            if start == start1:
                start1 = start1 + 1000
            if start == start2:
                start2 = start2 + 5000
                print(start2)
            if start == start3:
                start3 = start3 + 10000
 