import numpy as np
from matplotlib import pyplot as plt
import cv2 #Opencv
import skimage
from skimage import io
import math

#Imágenes Iniciales
img1 = cv2.imread('Foto.png', 1)
img2 = cv2.imread('Foto2.png', 1)

#Dimencionamiento en bruto
Redimg1 = cv2.resize(img1, (300, 300))
Redimg2 = cv2.resize(img2, (300, 300))

#De matriz BGR a RGB "Genio!!"
Redimg1 = cv2.cvtColor(Redimg1, cv2.COLOR_BGR2RGB)
Redimg2 = cv2.cvtColor(Redimg2, cv2.COLOR_BGR2RGB)

# >>>>>>>>>>>>>>>>>>>>>>> 1) Suma <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Suma 1
suma = cv2.add(Redimg1,Redimg2) #Redimg1+Redimg2
combinado2 = np.concatenate((Redimg1, suma, Redimg2), axis=1)

# plt.subplots(Filas, Columnas)
# ax -> para las coordenadas
figurasuma, ax = plt.subplots(3, 4)
# tamaño del recuadro de graficas imágenes
figurasuma.set_size_inches(12, 35)

# Forma de impresión de las imágenes y gráficos -> sistema 3x4
# # Img1   ; HistImg1 ; ImgEc1   ; HistImgEc1;
# # ImgSum1; HistSum1 ; ImgSum1Ec; ImgSum1Ec ;
# # Img2   ; HistImg2 ; ImgEc2   ; HistImgEc2;

# Posiciones de las imágenes
ax[0, 0].imshow(Redimg1)
ax[0, 0].set_title('Tigre')
ax[0, 0].axis('off')

ax[1, 0].imshow(suma)
ax[1, 0].set_title('Suma')
ax[1, 0].axis('off')

ax[2, 0].imshow(Redimg2)
ax[2, 0].set_title('Puma')
ax[2, 0].axis('off')

# Definir colores para plotear el Histograma
colors = ('b', 'g', 'r')

# Imprimir todos los Histogramas RGB sin ecualizar
for i, color in enumerate(colors):
    hist1 = cv2.calcHist([Redimg1], [i], None, [256], [0, 256])
    ax[0, 1].plot(hist1, color=color)
#ax[0, 1].set_title('H. Imag1 BGR')

for i, color in enumerate(colors):
    hist2 = cv2.calcHist([suma], [i], None, [256], [0, 256])
    ax[1, 1].plot(hist2, color=color)
#ax[1, 1].set_title('H. Suma1 BGR')

for i, color in enumerate(colors):
    hist3 = cv2.calcHist([Redimg2], [i], None, [256], [0, 256])
    ax[2, 1].plot(hist3, color=color)
#ax[2, 1].set_title('H. Imag2 BGR')

# Ecualizar imagenes
Img1Ec = cv2.cvtColor(Redimg1, cv2.COLOR_BGR2YUV)
Img1Ec[:, :, 0] = cv2.equalizeHist(Img1Ec[:, :, 0])
Img1Ec = cv2.cvtColor(Img1Ec, cv2.COLOR_YUV2BGR)
ax[0, 2].imshow(Img1Ec)
ax[0, 2].set_title('Ec. Tigre')
ax[0, 2].axis('off')

ImgSum1Ec = cv2.cvtColor(suma, cv2.COLOR_BGR2YUV)
ImgSum1Ec[:, :, 0] = cv2.equalizeHist(ImgSum1Ec[:, :, 0])
ImgSum1Ec = cv2.cvtColor(ImgSum1Ec, cv2.COLOR_YUV2BGR)
ax[1, 2].imshow(ImgSum1Ec)
ax[1, 2].set_title('Ec. Suma')
ax[1, 2].axis('off')

Img2Ec = cv2.cvtColor(Redimg2, cv2.COLOR_BGR2YUV)
Img2Ec[:, :, 0] = cv2.equalizeHist(Img2Ec[:, :, 0])
Img2Ec = cv2.cvtColor(Img2Ec, cv2.COLOR_YUV2BGR)
ax[2, 2].imshow(Img2Ec)
ax[2, 2].set_title('Ec. Puma')
ax[2, 2].axis('off')

# Imprimir todos los Histogramas RGB ecualizados
for i, color in enumerate(colors):
    ehist1 = cv2.calcHist([Img2Ec], [i], None, [256], [0, 256])
    ax[0, 3].plot(ehist1, color=color)
#ax[0, 3].set_title('H. Imag1 BGR')

for i, color in enumerate(colors):
    ehist2 = cv2.calcHist([ImgSum1Ec], [i], None, [256], [0, 256])
    ax[1, 3].plot(ehist2, color=color)
#ax[1, 3].set_title('H. Suma1 BGR')

for i, color in enumerate(colors):
    ehist3 = cv2.calcHist([Img2Ec], [i], None, [256], [0, 256])
    ax[2, 3].plot(ehist3, color=color)
#ax[2, 3].set_title('H. Imag2 BGR')
plt.show()
