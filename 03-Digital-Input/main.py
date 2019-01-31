from machine import Pin

led = Pin(5, Pin.OUT)
btn = Pin(0, Pin.IN)

while True:
    if btn() == 0:
        led.on()
    else:
        led.off() 