import cv2

# cap= cv2.VideoCapture(0)
#카메라 오픈

cap = cv2.VideoCapture(0)
#가로길이를 get함수를 써서 반환

while True:
    cap.read()
    #1 프레임을 읽고 반환, 반환인자는 ret,frame
    ret, frame = cap.read()
    #return 되었는지 bool 자료,
    if not ret: #return이 false면 나가라
        break

    edge = cv2.Canny(frame,50,150)
    ## porcessing
    cv2.imshow('frame',frame)
    cv2.imshow('edge',edge)
    ##window의 이름이 frame, frame 변수를 띄우겠다.
    if cv2.waitKey(15) == 27: #27은 아스키코드 esc
    #키 입력을 기다리는 함수, 30은 인자 밀리세컨드 = 0.03초 동안만 재생, 그리고 꺼짐 => 30이면 33hz
    #1000 => 1초마다 한장씩

        break
    #키를 누르면 종료
cap.release()
cv2.destroyAllWindows()