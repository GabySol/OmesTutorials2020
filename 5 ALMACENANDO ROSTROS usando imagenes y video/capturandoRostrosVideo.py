import cv2
import os

if not os.path.exists('Rostros encontrados'):
	print('Carpeta creada: Rostros encontrados')
	os.makedirs('Rostros encontrados')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

count = 0
while True:
	ret,frame = cap.read()
	frame = cv2.flip(frame,1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray, 1.3, 5)

	k = cv2.waitKey(1)
	if k == 27:
		break

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(128,0,255),2)
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
		if k == ord('s'):
			cv2.imwrite('Rostros encontrados/rostro_{}.jpg'.format(count),rostro)
			cv2.imshow('rostro',rostro)
			count = count +1
	cv2.rectangle(frame,(10,5),(450,25),(255,255,255),-1)
	cv2.putText(frame,'Presione s, para almacenar los rostros encontrados',(10,20), 2, 0.5,(128,0,255),1,cv2.LINE_AA)
	cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()