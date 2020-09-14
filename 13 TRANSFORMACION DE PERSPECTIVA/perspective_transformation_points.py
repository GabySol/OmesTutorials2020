import cv2
import numpy as np

imagen = cv2.imread('gato.jpeg')

cv2.circle(imagen, (84, 69), 7, (255,0,0), 2)
cv2.circle(imagen, (513, 77), 7, (0,255,0), 2)
cv2.circle(imagen, (113, 358), 7, (0,0,255), 2)
cv2.circle(imagen, (542, 366), 7, (255,255,0), 2)

pts1 = np.float32([[84,69], [513,77], [113, 358], [542,366]])
pts2 = np.float32([[0,0], [480,0], [0,300], [480,300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(imagen, M, (480,300))

cv2.imshow('Imagen', imagen)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()