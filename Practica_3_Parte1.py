import numpy as np
from matplotlib import pyplot as plt
import cv2 #Opencv
import skimage
from skimage import io
import math

img1 = cv2.imread('foto.png',1)
img2 = cv2.imread('foto2.png',1)

#De matriz BGR a RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#Tamaño y Canales
(alto1, ancho1, canales1) = img1.shape
print('Alto={}, Ancho={}, Canales={}'.format(alto1, ancho1, canales1))
(alto2, ancho2, canales2) = img2.shape
print('Alto={}, Ancho={}, Canales={}'.format(alto2, ancho2, canales2))
#Dimencionamiento en bruto
Redimg1 = cv2.resize(img1, (300, 300))
Redimg2 = cv2.resize(img2, (300, 300))

#De matriz BGR a RGB "Genio!!"
Redimg1 = cv2.cvtColor(Redimg1, cv2.COLOR_BGR2RGB)
Redimg2 = cv2.cvtColor(Redimg2, cv2.COLOR_BGR2RGB)

#Concatenamiento de la Primera imagen a la Segunda imagen
combinado1 = np.concatenate((Redimg1, Redimg2), axis=1)  #Concatenar
cv2.imshow('combinado', combinado1)
cv2.waitKey()


# >>>>>>>>>>>>>>>>>>>>>>> 1) Suma <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Suma 1
suma = cv2.add(Redimg1,Redimg2) #Redimg1+Redimg2
combinado2 = np.concatenate((Redimg1, suma, Redimg2), axis=1)

# Variable = cv2.calcHist([imagen], [CoG], )
# BGR -> Color: B= 0; G= 1; R= 2
# Tamaño -> [256]
# Rango -> [0, 256]
histsuma1B = cv2.calcHist([suma], [0], None, [256], [0, 256]) #Azul
histsuma1G = cv2.calcHist([suma], [1], None, [256], [0, 256]) #Verde
histsuma1R = cv2.calcHist([suma], [2], None, [256], [0, 256]) #Rojo

# plt.subplots(Filas, Columnas)
# ax -> para las coordenadas
# figurasuma -> para guardar las imágenes y graficas aquí
           # -> y después mostrarlas
figurasuma, ax = plt.subplots(3, 5)

# tamaño del recuadro de graficas imágenes
figurasuma.set_size_inches(12, 42)

# Imagen; Posición de [Fila, Columna]
ax[0, 0].imshow(suma)
ax[0, 0].set_title('Tigres vs Puma')
ax[0, 0].axis('off')

# Graficas
ax[0, 1].plot(histsuma1B, color='b')
ax[0, 1].set_title('Hist. Azul')

ax[0, 2].plot(histsuma1G, color='g')
ax[0, 2].set_title('Hist. Verde')

ax[0, 3].plot(histsuma1R, color='r')
ax[0, 3].set_title('Hist. Rojo')


# Definir colores para plotear el histograma (todos juntos)
colors = ('b', 'g', 'r')

# Imprimir todos los RGB en uno solo
for i, color in enumerate(colors):
    hist = cv2.calcHist([suma], [i], None, [256], [0, 256])
    ax[0, 4].plot(hist, color=color)
ax[0, 4].set_title('Hist. BGR')
plt.show()

print('Operación Suma 1')
cv2.imshow('combinado completo', combinado2)
cv2.waitKey()


