import cv2
import imutils 

imagen1 = cv2.imread('imagen_01.jpeg')
imagen2 = cv2.imread('imagen_02.jpeg')
imagen3 = cv2.imread('ave.jpg')

# Dimensiones de las imágenes leídas
print('imagen1.shape = ', imagen1.shape)
print('imagen2.shape = ', imagen2.shape)
print('imagen3.shape = ', imagen3.shape)

# Concatenando 2 imágenes vertical y horizontalmente
concat_horizontal = cv2.hconcat([imagen1, imagen2])
concat_vertical = cv2.vconcat([imagen1, imagen2])
cv2.imshow('concat_horizontal', concat_horizontal)
cv2.imshow('concat_vertical', concat_vertical)

# Concatenando imágenes, 2 filas por 4 columnas
concat_h1 = cv2.hconcat([imagen1, imagen2, imagen1, imagen2])
concat_h2 = cv2.hconcat([imagen2, imagen1, imagen2, imagen1])
concat_v = cv2.vconcat([concat_h1, concat_h2])
cv2.imshow('concat_v', concat_v)

# Concatenando una imagen arriba y 3 abajo
imagen3 = imutils.resize(imagen3, width=600)
concat_h_3imagenes = cv2.hconcat([imagen1, imagen2, imagen1])
concat_v_1sobre3 = cv2.vconcat([imagen3, concat_h_3imagenes])

cv2.imshow('concat_v', concat_v)
cv2.imshow('concat_horizontal', concat_horizontal)
cv2.imshow('concat_v_1sobre3', concat_v_1sobre3)
cv2.waitKey(0)
cv2.destroyAllWindows()