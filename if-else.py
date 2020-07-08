import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO,setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(21,GPIO.IN)
while 1:
	if GPIO.input(21):
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(17,GPIO.LOW)
	else:
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(18,GPIO.LOW)
	time.sleep(0.1)
