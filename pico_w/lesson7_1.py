from machine import Pin, Timer

led = Pin('LED', Pin.OUT)

i = 0
def second1(t):
    global i
    i += 1
    led.toggle()
    print('過1秒')
    if i >= 3:
        t.deinit()
        
tim1 = Timer()
tim1.init(period=1000, callback=second1)