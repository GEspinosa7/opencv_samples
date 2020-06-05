import numpy as np
import imutils
import cv2
img = cv2.imread('img/ponte.png')
cv2.imshow("Original", img)
img_redimensionada = img[::2,::2]
cv2.imshow("Imagem redimensionada", img_redimensionada)
cv2.waitKey(0)


# O código basicamente refaz a imagem interpolando linhas e colunas, ou seja, pega a
# primeira linha, ignora a segunda, depois pega a terceira linha, ignora a quarta, e assim por
# diante. O mesmo é feito com as colunas.