import cv2

def rotate(event,x,y,flags,param):
	global angulo, imagen_a_rotar

	if event == cv2.EVENT_LBUTTONDOWN:
		angulo = angulo + 15
		M = cv2.getRotationMatrix2D((ancho//2,alto//2), angulo, 1)
		imagen_a_rotar = cv2.warpAffine(imagen, M, (ancho,alto))

	if event == cv2.EVENT_RBUTTONDOWN:
		angulo = angulo - 15
		M = cv2.getRotationMatrix2D((ancho//2,alto//2), angulo, 1)
		imagen_a_rotar = cv2.warpAffine(imagen, M, (ancho,alto))

imagen = cv2.imread('ave.jpg')
imagen_a_rotar = imagen.copy() 
ancho = imagen.shape[1] # columnas
alto = imagen.shape[0]  # filas
angulo = 0
cv2.namedWindow('imagen_a_rotar')
cv2.setMouseCallback('imagen_a_rotar',rotate)

while True:
	#cv2.imshow('Imagen',imagen)
	cv2.imshow('imagen_a_rotar',imagen_a_rotar)
	print('Ángulo=',angulo)
	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()