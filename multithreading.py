import _thread as th
import esp32
from machine import Pin
from time import sleep

led1 = Pin(2, Pin.OUT)


def function_led(message,t):
    while True:
        print(message)
        led1.on()
        sleep(t)
        led1.off()
        sleep(t)
def read_internal_temperature(message,t):
    while True:
        temp_f = esp32.raw_temperature()
        print(message)
        print("ESP32 internal temperature in °F is: ",temp_f)
        sleep(t)
def read_halleffect_sensorvalue(message,t):
    while True:
        print(message)
        h_value = esp32.hall_sensor()
        print("ESP32 hall effect sensor value is: ",h_value)
        sleep(t)
        
try:
    th.start_new_thread(function_led("Led1",1))
    th.start_new_thread(read_internal_temperature("esp32 temp",2))
    th.start_new_thread(read_halleffect_sensorvalue("esp32 hall sensor value",3))
except _thread.error as e:
    print("Threading is not initiated due to an internal error")
    
        