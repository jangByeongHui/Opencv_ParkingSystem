# Opencv_ParkingSystem

차량 주차 상태 확인을 위해서 영상 혹은 이미지를 gray scale로 변환하여 특정 영역 내에 있는 픽셀 수를 통해서 차량 주차 상태를 확인하는 시스템이다.
기존 yolov5를 통해서 주차 상태를 확인하고자 하였을 경우 이면 주차 등의 문제로 인하여 차량의 형태를 파악하지 못하면 차량을 인식하는 문제가 발생하였다.
그러나 주차장 같은 경우 주차면의 주로 차량만이 주차되어 있다는 가정하에 픽셀 수만으로 차량이라고 판단 할 수 있을 것이라고 판단하였다. 그래서 특정 영역만 픽셀 수를 잡으면
머신러닝을 사용하지 않고도 빠른 시간 내에 주차면의 차량을 인식할 수 있을 것이다.

## ParkingSpacePicker

검출하고자 하는 CCTV 혹은 장소 영상이나 이미지에서 픽셀 수를 검출하고자 하는 영역을 표시하는 것이다. width나 height 값을 조절하여 bounding 영역을 표시할 수 있다.
이 때 마우스 왼쪽 버튼을 클릭시 설정한 크기의 영역이 잡히고 오른쪽 버튼을 선택시 영역이 해제된다. 잡은 영역의 좌표들은 CarParkPos에 저장되어 자동으로 main.py에서 설정한 좌표값을 사용할 수 있도록 하였다.

<img src="https://github.com/jangByeongHui/Opencv_ParkingSystem/blob/main/img/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-01-18%20%EC%98%A4%EC%A0%84%2010.55.36.png?raw=true">

## main,py

ParkingSpacePicker를 통해서 저장한 좌표 값들을 이용하여 해당 영역들의 픽셀을 잡고 설정한 픽셀 수 만큼 검출하게 되면 색상이 변화하여 차량이 주차중이거나 빈 주차면인 상황을 표시한다.

<img src="https://github.com/jangByeongHui/Opencv_ParkingSystem/blob/main/img/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-01-18%20%EC%98%A4%EC%A0%84%2011.09.02.png?raw=true">

## 사용 방법

1. ParkingSpacePicker

```

git clone https://github.com/jangByeongHui/Opencv_ParkingSystem.git
cd Opencv_ParkingSystem
//소스코드 내부안에서 검출한 이미지나 영상 자료 , 검출 영역 크기 설정

python ParkingSpacePicker.py //실행

//마우스 클릭으로 영역 표시 후 종료
//선택한 좌표들은 CarParkPos에 자동 저장

```

2. main.py

```
cd Opencv_ParkingSystem

//검출할 이미지나 영상 정보 입력후
python main.py //실행

```
