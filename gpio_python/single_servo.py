import RPi.GPIO as GPIO
import time


def angle2duty(angle):
	return (1.0+angle/180.0)/20.0*100.0

pin_No = 17
hz = 100
sleep_time = 1

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin_No, GPIO.OUT)


servo = GPIO.PWM(pin_No, hz)


#initialize
servo.start(0.0)


try:
	while True:
		"""for angle in range(0, 210, 30):
			dc = angle2duty(angle)
			print "Angle:%s, Duty:%s"%(str(angle), str(dc))
			servo.ChangeDutyCycle(dc)
			time.sleep(sleep_time)"""
		dc = angle2duty(0)
		print "Angle:%s, Duty:%s"%(str(0), str(dc))
		servo.ChangeDutyCycle(dc)
		time.sleep(sleep_time)
		
		dc = angle2duty(360)			
		print "Angle:%s, Duty:%s"%(str(180), str(dc))
		servo.ChangeDutyCycle(dc)
		time.sleep(sleep_time)


except KeyboardInterrupt:
	print "Ctrl + c"
	servo.start(0.0)
	time.sleep(1)
	GPIO.cleanup()
