import cv2 
import numpy as np 

img = cv2.imread('img/ponte.png')

#split
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

#merge
recolocado = cv2.merge([canalAzul, canalVerde, canalVermelho])

#exibir nas cores originais
zeros = np.zeros(img.shape[:2], dtype = "uint8")


cv2.imshow("Original",img)
cv2.imshow("Canal Vermelho", canalVermelho)
cv2.imshow("Canal Verde", canalVerde)
cv2.imshow("Canal Azul", canalAzul)
cv2.imshow("Canais juntos", recolocado)
cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))



cv2.waitKey(0)

# (b, g, r) = cv2.split(variavel da imagem)

# cv2.merge([b, g, r])