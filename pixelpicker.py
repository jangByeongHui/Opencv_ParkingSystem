import cv2 as cv    # OpenCV import

pos_list_CCTV=[]
pos_list_MAP=[]
#비교할 이미지 두장
CCTV = cv.imread('/Users/jangbyeonghui/Desktop/opevcv_cardetect/results/cctv21_HD.png')  # 행렬 생성, (가로, 세로, 채널(rgb)),bit)
MAP = cv.imread('Anyang2_SKV1_B3.png')  # 행렬 생성, (가로, 세로, 채널(rgb)),bit)

# 마우스 이벤트 콜백함수 정의
def mouse_callback_CCTV(event, x, y, flags, param):
    global CCTV
    if event == cv.EVENT_LBUTTONDOWN:
        pos_list_CCTV.append([x,y])
        print("CCTV, x:", x ," y:", y) # 이벤트 발생한 마우스 위치 출력
    elif event == cv.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pos_list_CCTV):
            x1,y1=pos
            w,h=12,12
            if x1-w < x < x1 + w and y1 -h< y < y1 + h:
                pos_list_CCTV.pop(i)
                CCTV = cv.imread('/Users/jangbyeonghui/Desktop/opevcv_cardetect/results/cctv21_HD.png')

def mouse_callback_MAP(event, x, y, flags, param):
    global MAP
    if event == cv.EVENT_LBUTTONDOWN:
        pos_list_MAP.append([x,y])
        print("MAP, x:", x ," y:", y) # 이벤트 발생한 마우스 위치 출력
    elif event == cv.EVENT_RBUTTONDOWN:
        print("remove : x:{} y:{}".format(x,y))
        for i, pos in enumerate(pos_list_MAP):
            x1, y1= pos
            w,h=20,20
            if x1-w < x < x1 + w and y1 -h < y < y1 + h:
                pos_list_MAP.pop(i)
                MAP = cv.imread('Anyang2_SKV1_B3.png')




cv.namedWindow('CCTV')  #마우스 이벤트 영역 윈도우 생성
cv.setMouseCallback('CCTV', mouse_callback_CCTV)

cv.namedWindow('MAP')  #마우스 이벤트 영역 윈도우 생성
cv.setMouseCallback('MAP', mouse_callback_MAP)

while(True):

    for i in pos_list_CCTV:
        cv.circle(CCTV,i,12,(0,0,255),-1)

    for i in pos_list_MAP:
        cv.circle(MAP,i,12,(0,0,255),-1)

        #cvzone.putTextRect(img, str(count), (x, y + h - 5), scale=0.5, thickness=1, offset=0)  # 검출 되는 픽셀 수 표시
    
    cv.imshow('CCTV',CCTV)
    cv.imshow('MAP', MAP)

    k = cv.waitKey(1) 
    if k == 27:    # ESC 키 눌러졌을 경우 종료
        print("CCTV 저장 좌표")
        print(pos_list_CCTV)
        print()
        print("MAP 저장 좌표")
        print(pos_list_MAP)
        print("ESC 키 눌러짐")
        break

cv.destroyAllWindows()