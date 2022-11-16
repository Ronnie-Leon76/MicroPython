from hcsr04 import HCSR04
from dcmotor import DCMotor 
from time import sleep
from machine import Pin, PWM
try:
  import usocket as socket
except:
  import socket


# frequency at which the driver operates at
frequency = 15000       
pin1 = Pin(16, Pin.OUT)    
pin2 = Pin(17, Pin.OUT)
pin3 = Pin(19, Pin.OUT)    
pin4 = Pin(21, Pin.OUT)

enable_left = PWM(Pin(13), frequency)
enable_right = PWM(Pin(12), frequency)
     
dc_motor_left = DCMotor(pin1, pin2, enable_left, 750, 1023)     
dc_motor_right = DCMotor(pin3, pin4, enable_right, 750, 1023)


"""
Function that returns a variable called html
that contains the HTML text to build the the web page.
The web page displays the current GPIO state, before generating the HTML text.
The GPIO state is incoporated into the HTML text using "+" to concatenate strings
"""
def web_page():
  if led.value() == 1:
    gpio_state="FOWARD"
  else:
    gpio_state="BACKWARD"
  
  html = """<html><head> <title>Tesla Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}.button3{background-color: #8B0000;}</style></head><body> <h1>Tesla Web Server </h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?forward=true"><button class="button">Forward</button></a></p>
  <p><a href="/?reverse=true"><button class="button button2">Reverse</button></a></p><p><a href="/?stop=true"><button class="button button3">Stop</button></a></p></body></html>"""
  return html

#Creating a socket and specifying the socket type. This is a stream tcp socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('got here')
#Bind the socket to an address(network interface and port number)
try:
    s.bind(('192.168.43.250',80))
except OSError:
    print('got an existing socket')

#Enables the server to accept connections ( a listening socket)
s.listen(5)

"""
In the while loop we :
Listen for requests and send responses
When a client connects , server calls the accept() method to accept the connections.
When the client connects, it saves a new socket object to accept and send data on the conn variable
and saves the client address to connect to the server on the addr variable.
"""
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  forward= request.find('/?forward=true')
  reverse = request.find('/?reverse=true')
  stop= request.find('/?stop=true')
  
  if forward == 6:
        print('LED ON')
        dc_motor_left.forward(10)
        dc_motor_right.forward(10)
        led.value(1)
  if reverse == 6:
        print('LED OFF')
        dc_motor_left.backwards(10)
        dc_motor_right.backwards(10)
        led.value(0)
  if stop==6:
        dc_motor_left.stop()
        dc_motor_right.stop()
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

