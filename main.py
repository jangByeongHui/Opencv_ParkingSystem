import cv2
import pickle

import cvzone
import numpy as np

#Video feed
cap = cv2.VideoCapture('Anyang2_SKV1_cctv22.mp4')
with open('CarParkPos','rb') as f:
    posList = pickle.load(f)

img_width,img_heiht = 720,480

def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x,y ,w,h=pos
        imgCrop = imgPro[y:y+h,x:x+w]
        cv2.imshow("imgCrroped{}{}".format(x,y),imgCrop) #우리가 확인하는 영역에 부분만 view

        count =cv2.countNonZero(imgCrop) #특정 영역에 보이는 0이 아닌 픽셀 수
        cvzone.putTextRect(img, str(count), (x, y + h - 5), scale=0.5, thickness=1, offset=0) #검출 되는 픽셀 수 표시

        #검출 되는 픽셀 수에 따라 영역 색상 표시 변경

        #차량 주차면 주차
        if count < 500:
            color=(0,255,0)
            thickness=1
            spaceCounter += 1
        #빈 주차면
        else:
            color=(0,0,255)
            thickness = 1

        cv2.rectangle(img, pos, (pos[0] + w, pos[1] + h), color, thickness)

    cvzone.putTextRect(img,"FULL:{}".format(spaceCounter),(50,25),scale=0.5,thickness=1,offset=15,colorR=(0,255,0)) # 빈공간 표시


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.cv2.CAP_PROP_POS_FRAMES,0)
    success, img = cap.read()

    img = cv2.resize(img,dsize=(img_width,img_heiht)) # 이미지 사이즈 변환

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,19,17)


    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.int8)
    imgDilate = cv2.dilate(imgMedian,kernel,iterations=1)

    checkParkingSpace(imgDilate)

    cv2.imshow("Image",img)
    cv2.imshow("ImageBlur",imgBlur)
    cv2.imshow("imgMedian", imgMedian)
    cv2.waitKey(10)
