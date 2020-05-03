import cv2
import numpy as np

image = cv2.imread('ave.jpg')
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas

# Traslación
M = np.float32([[1,0,100],[0,1,150]])
imageOut = cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()