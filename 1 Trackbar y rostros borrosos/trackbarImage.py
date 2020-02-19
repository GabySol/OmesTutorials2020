import cv2

def nothing(x):
    pass

image = cv2.imread('oficina2.jpg')
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cv2.namedWindow('Imagen')
cv2.createTrackbar('Blur','Imagen',0,15,nothing)
cv2.createTrackbar('Gray','Imagen',0,1,nothing)

while True:

    val = cv2.getTrackbarPos('Blur','Imagen')
    grayVal = cv2.getTrackbarPos('Gray','Imagen')
    if grayVal == 1:
        imageN = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    else: imageN = image.copy()
    faces = faceClassif.detectMultiScale(image, 1.1, 5)

    for (x,y,w,h) in faces:
        if val > 0:
            imageN[y:y+h,x:x+w] = cv2.blur(imageN[y:y+h,x:x+w],(val,val))

    cv2.imshow('Imagen',imageN)
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()