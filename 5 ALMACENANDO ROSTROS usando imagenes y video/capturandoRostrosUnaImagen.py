import cv2

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

image = cv2.imread('imagen_000.jpg')
imageAux = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray, 1.1, 5)

count = 0

for (x,y,w,h) in faces:

	cv2.rectangle(image, (x,y),(x+w,y+h),(128,0,255),2)
	rostro = imageAux[y:y+h,x:x+w]
	rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite('rostro_{}.jpg'.format(count),rostro)
	count = count + 1

	cv2.imshow('rostro',rostro)
	cv2.imshow('image',image)
	cv2.waitKey(0)

cv2.destroyAllWindows()
