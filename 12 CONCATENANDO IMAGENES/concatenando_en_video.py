import cv2
import imutils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
	ret, frame = cap.read()
	if ret == False: break

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

	# Ya que gray y th tienen solo un canal habrá que pasar las imágenes
	# a 3 canales, luego se redimensionarán para realizar concatenar
	# las imágenes
	gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
	th = cv2.cvtColor(th, cv2.COLOR_GRAY2BGR)
	gray = imutils.resize(gray, height = (gray.shape[0] // 2))
	th = imutils.resize(th, height = (th.shape[0] // 2))

	# Puedes imprimir las dimensiones de frame, gray y th
	#print('frame.shape = ', frame.shape)
	#print('gray.shape = ', gray.shape)
	#print('th.shape = ', th.shape)

	# Concatenando primero verticalmente y luego horizontalmente
	concat_v = cv2.vconcat([gray, th])
	concat_h = cv2.hconcat([frame, concat_v])

	# Colocamos texto en las 3 imágenes
	cv2.putText(concat_h, 'Video streaming', (10, 20), 1, 1.5, 
		(0, 255, 0), 2)
	cv2.putText(concat_h, 'Escala de grises', (650, 20), 1, 1.5, 
		(0, 255, 0), 2)
	cv2.putText(concat_h, 'Binarizada', (650, 260), 1, 1.5, 
		(0, 255, 0), 2)

	# Visualización
	#cv2.imshow('Frame',frame)
	#cv2.imshow('gray',gray)
	#cv2.imshow('th',th)
	cv2.imshow('concat_h',concat_h)

	if cv2.waitKey(1) & 0xFF == ord ('q'):
		break
cap.release()
cv2.destroyAllWindows()