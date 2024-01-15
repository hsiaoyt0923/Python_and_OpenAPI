from machine import ADC, Pin, Timer

adc = ADC(4)
conversion_factor = 3.3/65535

def second1(t):
    reading_v = adc.read_u16() * conversion_factor
    celsius = 27 - (reading_v-0.706) / 0.001721
    print(celsius)    

    
tim1 = Timer()
tim1.init(period=1000, callback=second1)
    