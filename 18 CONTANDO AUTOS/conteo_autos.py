import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture('autos.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
car_counter = 0

while True:

	ret, frame = cap.read()
	if ret == False: break
	frame = imutils.resize(frame, width=640)

	# Especificamos los puntos extremos del área a analizar
	area_pts = np.array([[330, 216], [frame.shape[1]-80, 216], [frame.shape[1]-80, 271], [330, 271]])

	# Con ayuda de una imagen auxiliar, determinamos el área
	# sobre la cual actuará el detector de movimiento
	imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
	imAux = cv2.drawContours(imAux, [area_pts], -1, (255), -1)
	image_area = cv2.bitwise_and(frame, frame, mask=imAux)	

	# Obtendremos la imagen binaria donde la región en blanco representa
	# la existencia de movimiento
	fgmask = fgbg.apply(image_area)
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
	fgmask = cv2.dilate(fgmask, None, iterations=5)

	# Encontramos los contornos presentes de fgmask, para luego basándonos
	# en su área poder determinar si existe movimiento (autos)
	cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

	for cnt in cnts:
		if cv2.contourArea(cnt) > 1500:
			x, y, w, h = cv2.boundingRect(cnt)
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 1)
			
			# Si el auto ha cruzado entre 440 y 460 abierto, se incrementará
			# en 1 el contador de autos
			if 440 < (x + w) < 460:
				car_counter = car_counter + 1
				cv2.line(frame, (450, 216), (450, 271), (0, 255, 0), 3)
				
	# Visualización del conteo de autos
	cv2.drawContours(frame, [area_pts], -1, (255, 0, 255), 2)
	cv2.line(frame, (450, 216), (450, 271), (0, 255, 255), 1)
	cv2.rectangle(frame, (frame.shape[1]-70, 215), (frame.shape[1]-5, 270), (0, 255, 0), 2)
	cv2.putText(frame, str(car_counter), (frame.shape[1]-55, 250),
				cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)
	cv2.imshow('frame', frame)

	k = cv2.waitKey(70) & 0xFF
	if k ==27:
		break

cap.release()
cv2.destroyAllWindows()