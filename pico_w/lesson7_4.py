import time
import urequests
from machine import ADC, Pin, Timer, RTC
from tools import connect, reconnect

connect()
adc = ADC(4)
conversion_factor = 3.3/65535
start_time = 0
duration = 30

def alert(temperature):
    global start_time
    if time.ticks_diff(time.ticks_ms(), start_time) >= duration * 1000:
        rtc = RTC()
        datetime_tuple = rtc.datetime()
        datetime_str = f'{datetime_tuple[0]}-{datetime_tuple[1]}-{datetime_tuple[2]} {datetime_tuple[4]}:{datetime_tuple[5]}:{datetime_tuple[6]}'
        webhook_url = f'https://hook.eu2.make.com/lxhmsr8brzqjd2kpmpeoenrbmt6mziva?date={datetime_str}&temperature={temperature}&location=%E5%AD%B8%E9%99%A2'
        try:
            response = urequests.get(webhook_url)
        except:
            print("ap出現問題")
            reconnect()
        else:
            if response.status_code == 200:            
                print("傳送訊息成功")
            else:
                print("傳送失敗(make服務出問題)")
            response.close()
        start_time = time.ticks_ms()
        

# The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
# Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
def second1(t):
    reading_v = adc.read_u16() * conversion_factor
    celsius = 27 - (reading_v-0.706) / 0.001721
    print(celsius)
    if celsius > 22:
        alert(celsius)
    
tim1 = Timer()
tim1.init(period=1000, callback=second1)
    