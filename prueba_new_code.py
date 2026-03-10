import cv2
import numpy as np
import pyvista as pv
from pyvista import StructuredGrid
import matplotlib.pyplot as plt


### Add the image to process
img_original = cv2.imread(r'C:\Users\cotif\Documents\GitHub\imgtoSTL\imgs\-helix-nebula.png')

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
### -----------------Clasificacion nebula helix-------------------------------------------
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
            z[i, j] = 30
            pbl[i, j] = pixel
        #BLANCO
        elif 25 <= pR <= 40 and 25 <= pG <= 40 and 25 <= pB <= 40:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 50
            pw[i, j] = pixel
        #ROJO
        elif pR >= 50 and pG <= 30 and pB <= 30:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 33
            pr[i, j] = pixel
        
        #CIAN
        elif pR <= 21 and pG >= 33 and pB >= 39 and abs(pG - pB) <= 20:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 46
            pc[i, j] = pixel
        #AZUL
        elif pB >= 15 and pR <= 35 and pG <= 53:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 53
            pb[i, j] = pixel
        #VERDE
        elif pG >= 38 and pR >= 35 and pB <= 25 and pG >= pR:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 43
            pg[i, j] = pixel
        #AMARILLO
        elif pR >= 35 and pG >= 35 and pB <= 20:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 40
            py[i, j] = pixel
        #VIOLETA
        elif pR >= 40 and pB >= 20 and pG <= 30:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 56
            pvi[i, j] = pixel
        #NARANJA
        elif pR >= 35 and 20 <= pG <= 40 and pB <= 35:
            x[i, j] = j
            y[i, j] = i 
            z[i, j] = 36
            po[i, j] = pixel  
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
p.add_mesh(mesh, color="lightgreen")
p.show()

# ### Export the model to stl 
polydata = mesh.extract_geometry()
stl_file = 'helixnebula.stl'
polydata.save(stl_file)
print("se guardo la imagen como: ", stl_file)
