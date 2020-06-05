import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imagem com seus dados de altura, largura e canais
# Cria a tupla colors (BGR) e cria a lista features
img = cv2.imread('img/ponte.png',-1)
height, width, channels = img.shape
colors = ('b', 'g', 'r')
features=[]

#Cria a máscara
mask = np.zeros(img.shape[:2], np.uint8)
mask[int(height*0.1):int(height*0.9), 0:int(width*0.6)] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

#Mostra a imagem original, a máscara e a imagem com adição da máscara
plt.subplot(221), plt.imshow(img)
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img)
plt.show()

#Exemplo PYImageSearch
#Carrega o Histograma da imagem inteira
chans = cv2.split(img)
for (chan, color) in zip(chans, colors):
    hist_full = cv2.calcHist([chan], [0], None, [256], [0, 256])
    features.extend(hist_full)
    plt.plot(hist_full, color=color)
    plt.xlim([0, 256])
plt.show()

#Exemplo Doc OpenCV
#Carrega a imagem com a adição da máscara
for i,col in enumerate(colors):
    hist_mask = cv2.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist_mask, color=col)
    plt.xlim([0, 256])
plt.show()