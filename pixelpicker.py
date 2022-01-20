from telnetlib import STATUS
from tkinter import Frame
import cv2 as cv    # OpenCV import
import numpy as np  # 행렬(img)를 만들기 위한 np import

# 마우스 이벤트 콜백함수 정의
def mouse_callback(event, x, y, flags, param): 
    if event == cv.EVENT_LBUTTONDOWN:
        print("마우스 이벤트 발생, x:", x ," y:", y) # 이벤트 발생한 마우스 위치 출력

img = cv.imread('image.jpg')  # 행렬 생성, (가로, 세로, 채널(rgb)),bit)


cv.namedWindow('image')  #마우스 이벤트 영역 윈도우 생성
cv.setMouseCallback('image', mouse_callback)

while(True):
    
    cv.imshow('image',img)
    k = cv.waitKey(1) 
    if k == 27:    # ESC 키 눌러졌을 경우 종료
        print("ESC 키 눌러짐")
        break
cv.destroyAllWindows()