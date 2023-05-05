import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)

try:
	print("PIR MODULE TEST (CTRL+C TO EXIT)")
	time.sleep(2)
	print("ready")
	while True:
		if GPIO.input(PIR_PIN):
			print("Motion Detected!")
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
