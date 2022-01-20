#Opencv만을 활용한 주차장내에 차량 주차여부 확인 시스템
import cv2
import pickle


width , height = 10, 10
block_size=3
grey_weight=0 # Threshold 감도
isDragging=False
try:
    with open('CarParkPos','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]
    ß
def onMouse(event,x,y,flags,param):     # 마우스 이벤트 핸들 함수  ---①
    global isDragging, x0, y0, img      # 전역변수 참조
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 다운, 드래그 시작 ---②
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 움직임 ---③
        if isDragging:                  # 드래그 진행 중
            img_draw = img.copy()       # 사각형 그림 표현을 위한 이미지 복제
            cv2.rectangle(img_draw, (x0, y0), (x, y), (255,0,255), 2) # 드래그 진행 영역 표시
            cv2.imshow('img', img_draw) # 사각형 표시된 그림 화면 출력

    elif event == cv2.EVENT_LBUTTONUP:  # 왼쪽 마우스 버튼 업 ---④
        if isDragging:                  # 드래그 중지
            isDragging = False
            w = x - x0                  # 드래그 영역 폭 계산
            h = y - y0                  # 드래그 영역 높이 계산
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            if w > 0 and h > 0:         # 폭과 높이가 양수이면 드래그 방향이 옳음 ---⑤
                img_draw = img.copy()   # 선택 영역에 사각형 그림을 표시할 이미지 복제
                # 선택 영역에 빨간 사각형 표시
                cv2.rectangle(img_draw, (x0, y0), (x, y), (0,0,255), 2)
                posList.append((x0, y0, w, h))

            else:
                cv2.imshow('img', img)  # 드래그 방향이 잘못된 경우 사각형 그림ㅇㅣ 없는 원본 이미지 출력
                print("좌측 상단에서 우측 하단으로 영역을 드래그 하세요.")
    elif event == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1, y1, w, h = pos
            if x1<x<x1+w and y1<y<y1+h:
                posList.pop(i)
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

def img_Contrast(img): # -----Converting image to LAB Color model-----------------------------------
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) # -----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab) # -----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l) # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl, a, b)) # -----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final

def adjustGreyWeight(pos):
   global grey_weight
   grey_weight=pos

def adjustBlockSize(pos):
   global block_size
   block_size=pos*2

#비디오 사용시 주석헤제
#cap = cv2.VideoCapture('Anyang2_SKV1_cctv22.mp4') # <---------- 비디오 첨부
img_width, img_heiht=720,480 #변환하고자 하는 비디오 크기

cv2.namedWindow('imgThreshold')
cv2.createTrackbar('grey_weight', 'imgThreshold', 0, 30, adjustGreyWeight)
cv2.createTrackbar('blocksize', 'imgThreshold', 3, 15, adjustBlockSize)


while True:
    #이미지
    img = cv2.imread('388.png') # <------------------ 이미지 첨부

    #비디오 사용시 주석헤제
    #success, img = cap.read()
    # img = cv2.resize(img, dsize=(img_width, img_heiht))  # 이미지 사이즈 변환

    #img=img_Contrast(img) #색상 강조
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #그레이 스케일로 변환
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, grey_weight)

    for pos in posList:
        x, y, w, h =pos
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),1)
        cv2.rectangle(imgThreshold, (x,y), (x+ w, y + h), (255, 0, 255), 1)

    cv2.getTrackbarPos('grey_weight', 'imgThreshold')
    cv2.getTrackbarPos('blocksize', 'imgThreshold')

    cv2.imshow("image",img)
    cv2.imshow("imgThreshold", imgThreshold)
    cv2.setMouseCallback("image",onMouse)
    cv2.setMouseCallback("imgThreshold", onMouse)

    end_key=cv2.waitKey(1)
    if end_key == 27:
        print(posList)
        break
