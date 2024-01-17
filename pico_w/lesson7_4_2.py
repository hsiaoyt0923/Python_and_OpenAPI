import time
import urequests
from machine import Pin, ADC, RTC, Timer
from tools import connect, reconnect

connect()
adc = ADC(4)
conversion_rate = 3.3/65535
start_time = 0
duration = 30

def alert(temperature:float):
    global start_time
    if time.ticks_diff(time.ticks_ms(), start_time) >= duration * 1000:
        print('警告溫度過高')
        rtc = RTC()
        date_tuple = rtc.datetime()
        date_str = f'{date_tuple[0]}-{date_tuple[1]}-{date_tuple[2]} {date_tuple[4]}:{date_tuple[5]}:{date_tuple[6]}'
        webhook_url = f'https://hook.eu2.make.com/lxhmsr8brzqjd2kpmpeoenrbmt6mziva?date={date_str}&temperature={temperature}&location=pico_w_rp2040'
        try:
            res = urequests.get(webhook_url)
        except:
            print('wifi有問題')
            reconnect()
        else:
            if res.status_code == 200:
                print('傳送訊息成功')
            else:
                print('傳送訊息失敗(make伺服器有問題)')
            res.close()
        start_time = time.ticks_ms()

def check(t):
    reading_v = adc.read_u16() * conversion_rate
    celsius = 27 - (reading_v - 0.706) / 0.001721
    print(celsius)
    if celsius >= 22:
        alert(celsius)

timer = Timer(period=1000, callback=check)