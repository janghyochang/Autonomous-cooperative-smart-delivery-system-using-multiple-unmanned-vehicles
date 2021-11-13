import cv2
import numpy as np


cap = cv2.VideoCapture(-1)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.inRange(hsv_frame, (50, 150, 0), (80, 255, 255))
    print(dst)
    cv2.imshow("Frame", frame)
    cv2.imshow("dst",dst)



    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
