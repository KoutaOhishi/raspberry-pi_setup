
import RPi.GPIO as GPIO
import time

pin_No = 17


GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin_No, GPIO.OUT)


try:
	while True:
		print "ON"
		GPIO.output(pin_No, True)
		time.sleep(1)
		
		print "OFF"
		GPIO.output(pin_No, False)
		time.sleep(1)

		print "---"




except KeyboardInterrupt:
	print "Ctrl + c"
	GPIO.cleanup()
