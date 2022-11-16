"""
Pivot Club KU: Hardware Cohort
Farm Conditions Remote System using ESP32, Soil Moisture Sensor & DHT11
Author: Ronnie Leon

"""



from machine import Pin, ADC
from time import sleep
import dht

SOIL_WET = 500
SOIL_DRY = 750

# will change to the Analog Pin Connected
analogue_pin = None
moisture_sensor_pin = ADC(Pin(analogue_pin))

# read voltage in full range by setting the attenuation ratio to 11db
moisture_sensor_pin.atten(ADC.ATTN_11DB)

# will change to the GPIO pin connected to DHT
dht_pin = None

dht_sensor = dht.DHT11(Pin(dht_pin))





def web_page(temp_c, temp_f, humid, moisture_status):
    html = """"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


while True:
    try:
        moisture_level = ""
        moisture_value = moisture_sensor_pin.read()
        if moisture_value < SOIL_WET:
            print("Status: Soil is too wet")
            moisture_level = "Too Wet"
        elif moisture_value >= SOIL_WET and moisture_value < SOIL_DRY:
            print("Status: Soil moisture is perfect")
            moisture_level = "Perfect soil moisture"
        elif moisture_value >= SOIL_DRY:
            moisture_level = "Too Dry"
            print("Status: Soil is too dry - time to water!")
        sleep(2)
        moisture_sensor_pin.measure()
        temp_c = moisture_sensor_pin.temperature()
        hum = moisture_sensor_pin.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp_c)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)
        
        
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        response = web_page(temp_c, temp_f, hum, moisture_level)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    





    except OSError as e:
        print('Failed to read from the sensors.')
        

