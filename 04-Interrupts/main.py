# Video: Learn MicroPython #4 - Interrupts

from machine import Pin

led = Pin(5, Pin.OUT)
btn = Pin(0, Pin.IN)

def my_func(pin):
    print("rising!")

# Interrupt Request
btn.irq(my_func, Pin.IRQ_RISING)
