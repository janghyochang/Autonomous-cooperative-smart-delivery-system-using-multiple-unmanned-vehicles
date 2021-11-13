import cv2
import numpy as np
import time
import requests

cap = cv2.VideoCapture(-1)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red color
        
   # low_red = np.array([161, 155, 84])
   # high_red = np.array([179, 255, 255])
   # red_mask = cv2.inRange(hsv_frame, low_red, high_red)
   # red = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Blue color
   # low_blue = np.array([94, 80, 2])
   # high_blue = np.array([126, 255, 255])
   # blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
   # blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    # print(green[0][0][1])
    
    img_height, img_width ,_=hsv_frame.shape

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)

#    cv2.imshow("Red", red)
#    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
#    cv2.imshow("Result", result)
    for i in range(img_height):
        for j in range(img_width):
            if (green_mask[i].sum()) > 0:
            #if (hsv_frame[i][j][1]>=low_green).all() and (hsv_frame[i][j][1]<=high_green).all():
                print("stop")
                
                url="http://203.253.128.161:7579/Mobius/cssrj/Turtlebot"

                payload = "{\n    \"m2m:cin\": {\n        \"con\": \"stop\"\n    }\n}"
                headers = {
                'Accept': 'application/json',
                'X-M2M-RI': '12345',
                'X-M2M-Origin': '{{aei}}',
                'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                print
                
                #print(green)
                print(green_mask[i].sum())
                break
            
            else:
                print("go")
                
                url="http://203.253.128.161:7579/Mobius/cssrj/Turtlebot"

                payload = "{\n    \"m2m:cin\": {\n        \"con\": \"go\"\n    }\n}"
                headers = {
                'Accept': 'application/json',
                'X-M2M-RI': '12345',
                'X-M2M-Origin': '{{aei}}',
                'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                print
                
                # print(green_mask[i])
                print(green_mask[i].sum())
                
                break
            break
        break


    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
