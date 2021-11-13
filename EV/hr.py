import RPi.GPIO as GPIO
import time

servo_pin = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo_pin, GPIO.OUT)

pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(7.5) 

flag_exit = False

try:
	while True:
		userInput = input()
		if userInput == "T": 
			pwm_servo.ChangeDutyCycle(3.0) 
			time.sleep(1.0)
			pwm_servo.ChangeDutyCycle(0.0)

			pwm_servo.ChangeDutyCycle(7.5) 
			time.sleep(1.5)
			pwm_servo.ChangeDutyCycle(0.0)

		if flag_exit:
			break

except KeyboardInterrupt:
	pass

flag_exit = True

pwm_servo.stop()
GPIO.cleanup()

