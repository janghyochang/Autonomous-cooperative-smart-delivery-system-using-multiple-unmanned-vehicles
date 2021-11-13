#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import requests

#Definition of  motor pin 
IN1 = 20
IN2 = 21
#IN3 = 19
#IN4 = 26
ENA = 16
ENB = 13

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pin initialization operation
def motor_init():
    global pwm_ENA
    global pwm_ENB
    global delaytime
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    #GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    #GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)


motor_init()

# 드론 도착 시 'Open_Station'이라는 명령어를 받아오면 모터 돌아가게 하기
while(1):
  url = "http://203.253.128.161:7579/Mobius/cssrj/Drone_station/to_Station/la"

  payload={}
  headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SOrigin'}
  response = requests.request("GET", url, headers=headers, data=payload)
  new_json=response.json()
  res=new_json["m2m:cin"]['con']
  if res == 'Open Station':
    print('Open Station')
    GPIO.output(IN1,GPIO.HIGH) #모터 돌아가기
    GPIO.output(IN2,GPIO.HIGH)
        
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(1000)
  else:    
    print(res)

pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup() 

