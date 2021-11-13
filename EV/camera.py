# -*- coding: utf-8 -*-

import cv2
import sys

# WebCAM을 불러옴 (장치가 여러개 연결된 경우 인덱스는 0이 아닐 수도 있습니다)
vc = cv2.VideoCapture(-1)

while True:
    # WebCAM에서 이미지 읽어오기
    ret, frame = vc.read()
    # 위에서 읽어온 이미지를 "Video Window"이름을 가진 윈도우에서 보여줌
    cv2.imshow("Video Window", frame)

    # 키보드의 'q' 가 눌리면 while loop 빠져나가기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# WebCAM 리소스를 해제
vc.release()
# 열린 모든 윈도우 닫기
cv2.destroyAllWindows()
