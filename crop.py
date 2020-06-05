import numpy as np
import cv2
imagem = cv2.imread('img/ponte.png')
recorte = imagem[10:1900, 100:200]
cv2.imshow("Recorte da imagem", recorte)
cv2.waitKey(0)
