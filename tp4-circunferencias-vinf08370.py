import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('perforacion_zoom.png')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un desenfoque gaussiano
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplicar la transformada de Hough para círculos
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=60,
    param1=40,
    param2=50,
    minRadius=25,
    maxRadius=200
)

if circles is not None:
    # Dibujar los círculos en una copia de la imagen original
    result = image.copy()
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(result, (i[0], i[1]), i[2], (0, 255, 0), 2)

    # Mostrar las imágenes
    cv2.imshow('Original', image)
    cv2.imshow('Circles Detected', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No se encontraron círculos en la imagen.")
