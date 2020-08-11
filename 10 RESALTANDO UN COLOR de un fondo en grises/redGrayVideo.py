import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture('video1.mp4')

rojoBajo1 = np.array([0, 140, 90], np.uint8)
rojoAlto1 = np.array([8, 255, 255], np.uint8)
rojoBajo2 = np.array([160, 140, 90], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

while True:

	ret, frame = cap.read()
	if ret == False: break
	frame = imutils.resize(frame,width=640)
	

	# Pasamos las imágenes de BGR a: GRAY (esta a BGR nuevamente) y a HSV
	frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frameGray = cv2.cvtColor(frameGray, cv2.COLOR_GRAY2BGR)
	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Detectamos el color rojo
	maskRojo1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
	maskRojo2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)
	mask = cv2.add(maskRojo1,maskRojo2)
	mask = cv2.medianBlur(mask, 7)
	redDetected = cv2.bitwise_and(frame,frame,mask=mask)

	# Fondo en grises
	invMask = cv2.bitwise_not(mask)
	bgGray = cv2.bitwise_and(frameGray,frameGray,mask=invMask)
	
	# Sumamos bgGray y redDetected
	finalframe = cv2.add(bgGray,redDetected)

	# Visualización
	cv2.imshow('Frame',frame)
	cv2.imshow('finalframe', finalframe)

	if cv2.waitKey(1) & 0xFF == 27:
		break

cap.release()
cv2.destroyAllWindows()