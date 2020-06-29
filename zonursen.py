from threading import Thread
import io
import socket
import struct
import time
import picamera
import RPi.GPIO as GPIO
from time import sleep

ileri = 23
geri = 24
sag = 17
sol = 4
en = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(ileri, GPIO.OUT)
GPIO.setup(geri, GPIO.OUT)
GPIO.setup(sag, GPIO.OUT)
GPIO.setup(sol, GPIO.OUT)
GPIO.output(ileri, GPIO.LOW)
GPIO.output(geri, GPIO.LOW)
GPIO.output(sag, GPIO.LOW)
GPIO.output(sol, GPIO.LOW)



HOST = ''
PORT = 6001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

def kameraGonder(arg):
	client_socket = socket.socket()
	client_socket.connect(('192.168.1.103', 8001))  # ADD IP HERE
	connection = client_socket.makefile('wb')
	try:
		camera = picamera.PiCamera()
	    	camera.vflip = True
	    	camera.resolution = (500, 480)
	    	camera.start_preview()
	    	time.sleep(2)
	    	start = time.time()
	    	stream = io.BytesIO()
	    	for foo in camera.capture_continuous(stream, 'jpeg'):
			connection.write(struct.pack('<L', stream.tell()))
	        	connection.flush()
	        	stream.seek(0)
	        	connection.write(stream.read())
	        	if time.time() - start > 60:
	        		break
	        	stream.seek(0)
	        	stream.truncate()
	    	connection.write(struct.pack('<L', 0))
	except:
		pass
        #finally:
	#	connection.close()
	#	client_socket.close()


threadDeneme = Thread(target = kameraGonder, args = (10, ))
while True:
	print("Server is running")
	data, addr = sock.recvfrom(1024)
	print("received message: ", data,addr)
	if data == "KameraAc":
		print("Kamera calistiriliyor...")
		try:
			threadDeneme.start()
		except Exception as err:
			print("An error", err)
	if data == "Ileri":
		GPIO.output(ileri, GPIO.HIGH)
		sleep(1)
		GPIO.output(ileri, GPIO.LOW)

	if data == "Geri":
		GPIO.output(geri, GPIO.HIGH)
		sleep(1)
		GPIO.output(geri, GPIO.LOW)

	if data == "Sag":
		GPIO.output(sag, GPIO.HIGH)
		sleep(1)
		GPIO.output(sag, GPIO.LOW)

	if data == "Sol":
		GPIO.output(sol, GPIO.HIGH)
		sleep(1)
		GPIO.output(sol, GPIO.LOW)


