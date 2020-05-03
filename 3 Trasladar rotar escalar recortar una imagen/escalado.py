import cv2

image = cv2.imread('ave.jpg')

# Escalando una imagen
imageOut = cv2.resize(image,(600,300), interpolation=cv2.INTER_CUBIC)

# Escalando una imagen usando imutils.resize
#imageOut1 = imutils.resize(image,width=300)
#imageOut2 = imutils.resize(image,height=300)
#cv2.imshow('Imagen de salida1',imageOut1)
#cv2.imshow('Imagen de salida2',imageOut2)

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()