import numpy as np
import cv2
imagem = cv2.imread('img/ponte.png')
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'Teste',(15,65), fonte,
2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Ponte", imagem)
cv2.waitKey(0)