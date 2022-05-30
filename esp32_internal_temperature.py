import esp32
from time import sleep

temp_f = esp32.raw_temperature()
temp_c = (temp_f - 32)/1.8

while True:
    print("Temp in Fahrenheit is: ", temp_f)
    print("Temp in degrees celsius is: ", temp_c)
    sleep(2)