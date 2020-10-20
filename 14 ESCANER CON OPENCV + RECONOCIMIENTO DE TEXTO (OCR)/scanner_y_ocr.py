import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ordenar_puntos(puntos):
	n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()

	y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])

	x1_order = y_order[:2]
	x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])

	x2_order = y_order[2:4]
	x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
	
	return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]
	
image = cv2.imread('img_00.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)

cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]

for c in cnts:
	epsilon = 0.01*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)
	
	if len(approx)==4:
		cv2.drawContours(image, [approx], 0, (0,255,255),2)
		
		puntos = ordenar_puntos(approx)

		cv2.circle(image, tuple(puntos[0]), 7, (255,0,0), 2)
		cv2.circle(image, tuple(puntos[1]), 7, (0,255,0), 2)
		cv2.circle(image, tuple(puntos[2]), 7, (0,0,255), 2)
		cv2.circle(image, tuple(puntos[3]), 7, (255,255,0), 2)
		
		pts1 = np.float32(puntos)
		pts2 = np.float32([[0,0],[270,0],[0,310],[270,310]])
		M = cv2.getPerspectiveTransform(pts1,pts2)
		dst = cv2.warpPerspective(gray,M,(270,310))
		cv2.imshow('dst', dst)
		
		texto = pytesseract.image_to_string(dst, lang='spa')
		print('texto: ', texto)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()