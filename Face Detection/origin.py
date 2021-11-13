import cv2
import sys
# from PIL import Image

import numpy as np
import os
import base64


# import sys

import io
from PIL import Image
cascade_file = "haarcascade_frontalface_default.xml"

#만약 dataset이라는 폴더 못찾으면 만들도록 설정
path_data = 'dataset'
if path_data not in os.listdir():
    os.mkdir(path_data)


def cropImage(path, cnt):
    num = 1
    files = os.listdir(path)
    # path에 있는 파일들에 대해서 얼굴 인식해서 크롭 후 dataset폴더에 저장하는 과정 수행
    for file in files:
        img = cv2.imread(os.path.join(path, file))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cascade_file)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
            cv2.imwrite("dataset/User." + str(cnt) + '.' + str(num) + ".jpg", cropped)
            num += 1



def decode_img(msg):
    msg = msg[msg.find(b"<plain_txt_msg:img>")+len(b"<plain_txt_msg:img>"):
            msg.find(b"<!plain_txt_msg>")]
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    img = Image.open(buf)
    return img


#path ='../nCube-Thyme-Nodejs-master/note.txt'
path = '/home/pi/Desktop/Documents/nCube-Thyme-Nodejs-master/note2.txt'
f = open(path,'rb')
#fileread = f.read()+b"<!plain_txt_msg>"
fileread = f.read()
print(fileread)
decoding_img = decode_img(fileread)
print(decode_img)

resize=decoding_img.resize((720,720))
resize.save('./decodinpi    g2.jpg')
f.close()

cnt=1

#dataset 폴더에 있는 이미지들로 학습 수행
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cascade_file)

# 이미지랑 label 데이터 얻기
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

#print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path_data)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
#print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

cv2.waitKey(0)
cv2.destroyAllWindows()