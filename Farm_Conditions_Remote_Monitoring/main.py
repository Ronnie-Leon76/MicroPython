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
    html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
      crossorigin="anonymous"
    />
    <style>
        body {
            background-color: #f5f5f5;
        }
        h1 {
            text-align: center;
            margin-top: 10px;
        }
        
        .container {
            margin-top: 100px;
            margin-left:100px;
            align-items: center;
            justify-content: center;
        }
    </style>

    <title>Remote Farm Condition Monitoring System</title>
  </head>
  <body>
    <header>
      <h1 >Remote Farm Conditions Monitoring System</h1>
    </header>
    <main>
        <div class="container d-flex justify-container-center">
            <div class="row">
                <div class="col-md-12">
                   <div id="chart_div" style="width: 400px; height: 120px;"></div>
                </div>
            </div>
        </div>
    </main>
    <script
      src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"
      integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"
      integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF"
      crossorigin="anonymous"
    ></script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script>
        $(document).ready(function(){
    
            google.charts.load('current', {'packages':['gauge']});
              google.charts.setOnLoadCallback(drawChart);
        
              function drawChart() {
        
                var data = google.visualization.arrayToDataTable([
                  ['Label', 'Value'],
                  ['Temperature', 25],
                  ['Humidity', 55],
                  ['Moisture Content', 68]
                ]);
        
                var options = {
                  width: 400, height: 120,
                  redFrom: 90, redTo: 100,
                  yellowFrom:75, yellowTo: 90,
                  minorTicks: 5
                };
        
                var chart = new google.visualization.Gauge(document.getElementById('chart_div'));
        
                chart.draw(data, options);
        
                setInterval(function() {
                  data.setValue(0, 1, 40 + Math.round(60 * Math.random()));
                  chart.draw(data, options);
                }, 13000);
                setInterval(function() {
                  data.setValue(1, 1, 40 + Math.round(60 * Math.random()));
                  chart.draw(data, options);
                }, 5000);
                setInterval(function() {
                  data.setValue(2, 1, 60 + Math.round(20 * Math.random()));
                  chart.draw(data, options);
                }, 26000);
              }
            
        });
                                
    </script>
  </body>
</html>
"""
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
        dht_sensor.measure()
        temp_c = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp_c)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %' %hum)
        
        
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
        

