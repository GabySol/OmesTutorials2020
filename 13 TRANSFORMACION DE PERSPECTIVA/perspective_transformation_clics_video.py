import cv2
import numpy as np

def clics(event,x,y,flags,param):
	global puntos
	if event == cv2.EVENT_LBUTTONDOWN:
		puntos.append([x,y])

def dibujando_puntos(puntos):
	for x, y in puntos:
		cv2.circle(frame,(x,y),5,(0,255,0),2)

def uniendo4puntos(puntos):
	cv2.line(frame,tuple(puntos[0]),tuple(puntos[1]),(255,0,0),1)
	cv2.line(frame,tuple(puntos[0]),tuple(puntos[2]),(255,0,0),1)
	cv2.line(frame,tuple(puntos[2]),tuple(puntos[3]),(255,0,0),1)
	cv2.line(frame,tuple(puntos[1]),tuple(puntos[3]),(255,0,0),1)

puntos = []
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video1.mp4')
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',clics)

while True:
	ret, frame = cap.read()
	if ret == False: break
	dibujando_puntos(puntos)

	if len(puntos) == 4:
		uniendo4puntos(puntos)
		pts1 = np.float32([puntos])
		pts2 = np.float32([[0,0], [500,0], [0,300], [500,300]])

		M = cv2.getPerspectiveTransform(pts1,pts2)
		dst = cv2.warpPerspective(frame, M, (500,300))

		cv2.imshow('dst', dst)
	cv2.imshow('frame',frame)
	
	k = cv2.waitKey(1) & 0xFF
	if k == ord('n'): # Limpiar el contenido de la frame
		puntos = []
		
	elif k == 27:
		break
cap.release()
cv2.destroyAllWindows()