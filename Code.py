import cv2
import numpy as np
import pyvista as pv
from pyvista import StructuredGrid
import matplotlib.pyplot as plt


### Add the image to process
img_original = cv2.imread(r'C:\Users\cotif\Documents\GitHub\imgtoSTL\imgs\wmapp.png')

### If you wwnat to resize the image  
# imgresize = cv2.resize(imagen_original, (512,256))
# cv2.imshow('imagen dimesionada',imgresize)
# cv2.imshow('imagenoriginal',imagen_original)
# cv2.waitKey(0)

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
z = np.zeros((h,w))

# # #-----------------Clasification for WMAPP------------------------------
for i in range(h):
    for j in range(w):
        pixel = imagen_rgb[i, j]
        r, g, b = pixel
        #### Calculate the % of each color in pixel
        pR = r / 255.0 * 100  # % of red 
        pG = g / 255.0 * 100   # % of green
        pB = b / 255.0 * 100  # % of blue
        # Blanco
        if pR >= 65 and pG == 100 and pB >= 65:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            pw[i, j] = pixel
        # Rojo Claro
        if 100 >= pR >= 20 and 30 >= pG >= 0 and 50 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 76
            # Rojo
        elif 100 >= pR >= 20 and 25 >= pG >= 0 and 30 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 78
            # Rojo Oscuro
        elif 70 >= pR >= 20 and 25 >= pG >= 0 and 10 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 70
            # Verde Claro
        elif 80 >= pR >= 40 and 100 >= pG >= 70 and 85 >= pB >= 15:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 48
            pg[i, j] = pixel
            # Verde
        elif 70 >= pR >= 0 and 100 >= pG >= 60 and 100 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 50
            pg[i, j] = pixel
            # Verde Oscuro
        elif 75 >= pR >= 0 and 75 >= pG >= 30 and 52 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 52
            pg[i, j] = pixel
            # Azul Claro
        elif 50 >= pR >= 0 and 50 >= pG >= 0 and 100 >= pB >= 5:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 36
            pb[i, j] = pixel
            # azul
        elif 45 >= pR >= 0 and 25 >= pG >= 0 and 100 >= pB >= 5:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 38
            pb[i, j] = pixel
            # Azul Oscuro
        elif 35 >= pR >= 0 and 25 >= pG >= 0 and 65 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 40
            pb[i, j] = pixel
             # Cian Claro
        elif 75 >= pR >= 0 and 100 >= pG >= 50 and 100 >= pB >= 50:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 42
            pc[i, j] = pixel
            # Cian
        elif 30 >= pR >= 0 and 100 >= pG >= 40 and 100 >= pB >= 40:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 5
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 44
            pc[i, j] = pixel
            # Cian Oscuro
        elif 40 >= pR >= 0 and 50 >= pG >= 20 and 50 >= pB >= 20:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 46
            pc[i, j] = pixel
            # Amarillo claro
        elif 100 >= pR >= 80 and 100 >= pG >= 60 and 70 >= pB >= 20:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 56
            py[i, j] = pixel
        # Amarillo
        elif 100 >= pR >= 70 and 100 >= pG >= 60 and 35 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 58
            py[i, j] = pixel
            # Amarillo Oscuro
        elif 80 >= pR >= 60 and 80 >= pG >= 60 and 50 >= pB >= 10:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 60
            py[i, j] = pixel
        # Marron Claro
        elif 100 >= pR >= 50 and 60 >= pG >= 40 and 40 >= pB >= 10:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 68
            pbr[i, j] = pixel
        # Marron
        elif 80 >= pR >= 50 and 60 >= pG >= 35 and 10 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 70
            pbr[i, j] = pixel
        # Marron Oscuro
        elif 65 >= pR >= 30 and 55 >= pG >= 15 and 30 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 72
            pbr[i, j] = pixel
            # Naranja Claro
        elif 100 >= pR >= 65 and 65 >= pG >= 30 and 35 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 62
            po[i, j] = pixel
        # Naranja Medio
        elif 85 >= pR >= 55 and 45 >= pG >= 20 and 20 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 64
            po[i, j] = pixel
        # Naranja Oscuro
        elif 90 >= pR >= 55 and 45 >= pG >= 25 and 15 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 66
            po[i, j] = pixel
            # Negro
        elif pR == 0 and pG == 0 and pB == 0:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 30
            pbl[i, j] = pixel
        else:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 6
            pe[i, j] = pixel
####---------------------WMAP 1 
# for i in range(h):
#     for j in range(w):
#         pixel = imagen_rgb[i, j]
#         r, g, b = pixel
#         #### Calculate the % of each color in pixel
#         pR = r / 255.0 * 100  # % of red 
#         pG = g / 255.0 * 100   # % of green
#         pB = b / 255.0 * 100  # % of blue
#         # WHITE
#         if 100 >= pR >= 80 and 100 >= pG >= 80 and 100 >= pB >= 80:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 5
#             pw[i, j] = pixel
#         # LIGHT RED
#         if 100 >= pR >= 50 and 30 >= pG >= 0 and 50 >= pB >= 0:
#             pr[i, j] = pixel
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 90
#             # RED
#         elif 100 >= pR >= 30 and 15 >= pG >= 0 and 30 >= pB >= 0:
#             pr[i, j] = pixel
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 95
#             # DARK RED
#         elif 70 >= pR >= 30 and 20 >= pG >= 0 and 10 >= pB >= 0:
#             pr[i, j] = pixel
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 100
#            #LIGHT ORANGE
#         elif 100 >= pR >= 65 and 65 >= pG >= 30 and 47 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 75
#             po[i, j] = pixel
#         # ORANGE
#         elif 85 >= pR >= 55 and 45 >= pG >= 20 and 20 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 80
#             po[i, j] = pixel
#         # DARK ORANGE
#         elif 90 >= pR >= 55 and 45 >= pG >= 25 and 15 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 85
#             po[i, j] = pixel
#          #LIGHT BROWN
#         elif 80 >= pR >= 50 and 60 >= pG >= 40 and 40 >= pB >= 10:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 60
#             pbr[i, j] = pixel
#         # BROWN
#         elif 80 >= pR >= 55 and 60 >= pG >= 35 and 35 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 65
#             pbr[i, j] = pixel
#         # DARK BROWN
#         elif 65 >= pR >= 30 and 45 >= pG >= 15 and 10 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 70
#             pbr[i, j] = pixel
            
#         # LIGHT YELLOW
#         elif 100 >= pR >= 80 and 100 >= pG >= 60 and 95 >= pB >= 20:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 45
#             py[i, j] = pixel
#         # YELLOW
#         elif 100 >= pR >= 50 and 85 >= pG >= 30 and 35 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 50
#             py[i, j] = pixel
#             # DARK YELLOW
#         elif 80 >= pR >= 60 and 80 >= pG >= 60 and 50 >= pB >= 10:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 55
#             py[i, j] = pixel
#             # LIGHT GREEN
#         elif 95 >= pR >= 40 and 100 >= pG >= 70 and 85 >= pB >= 15:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 40
#             pg[i, j] = pixel
#             # GREEN
#         elif 85 >= pR >= 0 and 100 >= pG >= 60 and 50 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 38
#             pg[i, j] = pixel
#             # DARK GREEN
#         elif 75 >= pR >= 0 and 75 >= pG >= 15 and 55 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 34
#             pg[i, j] = pixel
#                # Cian Claro
#         elif 85 >= pR >= 30 and 100 >= pG >= 50 and 100 >= pB >= 50:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 32
#             pc[i, j] = pixel
#             # Cian
#         elif 30 >= pR >= 0 and 100 >= pG >= 40 and 100 >= pB >= 40:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 28
#             pc[i, j] = pixel
#             # Cian Oscuro
#         elif 40 >= pR >= 0 and 50 >= pG >= 20 and 50 >= pB >= 20:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 24
#             pc[i, j] = pixel
            
#             # Azul Claro
#         elif 50 >= pR >= 0 and 50 >= pG >= 0 and 100 >= pB >= 5:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 20
#             pb[i, j] = pixel
#             # azul
#         elif 45 >= pR >= 0 and 25 >= pG >= 0 and 100 >= pB >= 5:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 18
#             pb[i, j] = pixel
#             # Azul Oscuro
#         elif 35 >= pR >= 0 and 25 >= pG >= 0 and 65 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 16
#             pb[i, j] = pixel
#             # Negro
#         elif pR == 0 and pG == 0 and pB == 0:
#             x[i, j] = j
#             y[i, j] = i
#             z[i, j] = 6
#             pbl[i, j] = pixel
#         else:
#             x[i, j] = j
#             y[i, j] = i
#             z[i, j] = 6
#             pe[i, j] = pixel

### Plot the clasification 
plt.figure(figsize=(12, 6))

plt.subplot(3, 3, 1)
plt.title('BROWN CHANNEL')
plt.imshow(pbr, cmap='gray')

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
plt.title('EXTRA')
plt.imshow(pe, cmap='gray')
plt.show()

### Create a base for the model 
x_base, y_base = np.meshgrid(range(w), range(h))
z_base = np.zeros_like(x_base)

### Merge base values and pixels
x = np.stack((x_base, x), axis=0)
y = np.stack((y_base, y), axis=0)
z = np.stack((z_base, z), axis=0)

### Create the structure
mesh = pv.StructuredGrid(-x, y, z)

### Dimension the mesh
mesh.points [:,0] /= 10
mesh.points [:,1] /= 10
mesh.points[:,2] /= 15

### Show the strcucture
p = pv.Plotter()
p.add_mesh(mesh, color="gray")
p.show()

### Export the model to stl 
polydata = mesh.extract_geometry()
stl_file = 'wmapp.stl'
polydata.save(stl_file)
print("se guardo la imagen como: ", stl_file)
