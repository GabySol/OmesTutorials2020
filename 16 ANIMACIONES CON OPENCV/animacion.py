import cv2
import numpy as np

salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*"MJPG"),30,(1280,720))

imagen = 255*np.ones(shape=(720,1280,3),dtype=np.uint8)

cinco = cv2.imread('cinco.png')
filas_cinco = cinco.shape[0]
col_cinco = cinco.shape[1]

cero = cv2.imread('cero.png')
filas_cero = cero.shape[0]
col_cero = cero.shape[1]

suscriptores = cv2.imread('suscriptores.png')
filas_suscriptores = suscriptores.shape[0]
col_suscriptores = suscriptores.shape[1]

corazon = cv2.imread('corazon.png')
filas_corazon = corazon.shape[0]
col_corazon = corazon.shape[1]

#----- Visualiza 5000 (bajan desde la parte superior) -----
for i in np.arange(0,150,4):
	n_imagen1 = imagen.copy()
	n_imagen1[i:i+filas_cinco,320:320+col_cinco] = cinco
	salida.write(n_imagen1)
	cv2.imshow('Imagen',n_imagen1)
	cv2.waitKey(10)

for i in np.arange(0,140,4):
	n_imagen2 = n_imagen1.copy()
	n_imagen2[i:i+filas_cero,480:480+col_cero] = cero
	salida.write(n_imagen2)
	cv2.imshow('Imagen',n_imagen2)
	cv2.waitKey(10)

for i in np.arange(0,140,4):
	n_imagen3 = n_imagen2.copy()
	n_imagen3[i:i+filas_cero,635:635+col_cero] = cero
	salida.write(n_imagen3)
	cv2.imshow('Imagen',n_imagen3)
	cv2.waitKey(10)

for i in np.arange(0,140,4):
	n_imagen4 = n_imagen3.copy()
	n_imagen4[i:i+filas_cero,790:790+col_cero] = cero
	salida.write(n_imagen4)
	cv2.imshow('Imagen',n_imagen4)
	cv2.waitKey(10)

#----- Visualiza ¡Suscriptores! (Aparece poco a poco) -----
for i in np.arange(0.3,1,0.03):
	crop_n_imagen4 = n_imagen4[428:428 + filas_suscriptores, 260:260 + col_suscriptores]
	n_imagen4[428:428 + filas_suscriptores, 260:260 + col_suscriptores] = cv2.addWeighted(suscriptores,i,crop_n_imagen4,0.9,0)
	salida.write(n_imagen4)
	cv2.imshow("Imagen",n_imagen4)
	cv2.waitKey(10)

#----- Visualiza el corazón (Latidos en encendido y apagado) -----
j = 0
for i in range(200):
	n_imagen5 = n_imagen4.copy()
	if j <= 10:
		n_imagen5[440:440+filas_corazon,865:865+col_corazon] = corazon
	if j > 20:
		j = 0
	j = j + 1

	salida.write(n_imagen5)
	cv2.imshow('Imagen',n_imagen5)
	cv2.waitKey(10)

salida.release()
cv2.waitKey(0)
cv2.destroyAllWindows()