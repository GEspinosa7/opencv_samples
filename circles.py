import numpy as np
import cv2

img = cv2.imread('img/ponte.png')

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

cv2.line(img, (0, 0), (100, 200), green)
cv2.line(img, (300, 200), (150, 150), red, 5)
cv2.rectangle(img, (20, 20), (120, 120), blue, 10)
cv2.rectangle(img, (200, 50), (225, 125), green, -1)

(X, Y) = (img.shape[1] // 2, img.shape[0] // 2)

for raio in range(0, 175, 15):   
    cv2.circle(img, (X, Y), raio, red)

cv2.imshow("Desenhando sobre a img", img)
cv2.waitKey(0)