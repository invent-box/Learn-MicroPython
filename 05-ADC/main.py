# Video: Learn MicroPython #5 - ADC

# ESP32 has 18 ADC pins, but only 8 are usable with MicroPython, #32-39

# Step One - import
# ========

from machine import Pin, ADC

# Step Two - create Pin
# ========

pin34 = Pin(34, mode=Pin.IN)  # setting to IN is optional since it is defualt
adc = ADC(pin34)

# ... or alternatively ...

adc = ADC(Pin(34))

# Step Three - set voltage range ("attenuation")
# ==========
# There are four attenuation options. Most likely you will want to change
# this setting to 11dB to use the full 3.6V range

adc.atten(ADC.ATTN_0DB)     # 0dB   => 1.00V max (default)
adc.atten(ADC.ATTN_2_5DB)   # 2.5db => 1.34V max
adc.atten(ADC.ATTN_6DB)     # 6dB   => 2.00V max
adc.atten(ADC.ATTN_11DB)    # 11db  => 3.60V max

# Step Four - set precision
# =========
# There are four precision options. The default option is most precise, 
# so most likely you don't need to bother changing the width.

adc.width(ADC.WIDTH_9BIT)   # 9 bits    => 0-511
adc.width(ADC.WIDTH_10BIT)  # 10 bits   => 0-1023
adc.width(ADC.WIDTH_11BIT)  # 11 bits   => 0-2047
adc.width(ADC.WIDTH_12BIT)  # 12 bits   => 0-4095 (default)

# Step Six - read raw ADC count
# ========

value = adc.read()

# Step Seven - convert to voltage
# ==========
# Remember that an ADC works by increasing an internal voltage in small steps
# until it matches the voltage present on the pin, so the value read from the ADC is actually a count, not a voltage.

# Assuming 12 bit precision and 11dB (3.6V) range:

voltage = value / 4095.0 * 3.6

print(voltage)

# ... and now you're done. Here's a full example:

# Example
# =======
# Print voltage on pin 34 every second

from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)

while True:
    value = adc.read()
    voltage = value / 4095.0 * 3.6

    print(voltage)

    time.sleep(1)
