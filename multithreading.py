import _thread as th
import esp32
from machine import Pin
from time import sleep

led1 = Pin(19, Pin.OUT)
led2 = Pin(21, Pin.OUT)
led3 = Pin(23, Pin.OUT)


def function_led(message,t):
    while True:
        print(message)
        led1.on()
        sleep(t)
        led1.off()
        sleep(t)
        
def function_led1(message,t):
    while True:
        print(message)
        led2.on()
        sleep(t)
        led2.off()
        sleep(t)
        
def function_led2(message,t):
    while True:
        print(message)
        led3.on()
        sleep(t)
        led3.off()
        sleep(t)
        

try:
    th.start_new_thread(function_led("Led1",1))
    th.start_new_thread(function_led1("Led2",2))
    th.start_new_thread(function_led2("Led3",3))
except _thread.error as e:
    print("Threading is not initiated due to an internal error")
    
        