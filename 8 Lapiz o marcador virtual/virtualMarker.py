import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

celesteBajo = np.array([75, 185, 88], np.uint8)
celesteAlto = np.array([112, 255, 255], np.uint8)

# Colores para pintar
colorCeleste = (255,113,82)
colorAmarillo = (89,222,255)
colorRosa = (128,0,255)
colorVerde = (0,255,36)
colorLimpiarPantalla = (29,112,246) # Solo se usará para el cuadro superior de 'Limpiar Pantalla'

# Grosor de línea recuadros superior izquierda (color a dibujar)
grosorCeleste = 6
grosorAmarillo = 2
grosorRosa = 2
grosorVerde = 2

# Grosor de línea recuadros superior derecha (grosor del marcador para dibujar)
grosorPeque = 6
grosorMedio = 1
grosorGrande = 1

#--------------------- Variables para el marcador / lápiz virtual -------------------------
color = colorCeleste  # Color de entrada, y variable que asignará el color del marcador
grosor = 3 # Grosor que tendrá el marcador
#------------------------------------------------------------------------------------------

x1 = None
y1 = None
imAux = None

while True:

	ret,frame = cap.read()
	if ret==False: break

	frame = cv2.flip(frame,1)
	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	if imAux is None: imAux = np.zeros(frame.shape,dtype=np.uint8)

	#------------------------ Sección Superior ------------------------------------------
	# Cuadrados dibujados en la parte superior izquierda (representan el color a dibujar)
	cv2.rectangle(frame,(0,0),(50,50),colorAmarillo,grosorAmarillo)
	cv2.rectangle(frame,(50,0),(100,50),colorRosa,grosorRosa)
	cv2.rectangle(frame,(100,0),(150,50),colorVerde,grosorVerde)
	cv2.rectangle(frame,(150,0),(200,50),colorCeleste,grosorCeleste)

	# Rectángulo superior central, que nos ayudará a limpiar la pantalla
	cv2.rectangle(frame,(300,0),(400,50),colorLimpiarPantalla,1)
	cv2.putText(frame,'Limpiar',(320,20),6,0.6,colorLimpiarPantalla,1,cv2.LINE_AA)
	cv2.putText(frame,'pantalla',(320,40),6,0.6,colorLimpiarPantalla,1,cv2.LINE_AA)

	# Cuadrados dibujados en la parte superior derecha (grosor del marcador para dibujar)
	cv2.rectangle(frame,(490,0),(540,50),(0,0,0),grosorPeque)
	cv2.circle(frame,(515,25),3,(0,0,0),-1)
	cv2.rectangle(frame,(540,0),(590,50),(0,0,0),grosorMedio)
	cv2.circle(frame,(565,25),7,(0,0,0),-1)
	cv2.rectangle(frame,(590,0),(640,50),(0,0,0),grosorGrande)
	cv2.circle(frame,(615,25),11,(0,0,0),-1)
	#-----------------------------------------------------------------------------------
	
	# Detección del color celeste
	maskCeleste = cv2.inRange(frameHSV, celesteBajo, celesteAlto)
	maskCeleste = cv2.erode(maskCeleste,None,iterations = 1)
	maskCeleste = cv2.dilate(maskCeleste,None,iterations = 2)
	maskCeleste = cv2.medianBlur(maskCeleste, 13)
	cnts,_ = cv2.findContours(maskCeleste, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]

	for c in cnts:
		area = cv2.contourArea(c)
		if area > 1000:
			x,y2,w,h = cv2.boundingRect(c)
			x2 = x + w//2
			
			if x1 is not None:
				if 0 < x2 < 50 and 0 < y2 < 50:
					color = colorAmarillo # Color del lápiz/marcador virtual
					grosorAmarillo = 6
					grosorRosa = 2
					grosorVerde = 2
					grosorCeleste = 2
				if 50 < x2 < 100 and 0 < y2 < 50:
					color = colorRosa # Color del lápiz/marcador virtual
					grosorAmarillo = 2
					grosorRosa = 6
					grosorVerde = 2
					grosorCeleste = 2
				if 100 < x2 < 150 and 0 < y2 < 50:
					color = colorVerde # Color del lápiz/marcador virtual
					grosorAmarillo = 2
					grosorRosa = 2
					grosorVerde = 6
					grosorCeleste = 2
				if 150 < x2 < 200 and 0 < y2 < 50:
					color = colorCeleste # Color del lápiz/marcador virtual
					grosorAmarillo = 2
					grosorRosa = 2
					grosorVerde = 2
					grosorCeleste = 6
				if 490 < x2 < 540 and 0 < y2 < 50:
					grosor = 3 # Grosor del lápiz/marcador virtual
					grosorPeque = 6
					grosorMedio = 1
					grosorGrande = 1
				if 540 < x2 < 590 and 0 < y2 < 50:
					grosor = 7 # Grosor del lápiz/marcador virtual
					grosorPeque = 1
					grosorMedio = 6
					grosorGrande = 1
				if 590 < x2 < 640 and 0 < y2 < 50:
					grosor = 11 # Grosor del lápiz/marcador virtual
					grosorPeque = 1
					grosorMedio = 1
					grosorGrande = 6
				if 300 < x2 < 400 and 0 < y2 < 50:
					cv2.rectangle(frame,(300,0),(400,50),colorLimpiarPantalla,2)
					cv2.putText(frame,'Limpiar',(320,20),6,0.6,colorLimpiarPantalla,2,cv2.LINE_AA)
					cv2.putText(frame,'pantalla',(320,40),6,0.6,colorLimpiarPantalla,2,cv2.LINE_AA)
					imAux = np.zeros(frame.shape,dtype=np.uint8)
				if 0 < y2 < 60 or 0 < y1 < 60 :
					imAux = imAux
				else:
					imAux = cv2.line(imAux,(x1,y1),(x2,y2),color,grosor)
			cv2.circle(frame,(x2,y2),grosor,color,3)
			x1 = x2
			y1 = y2
		else:
			x1, y1 = None, None
	
	imAuxGray = cv2.cvtColor(imAux,cv2.COLOR_BGR2GRAY)
	_, th = cv2.threshold(imAuxGray,10,255,cv2.THRESH_BINARY)
	thInv = cv2.bitwise_not(th)
	frame = cv2.bitwise_and(frame,frame,mask=thInv)
	frame = cv2.add(frame,imAux)
	
	#cv2.imshow('maskCeleste', maskCeleste)
	cv2.imshow('imAux',imAux)
	cv2.imshow('frame', frame)
	
	k = cv2.waitKey(1)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()