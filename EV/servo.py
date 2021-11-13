import RPi.GPIO as GPIO
import time
import getcode as get
import requests

servo_pin = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo_pin, GPIO.OUT)

pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(12.0)

flag_exit = False

userInput = get.res
if userInput == "push":
	print(get.res)
	pwm_servo.ChangeDutyCycle(7.5)
	time.sleep(1.0)
	pwm_servo.ChangeDutyCycle(0.0)
	pwm_servo.ChangeDutyCycle(12.0) 
	time.sleep(1.5)
	pwm_servo.ChangeDutyCycle(0.0)url="http://203.253.128.161:7579/Mobius/cssrj/Turtlebot"

payload = "{\n    \"m2m:cin\": {\n        \"con\": \"go\"\n    }\n}"
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': '{{aei}}',
  'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
}

response = requests.request("POST", url, headers=headers, data=payload)
print

flag_exit = True
pwm_servo.stop()
GPIO.cleanup()
