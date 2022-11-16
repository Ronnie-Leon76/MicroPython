from machine import Pin, ADC
from time import sleep
import dht

# will change to the Analog Pin Connected
analogue_pin = None
moisture_sensor_pin = ADC(Pin(analogue_pin))

# will change to the GPIO pin connected to DHT
dht_pin = None

dht_sensor = dht.DHT11(Pin(dht_pin))


# read voltage in full range by setting the attenuation ratio to 11db
moisture_sensor_pin.atten(ADC.ATTN_11DB)

while True:
    try:
        moisture_value = moisture_sensor_pin.read()
        print(moisture_value)
        sleep(2)
        moisture_sensor_pin.measure()
        temp = moisture_sensor_pin.temperature()
        hum = moisture_sensor_pin.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)
    except OSError as e:
        print('Failed to read from the sensors.')
        
def web_page():
    html = """"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
    



