# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

#importing the Pin Class from the machine module to be able to interact with GPIOs
from machine import Pin
#importing the network library to allow us connect esp boards to the Wi-Fi network
import network,time

#Turning off vendor OS debugging messages
# import esp
# esp.osdebug(None)

"""
Running a garbage collector.
A garbage collector is a way to reclaim memory occuppied by objects that are not no longer
used by the program
"""
import gc
gc.collect()

#Variables to hold network credentials
ssid = 'lemur'
password = 'alexgathua105'

#setting esp32 as a Wi-Fi station
station = network.WLAN(network.STA_IF)

# Activating the station and connecting to the router using the SSID and Password
station.active(True)
station.connect(ssid, password)

#Ensure that the code does not proceed if esp is not connected to your network
while station.isconnected() == False:
    station.connect(ssid, password)
    time.sleep(5)
    if station.isconnected() == True:
      break

#Indicate successful connection and print some of the network interface parameters
print('Connection successful')
print(station.ifconfig())

#Create a pin object
led = Pin(2, Pin.OUT)
