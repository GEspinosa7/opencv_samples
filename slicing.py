import cv2

imagem_m = cv2.imread('img/ponte.png')
imagem_s = cv2.imread('img/ponte.png')
imagem_m2 = cv2.imread('img/ponte.png')
imagem = cv2.imread('img/ponte.png')

(b, g, r) = imagem_m[0, 0] #ordem BGR e nao RGB
(b, g, r) = imagem_m2[0, 0]

for y in range(0, imagem_m.shape[0], 10): # percorre linhas pulando pixels de 10 em 10
 for x in range(0, imagem_m.shape[1], 10): # percorre colunas pulando pixels de 10 em 10
    imagem_m[y:y+3, x: x+3] = (0,255,255) # cada salto cria um quadrado de 3x3 pixels

imagem_s[100:150, 100:150] = (255, 0, 0)

cv2.imshow("imagem com slicing", imagem_s)

cv2.waitKey(0) #espera pressionar qualquer tecla

