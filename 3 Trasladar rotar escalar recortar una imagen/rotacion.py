import cv2
import numpy as np

image = cv2.imread('ave.jpg')
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas

# Rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),15,1)
imageOut = cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()