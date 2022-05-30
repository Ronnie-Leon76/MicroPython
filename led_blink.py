import machine, time
from machine import Pin
from time import sleep

led_obj = Pin(2, Pin.OUT)

while True:
    led_obj.value(1)
    sleep(0.2)
    led_obj.value(0)
    sleep(0.2)