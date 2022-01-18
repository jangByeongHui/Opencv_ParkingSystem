#Opencv만을 활용한 주차장내에 차량 주차여부 확인 시스템
import cv2
import pickle


width , height = 12, 12

try:
    with open('CarParkPos','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]


def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1, y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open('CarParkPos','wb') as f:
        pickle.dump(posList,f)

#비디오 사용시 주석헤제
#cap = cv2.VideoCapture('Anyang2_SKV1_cctv22.mp4')
img_width, img_heiht=720,480 #변환하고자 하는 비디오 크기
while True:
    #이미지
    img = cv2.imread('388.png')
    #비디오 사용시 주석헤제
    #success, img = cap.read()
    #img = cv2.resize(img, dsize=(img_width, img_heiht))  # 이미지 사이즈 변환

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),1)
        cv2.rectangle(imgThreshold, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 1)

    cv2.imshow("image",img)
    cv2.imshow("imgThreshold", imgThreshold)
    cv2.setMouseCallback("image",mouseClick)
    cv2.setMouseCallback("imgThreshold", mouseClick)
    cv2.waitKey(1)
