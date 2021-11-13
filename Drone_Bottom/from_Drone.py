# 아두이노 코드
# //홈페이지: www.daduino.co.kr
# //이메일: daduino@daduino.co.kr
 
# //2번핀에 전자석
# //모듈선연결: 흰색 S, 빨강 +, 검정 -
# //아두이노 선연결: 흰색 S, 빨강 +, 검정 -
 
 
# #define MAGNETIC_PIN 2
 
# void setup() {
#   pinMode(MAGNETIC_PIN,OUTPUT);//2번핀을 출력으로 설정한다
# }
 
# void loop() {
#   digitalWrite(MAGNETIC_PIN,HIGH); //2번핀에 연결된 전자석를 켠다
#   delay(1000); //1초 기다린다
#   digitalWrite(MAGNETIC_PIN,LOW); //2번핀에 연결된 전자석를 끈다
#   delay(1000); //1초 기다린다
# }

############################################

import RPi.GPIO as GPIO
import time
import requests
import to_Station

#definition of pin
EM= 2 #edit here. 전자석 연결하는 GPIO

delaytime = 1000
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

url = "http://203.253.128.161:7579/Mobius/cssrj/Drone_station/from_Drone/la"

payload={}
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SOrigin'
}
response = requests.request("GET", url, headers=headers, data=payload)

UserInput= response.text

# postman으로 드론 도착 시 'arrival'이라는 명령어 전송, 전자석 끄기
while(1):
    if UserInput == 'arrival':
        GPIO.setup(EM,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(delaytime)
        to_Station
    else:    
        GPIO.setup(EM,GPIO.OUT,initial=GPIO.HIGH)






