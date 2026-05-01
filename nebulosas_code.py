import cv2
import numpy as np
import pyvista as pv
from pyvista import StructuredGrid
import matplotlib.pyplot as plt
from pathlib import Path


### Add the image to process
path_img = r'C:\Users\cotif\Documents\GitHub\imgtoSTL\imgs\nebulosa3.jpeg'
# Reduce image
img_original = cv2.imread(path_img)
escala = 0.5
img_original = cv2.resize(img_original, (0,0), fx=escala, fy=escala)
### Converto BGR to RGB 
imagen_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
### Extract image matrix
matriz = np.asarray(imagen_rgb)
h, w, c = matriz.shape

### Create empty matrix for each color
pr = np.zeros((h, w, c), dtype=np.uint8) #Red
py = np.zeros((h, w, c), dtype=np.uint8) #Yellow
pg = np.zeros((h, w, c), dtype=np.uint8) #Green
pc = np.zeros((h, w, c), dtype=np.uint8) #Cyan
pb = np.zeros((h, w, c), dtype=np.uint8) #Blue
pbl = np.zeros((h, w, c), dtype=np.uint8) #Black
pw = np.zeros((h, w, c), dtype=np.uint8)  #White
pe = np.zeros((h, w, c), dtype=np.uint8)  #Extra
po = np.zeros((h, w, c), dtype=np.uint8)  #Orange
pvi = np.zeros((h, w, c), dtype=np.uint8) #Violet
### Create matrix to store positions 
x = np.zeros((h, w))
y = np.zeros((h, w))
z = np.zeros((h,w))
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
        # BLACK
        if total == 0:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 6
            pbl[i, j] = pixel
        #WHITE
        elif 25 <= pR <= 40 and 25 <= pG <= 40 and 25 <= pB <= 40:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 55
            pw[i, j] = pixel
        #RED
        elif pR >= 50 and pG <= 30 and pB <= 30:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 30
            pr[i, j] = pixel
        #CYAN
        elif pR <= 21 and pG >= 33 and pB >= 39 and abs(pG - pB) <= 20:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 60
            pc[i, j] = pixel
        #BLUE
        elif pB >= 15 and pR <= 35 and pG <= 53:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 65
            pb[i, j] = pixel
        
        #YELLOW
        elif pR >= 35 and pG >= 35 and pB <= 20:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 45
            py[i, j] = pixel
        
        #PURPLE
        elif pR >= 30 and pB >= 20 and pG <= 40:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 70
            pvi[i, j] = pixel
        #ORANGE
        elif pR >= 35 and 20 <= pG <= 40 and pB <= 35:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 40
            po[i, j] = pixel  
        #GREEN
        elif pR >= 0 and pB <= 75 and pG >= 10:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 50
            pg[i, j] = pixel
        
        #EXTRA
        else:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 6
            pe[i, j] = pixel


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
plt.title('EXTRA')
plt.imshow(pe, cmap='gray')
plt.show()



### Create a base for the model 
x_base, y_base = np.meshgrid(range(w), range(h))
z_base = np.full_like(x_base, -5) # Sugerencia: Una base un poco por debajo de 0

### Merge base values and pixels
x = np.stack((x_base, x), axis=0)
y = np.stack((y_base, y), axis=0)
z = np.stack((z_base, z), axis=0)
### Create the structure


mesh = pv.StructuredGrid(-x, y, z)

### Dimension the mesh
scale = 170.33 / 1087  

mesh.points[:, 0] *= scale
mesh.points[:, 1] *= scale
mesh.points[:, 2] *= scale
polydata = mesh.extract_geometry()
# Smooth the 3D model 
smoothed = polydata.smooth(
    n_iter=500,
    relaxation_factor=0.01,
    boundary_smoothing= False,   # Dont process edges models = FALSE
    feature_smoothing= False,     # Keep sharp edges = False
    feature_angle= 45       # Angle from which an "edge" is considered
)

### Show model
p = pv.Plotter()
p.add_mesh(smoothed, color="gray")
p.show()

### Export smooth model
name_base = Path(path_img).stem
stl_file = f"{name_base}_1.stl"
smoothed.save(stl_file)
print("Saved as:", stl_file)
