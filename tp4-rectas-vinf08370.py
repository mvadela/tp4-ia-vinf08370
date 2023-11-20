import cv2
import numpy as np

# Cargamos la imagen
image = cv2.imread('perforacion_zoom.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar desenfoque gaussiano para reducir el ruido
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Ajustar el umbral en la detección de bordes con el operador de Canny
edges = cv2.Canny(blurred, 50, 150)  # Estos valores los podemos ajustar para mayor precision

# Ajustar el tercer parámetro (umbral) en la función cv2.HoughLines
lines = cv2.HoughLines(edges, 1, np.pi / 180, 90)

# Verificamos si se encontraron líneas antes de intentar iterar sobre ellas
if lines is not None:
    # Dibujamos las líneas en una copia de la imagen original
    result = image.copy()
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Mostramos la imagen original y la imagen con las líneas detectadas
    cv2.imshow('Original', image)
    cv2.imshow('Lines Detected', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No se encontraron líneas en la imagen.")
