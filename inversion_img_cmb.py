import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

### Add the image to process
ruta_imagen = r'C:\Users\cotif\Documents\GitHub\imgtoSTL\imgs\COBE_1.png'
img_original = cv2.imread(ruta_imagen)

### Converto BGR to RGB 
imagen_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)

### Extract image matrix
matriz = np.asarray(imagen_rgb)
h, w, c = matriz.shape

### Create empty matrix for each color
pr = np.zeros((h, w, c), dtype=np.uint8) #Red
pp = np.zeros((h, w, c), dtype=np.uint8) #Pink   
py = np.zeros((h, w, c), dtype=np.uint8) #Yellow
pg = np.zeros((h, w, c), dtype=np.uint8) #Green
pc = np.zeros((h, w, c), dtype=np.uint8) #Cyan
pb = np.zeros((h, w, c), dtype=np.uint8) #Blue
pbl = np.zeros((h, w, c), dtype=np.uint8) #Black
pw = np.zeros((h, w, c), dtype=np.uint8)  #White
pe = np.zeros((h, w, c), dtype=np.uint8)  #Extra
pbr = np.zeros((h, w, c), dtype=np.uint8) #Brown
po = np.zeros((h, w, c), dtype=np.uint8)  #Orange
pvi = np.zeros((h, w, c), dtype=np.uint8) #Violet
### Create matrix to store positions 
x = np.zeros((h, w))
y = np.zeros((h, w))
### -----------------Clasificacion -------------------------------------------
for i in range(h):
    for j in range(w):
        pixel = imagen_rgb[i, j]
        r, g, b = pixel

        total = int(r) + int(g) + int(b)

        if total == 0:
            pR = 0
            pG = 0
            pB = 0
        else:
            pR = (r / total) * 100
            pG = (g / total) * 100
            pB = (b / total) * 100
        #NEGRO
        if total == 0:
            x[i, j] = j
            y[i, j] = i
            pbl[i, j] = pixel
        #BLANCO
        elif 25 <= pR <= 40 and 25 <= pG <= 40 and 25 <= pB <= 40:
            x[i, j] = j
            y[i, j] = i
            pw[i, j] = pixel
        #ROJO
        elif pR >= 50 and pG <= 30 and pB <= 30:
            x[i, j] = j
            y[i, j] = i
            pr[i, j] = pixel
        #CIAN
        elif pR <= 21 and pG >= 33 and pB >= 39 and abs(pG - pB) <= 20:
            x[i, j] = j
            y[i, j] = i
            pc[i, j] = pixel
        #AZUL
        elif pB >= 15 and pR <= 35 and pG <= 53:
            x[i, j] = j
            y[i, j] = i
            pb[i, j] = pixel
        
        #AMARILLO
        elif pR >= 35 and pG >= 35 and pB <= 20:
            x[i, j] = j
            y[i, j] = i 
            py[i, j] = pixel
        #ROSA/MAGENTA  
        elif pR >= 40 and pB >= 20 and pG <= 25 and pR > pB:
            x[i, j] = j
            y[i, j] = i
            pp[i, j] = pixel
        #VIOLETA
        elif pR >= 30 and pB >= 20 and pG <= 40:
            x[i, j] = j
            y[i, j] = i 
            pvi[i, j] = pixel
        #NARANJA
        elif pR >= 35 and 20 <= pG <= 40 and pB <= 35:
            x[i, j] = j
            y[i, j] = i 
            po[i, j] = pixel  
        #VERDE
        elif pR >= 0 and pB <= 75 and pG >= 10:
            x[i, j] = j
            y[i, j] = i 
            pg[i, j] = pixel
        
        #EXTRA
        else:
            x[i, j] = j
            y[i, j] = i 
            pe[i, j] = pixel
# ----------------- INVERSION: COBE CELESTE ---------------------------

# imagen_modificada = imagen_rgb.copy()

# for i in range(h):
#     for j in range(w):

#         # AZUL → AMARILLO
#         if np.any(pb[i, j] != 0):
#             imagen_modificada[i, j] = [255, 255, 0]

#         # AMARILLO → AZUL
#         elif np.any(py[i, j] != 0):
#             imagen_modificada[i, j] = [0, 0, 255]

#         # CIAN → VERDE
#         elif np.any(pc[i, j] != 0):
#             imagen_modificada[i, j] = [0, 255, 0]

#         # VERDE → CIAN
#         elif np.any(pg[i, j] != 0):
#             imagen_modificada[i, j] = [0, 255, 255]
# #fondo negrp
#         elif np.any(pw[i, j] != 0):
#             imagen_modificada[i, j] = [0, 0, 0]
# # Guardar imagen
# ruta_salida = Path(ruta_imagen).parent / "cobeceleste_inv.png"
# cv2.imwrite(str(ruta_salida), cv2.cvtColor(imagen_modificada, cv2.COLOR_RGB2BGR))

# # Mostrar
# plt.imshow(imagen_modificada)
# plt.title("Imagen invertida")
# plt.axis('off')
#plt.show()
# # ----------------- INTERCAMBIO: WMAP---------------------------
# imagen_modificada = imagen_rgb.copy()
# for i in range(h):
#     for j in range(w):

#         # AZUL → ROJO
#         if np.any(pb[i, j] != 0):
#             imagen_modificada[i, j] = [255, 0, 0]

#         # ROJO → AZUL
#         elif np.any(pr[i, j] != 0):
#             imagen_modificada[i, j] = [0, 0, 255]

#         # NARANJA → CIAN
#         elif np.any(po[i, j] != 0):
#             imagen_modificada[i, j] = [0, 255, 255]

#         # CIAN → NARANJA
#         elif np.any(pc[i, j] != 0):
#             imagen_modificada[i, j] = [255, 125, 0]

#         # AMARILLO → VERDE
#         elif np.any(py[i, j] != 0):
#             imagen_modificada[i, j] = [0, 255, 0]

#         # VERDE → AMARILLO
#         elif np.any(pg[i, j] != 0):
#             imagen_modificada[i, j] = [255, 255, 0]
#             # fondo negro
#         elif np.any(pw[i, j] != 0):
#             imagen_modificada[i, j] = [0, 0, 0]

# # Guardar imagen nueva
# ruta_salida = Path(ruta_imagen).parent / "inversion_wmap.png"
# cv2.imwrite(str(ruta_salida), cv2.cvtColor(imagen_modificada, cv2.COLOR_RGB2BGR))

# # Mostrar
# plt.imshow(imagen_modificada)
# plt.title("Inversion de escala")
# plt.axis('off')
# plt.show()

#----------------------COBE ROSA------------------------------
imagen_modificada = imagen_rgb.copy()
for i in range(h):
    for j in range(w):

        # AZUL → ROSA
        if np.any(pb[i, j] != 0):
            imagen_modificada[i, j] = [255, 105, 180]

        # ROSA → AZUL
        elif np.any(pvi[i, j] != 0):
            imagen_modificada[i, j] = [0, 0, 255]

        # ROJO → CIAN
        elif np.any(pr[i, j] != 0):
            imagen_modificada[i, j] = [0, 255, 255]

        # CIAN → ROJO
        elif np.any(pc[i, j] != 0):
            imagen_modificada[i, j] = [255,0, 0]


# Guardar imagen nueva
ruta_salida = Path(ruta_imagen).parent / "inversion_COBEROSA.png"
cv2.imwrite(str(ruta_salida), cv2.cvtColor(imagen_modificada, cv2.COLOR_RGB2BGR))

# Mostrar
plt.imshow(imagen_modificada)
plt.title("Inversion de escala")
plt.axis('off')
plt.show()

### Plot the clasification 
plt.figure(figsize=(12, 6))

plt.subplot(3, 3, 1)
plt.title('VIOLET CHANNEL')
plt.imshow(pvi, cmap='gray')

plt.subplot(3, 3, 2)
plt.title('RED CHANNEL')
plt.imshow(pr, cmap='gray')

plt.subplot(3, 3, 3)
plt.title('ORANGE CHANNEL')
plt.imshow(po, cmap='gray')

plt.subplot(3, 3, 4)
plt.title('YELLOW CHANNEL')
plt.imshow(py, cmap='gray')

plt.subplot(3, 3, 5)
plt.title('GREEN CHANNEL')
plt.imshow(pg, cmap='gray')

plt.subplot(3, 3, 6)
plt.title('CYAN CHANNEL')
plt.imshow(pc, cmap='gray')

plt.subplot(3, 3, 7)
plt.title('BLUE CHANNEL')
plt.imshow(pb, cmap='gray')

plt.subplot(3, 3, 8)
plt.title('WHITE CHANNEL')
plt.imshow(pw, cmap='gray')

plt.subplot(3, 3, 9)
plt.title('PINK')
plt.imshow(pp, cmap='gray')
plt.show()
# ----------------- RECLASIFICACION DE IMAGEN MODIFICADA ---------------------------

# Nuevas matrices
pr2 = np.zeros((h, w, c), dtype=np.uint8)
py2 = np.zeros((h, w, c), dtype=np.uint8)
pg2 = np.zeros((h, w, c), dtype=np.uint8)
pc2 = np.zeros((h, w, c), dtype=np.uint8)
pb2 = np.zeros((h, w, c), dtype=np.uint8)
pw2 = np.zeros((h, w, c), dtype=np.uint8)
pbl2 = np.zeros((h, w, c), dtype=np.uint8)
po2 = np.zeros((h, w, c), dtype=np.uint8)
pvi2 = np.zeros((h, w, c), dtype=np.uint8)
pe2 = np.zeros((h, w, c), dtype=np.uint8)

pp2 = np.zeros((h, w, c), dtype=np.uint8) #Pink  
for i in range(h):
    for j in range(w):
        pixel = imagen_modificada[i, j]
        r, g, b = pixel

        total = int(r) + int(g) + int(b)

        if total == 0:
            pR = pG = pB = 0
        else:
            pR = (r / total) * 100
            pG = (g / total) * 100
            pB = (b / total) * 100

        # NEGRO
        if total == 0:
            pbl2[i, j] = pixel

        # BLANCO
        elif 25 <= pR <= 40 and 25 <= pG <= 40 and 25 <= pB <= 40:
            pw2[i, j] = pixel

        # ROJO
        elif pR >= 50 and pG <= 30 and pB <= 30:
            pr2[i, j] = pixel

        # CIAN
        elif pR <= 21 and pG >= 33 and pB >= 39 and abs(pG - pB) <= 20:
            pc2[i, j] = pixel

        # AZUL
        elif pB >= 15 and pR <= 35 and pG <= 53:
            pb2[i, j] = pixel

        # AMARILLO
        elif pR >= 35 and pG >= 35 and pB <= 20:
            py2[i, j] = pixel
        #ROSA/MAGENTA
        elif pR >= 40 and pB >= 20 and pG <= 25 and pR > pB:
                    pp2[i, j] = pixel
        # VIOLETA
        elif pR >= 30 and pB >= 20 and pG <= 40:
            pvi2[i, j] = pixel

        # NARANJA
        elif pR >= 35 and 20 <= pG <= 40 and pB <= 35:
            po2[i, j] = pixel

        # VERDE
        elif pR >= 0 and pB <= 75 and pG >= 10:
            pg2[i, j] = pixel

        # EXTRA
        else:
            pe2[i, j] = pixel

# ----------------- PLOT CLASIFICACION MODIFICADA ---------------------------

plt.figure(figsize=(12, 6))

plt.subplot(3, 3, 1)
plt.title('VIOLET CHANNEL')
plt.imshow(pvi2, cmap='gray')

plt.subplot(3, 3, 2)
plt.title('RED CHANNEL')
plt.imshow(pr2, cmap='gray')

plt.subplot(3, 3, 3)
plt.title('ORANGE CHANNEL')
plt.imshow(po2, cmap='gray')

plt.subplot(3, 3, 4)
plt.title('YELLOW CHANNEL')
plt.imshow(py2, cmap='gray')

plt.subplot(3, 3, 5)
plt.title('GREEN CHANNEL')
plt.imshow(pg2, cmap='gray')

plt.subplot(3, 3, 6)
plt.title('CYAN CHANNEL')
plt.imshow(pc2, cmap='gray')

plt.subplot(3, 3, 7)
plt.title('BLUE CHANNEL')
plt.imshow(pb2, cmap='gray')

plt.subplot(3, 3, 8)
plt.title('WHITE CHANNEL')
plt.imshow(pw2, cmap='gray')

plt.subplot(3, 3, 9)
plt.title('PINK')
plt.imshow(pp2, cmap='gray')

plt.tight_layout()
plt.show()