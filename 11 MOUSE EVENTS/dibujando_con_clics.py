import cv2
import numpy as np

def dibujando(event,x,y,flags,param):
	# Imprimimos la información sobre los eventos que se estén realizando
	print('-----------------------------')
	print('event=',event)
	print('x=',x)
	print('y=',y)
	print('flags=',flags)

	# Ejemplos de acciones con algunos eventos del mouse
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(imagen,(x,y),20,(255,255,255),2)

	if event == cv2.EVENT_RBUTTONDOWN:
		cv2.circle(imagen,(x,y),20,(0,0,255),2)

	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(imagen,(x,y),10,(255,0,0),-1)

	if event == cv2.EVENT_RBUTTONDBLCLK:
		cv2.circle(imagen,(x,y),10,(0,255,0),-1)

	if event == cv2.EVENT_LBUTTONUP:
		cv2.putText(imagen,'Ha dejado de presionar (Izquierdo)',(x,y),2,0.4,(255,255,0),1,cv2.LINE_AA)

	if event == cv2.EVENT_RBUTTONUP:
		cv2.putText(imagen,'Ha dejado de presionar (Derecho)',(x,y),2,0.4,(0,255,255),1,cv2.LINE_AA)

imagen = np.zeros((480,640,3),np.uint8)
cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen',dibujando)

while True:
	cv2.imshow('Imagen',imagen)
	
	k = cv2.waitKey(1) & 0xFF
	if k == ord('l'): # Limpiar el contenido de la imagen
		imagen = np.zeros((480,640,3),np.uint8)
	elif k == 27:
		break

cv2.destroyAllWindows()