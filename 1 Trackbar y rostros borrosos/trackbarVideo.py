import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cv2.namedWindow('frame')
cv2.createTrackbar('Blur','frame',0,15,nothing)
cv2.createTrackbar('Gray','frame',0,1,nothing)

while True:    
    ret,frame = cap.read()    
    val = cv2.getTrackbarPos('Blur','frame')
    grayVal = cv2.getTrackbarPos('Gray','frame')
    if grayVal == 1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceClassif.detectMultiScale(frame, 1.3, 5)

    for (x,y,w,h) in faces:
        if val > 0: 
            frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],(val,val))
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()