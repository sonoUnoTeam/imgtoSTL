import cv2
import numpy as np
import pyvista as pv
from pyvista import StructuredGrid
import matplotlib.pyplot as plt


### Add the image to process
img_original = cv2.imread(r'C:\Users\franc\OneDrive\Escritorio\Coti\imgtoSTL\imgs\wmapp.png')

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
# for i in range(h):
#     for j in range(w):
#         pixel = imagen_rgb[i, j]
#         r, g, b = pixel
#         #### Calculate the % of each color in pixel
#         pR = r / 255.0 * 100  # % of red 
#         pG = g / 255.0 * 100   # % of green
#         pB = b / 255.0 * 100  # % of blue
#         # WHITE
#         if pR >= 65 and pG == 100 and pB >= 65:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             pw[i, j] = pixel
#         #  LIGHT RED 
#         if 100 >= pR >= 20 and 30 >= pG >= 0 and 50 >= pB >= 0:
#             pr[i, j] = pixel
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 48
#             # RED
#         elif 100 >= pR >= 20 and 25 >= pG >= 0 and 30 >= pB >= 0:
#             pr[i, j] = pixel
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 49
#             # DARK RED 
#         elif 70 >= pR >= 20 and 25 >= pG >= 0 and 10 >= pB >= 0:
#             pr[i, j] = pixel
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 50
#             # LIGHT GREEN 
#         elif 80 >= pR >= 40 and 100 >= pG >= 70 and 85 >= pB >= 15:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 38
#             pg[i, j] = pixel
#             # GREEN
#         elif 70 >= pR >= 0 and 100 >= pG >= 60 and 100 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 37
#             pg[i, j] = pixel
#             # DARK GREEN 
#         elif 75 >= pR >= 0 and 75 >= pG >= 30 and 52 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 36
#             pg[i, j] = pixel
#             # LIGHT BLUE 
#         elif 50 >= pR >= 0 and 50 >= pG >= 0 and 100 >= pB >= 5:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 32
#             pb[i, j] = pixel
#             # BLUE
#         elif 45 >= pR >= 0 and 25 >= pG >= 0 and 100 >= pB >= 5:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 31
#             pb[i, j] = pixel
#             # DARK BLUE 
#         elif 35 >= pR >= 0 and 25 >= pG >= 0 and 65 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 30
#             pb[i, j] = pixel
#              #  LIGHT CYAN
#         elif 75 >= pR >= 0 and 100 >= pG >= 50 and 100 >= pB >= 50:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 35
#             pc[i, j] = pixel
#             # CYAN
#         elif 30 >= pR >= 0 and 100 >= pG >= 40 and 100 >= pB >= 40:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 5
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 34
#             pc[i, j] = pixel
#             # DARK CYAN 
#         elif 40 >= pR >= 0 and 50 >= pG >= 20 and 50 >= pB >= 20:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 33
#             pc[i, j] = pixel
#             # LIGHT YELLOW 
#         elif 100 >= pR >= 80 and 100 >= pG >= 60 and 70 >= pB >= 20:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 39
#             py[i, j] = pixel
#         # YELLOW
#         elif 100 >= pR >= 70 and 100 >= pG >= 60 and 35 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 40
#             py[i, j] = pixel
#             #DARK YELLOW
#         elif 80 >= pR >= 60 and 80 >= pG >= 60 and 50 >= pB >= 10:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 41
#             py[i, j] = pixel
#         #  LIGHT BROWN 
#         elif 100 >= pR >= 50 and 60 >= pG >= 40 and 40 >= pB >= 10:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 45
#             pbr[i, j] = pixel
#         # BROWN
#         elif 80 >= pR >= 50 and 60 >= pG >= 35 and 10 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 46
#             pbr[i, j] = pixel
#         # LIGHT BROWN
#         elif 65 >= pR >= 30 and 55 >= pG >= 15 and 30 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 47
#             pbr[i, j] = pixel
#             # LIGHT ORANGE 
#         elif 100 >= pR >= 65 and 65 >= pG >= 30 and 35 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 42
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
#                 z[i, j] = 43
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
#                 z[i, j] = 44
#             po[i, j] = pixel
#             # BLACK
#         elif pR == 0 and pG == 0 and pB == 0:
#             x[i, j] = j
#             y[i, j] = i
#             z[i, j] = 40
#             pbl[i, j] = pixel
#         else:
#             x[i, j] = j
#             y[i, j] = i
#             z[i, j] = 6
#             pe[i, j] = pixel

####-------------------------CODE FOR HIG RESOLUTION IMAGE OF WMAP 1 ---------------------------------
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
#                 z[i, j] = 8
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
#                 z[i, j] = 58
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
#                 z[i, j] = 59
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
#                 z[i, j] = 60
#            #LIGHT ORANGE
#         elif 100 >= pR >= 65 and 65 >= pG >= 30 and 47 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 53
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
#                 z[i, j] = 54
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
#                 z[i, j] = 55
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
#                 z[i, j] = 56
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
#                 z[i, j] = 57
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
#                 z[i, j] = 58
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
#                 z[i, j] = 50
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
#                 z[i, j] = 51
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
#                 z[i, j] = 52
#             py[i, j] = pixel
#             # LIGHT GREEN
#         elif 90 >= pR >= 40 and 100 >= pG >= 70 and 85 >= pB >= 15:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 49
#             pg[i, j] = pixel
#             # GREEN
#         elif 70 >= pR >= 0 and 100 >= pG >= 60 and 50 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 48
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
#                 z[i, j] = 47
#             pg[i, j] = pixel
#                # LIGHT CYAN
#         elif 85 >= pR >= 30 and 100 >= pG >= 50 and 100 >= pB >= 50:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 46
#             pc[i, j] = pixel
#             # CYAN
#         elif 30 >= pR >= 0 and 100 >= pG >= 40 and 100 >= pB >= 40:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 45
#             pc[i, j] = pixel
#             #DARK CYAN
#         elif 40 >= pR >= 0 and 50 >= pG >= 20 and 50 >= pB >= 20:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 44
#             pc[i, j] = pixel
            
#             # LIGHT BLUE
#         elif 50 >= pR >= 0 and 50 >= pG >= 0 and 100 >= pB >= 5:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 43
#             pb[i, j] = pixel
#             # BLUE
#         elif 45 >= pR >= 0 and 25 >= pG >= 0 and 100 >= pB >= 5:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 42
#             pb[i, j] = pixel
#             # DARK BLUE
#         elif 35 >= pR >= 0 and 25 >= pG >= 0 and 65 >= pB >= 0:
#             if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 6
#             else:
#                 x[i, j] = j
#                 y[i, j] = i
#                 z[i, j] = 41
#             pb[i, j] = pixel
#             # BLACK
#         elif pR == 0 and pG == 0 and pB == 0:
#             x[i, j] = j
#             y[i, j] = i
#             z[i, j] = 6
#             pbl[i, j] = pixel
#         else:
#             pe[i, j] = pixel

#------------------------------CODE TO LOW RESOLUTION IMAGES---------------------------------------------------
for i in range(h):
    for j in range(w):
        pixel = imagen_rgb[i, j]
        r, g, b = pixel
        #### Calculate the % of each color in pixel
        pR = r / 255.0 * 100  # % of red 
        pG = g / 255.0 * 100   # % of green
        pB = b / 255.0 * 100  # % of blue
        # WHITE
        if 100 >= pR >= 80 and 100 >= pG >= 80 and 100 >= pB >= 80:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 0
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 0
            pw[i, j] = pixel
        # RED, YELLOW AND ORANGE
        if 100 >= pR >= 60 and 100 >= pG >= 10 and 95 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 40

            # GREEN
        elif 70 >= pR >= 0 and 100 >= pG >= 50 and 50 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 35
            pg[i, j] = pixel
               # CYAN
        elif 85 >= pR >= 0 and 100 >= pG >= 20 and 100 >= pB >= 20:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 30
            pc[i, j] = pixel
            # BLUE
        elif 50 >= pR >= 0 and 50 >= pG >= 0 and 100 >= pB >= 5:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 6
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 25
            pb[i, j] = pixel
            # BLACK
        elif pR == 0 and pG == 0 and pB == 0:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 6
            pbl[i, j] = pixel
        else:
            pe[i, j] = pixel
### Plot the clasification 
plt.figure(figsize=(12, 6))

# plt.subplot(3, 3, 1)
# plt.title('BROWN CHANNEL')
# plt.imshow(pbr, cmap='gray')

plt.subplot(3, 3, 2)
plt.title('RED, YELLOW AND ORANGE CHANNEL')
plt.imshow(pr, cmap='gray')

# plt.subplot(3, 3, 3)
# plt.title('ORANGE CHANNEL')
# plt.imshow(po, cmap='gray')

# plt.subplot(3, 3, 4)
# plt.title('YELLOW CHANNEL')
# plt.imshow(py, cmap='gray')

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

#------TO REDUCE THE MODEL
mesh.points [:,0] /= 3
mesh.points [:,1] /= 3
mesh.points[:,2] /= 3

#------TO INCREASE THE MODEL
# mesh.points [:,0] *= 5
# mesh.points [:,1] *= 5
# mesh.points[:,2] *= 5

### Show the strcucture
p = pv.Plotter()
p.add_mesh(mesh, color="gray")
p.show()

### Export the model to stl 
polydata = mesh.extract_geometry()
stl_file = 'wmapp.stl'
polydata.save(stl_file)
print("se guardo la imagen como: ", stl_file)
