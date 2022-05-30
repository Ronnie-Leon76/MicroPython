import esp32
from time import sleep

while True:
    hall_val = esp32.hall_sensor()
    print("Hall sensor val is: ", hall_val)
    sleep(1)