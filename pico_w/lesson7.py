from machine import Pin, Timer

def second1(t):
    print('過1秒')
    led.toggle()
    
led = Pin("LED", Pin.OUT)

timer = Timer(period=1000, mode=Timer.PERIODIC, callback = second1)
