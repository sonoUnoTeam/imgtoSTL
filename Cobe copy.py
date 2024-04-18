import cv2
import numpy as np
import pyvista as pv
from pyvista import StructuredGrid
import matplotlib.pyplot as plt


# Add the image to process
imagen_original = cv2.imread('cobe.png')
imgresize = cv2.resize(imagen_original, (1280,720))
cv2.imshow('imagen',imgresize)
cv2.waitKey(0)
imagen_rgb = cv2.cvtColor(imgresize, cv2.COLOR_BGR2RGB)
# Extract image matrix
matriz = np.asarray(imagen_rgb)
h, w, c = matriz.shape


pr = np.zeros((h, w, c), dtype=np.uint8)
pp = np.zeros((h, w, c), dtype=np.uint8)
py = np.zeros((h, w, c), dtype=np.uint8)
pg = np.zeros((h, w, c), dtype=np.uint8)
pc = np.zeros((h, w, c), dtype=np.uint8)
pb = np.zeros((h, w, c), dtype=np.uint8)
pbl = np.zeros((h, w, c), dtype=np.uint8)
pw = np.zeros((h, w, c), dtype=np.uint8)
pe = np.zeros((h, w, c), dtype=np.uint8)
pbr = np.zeros((h, w, c), dtype=np.uint8)
po = np.zeros((h, w, c), dtype=np.uint8)
pvi = np.zeros((h, w, c), dtype=np.uint8)
x = np.zeros((h, w))
y = np.zeros((h, w))
z = np.zeros((h,w))
zr = np.zeros((h, w))
zb = np.zeros((h, w))
zg = np.zeros((h, w))
zp = np.zeros((h, w))
zc = np.zeros((h, w))
zbl = np.zeros((h, w))
zy = np.zeros((h, w))
zw = np.zeros((h, w))
zbr = np.zeros((h, w))
zo = np.zeros((h, w))
zv = np.zeros((h, w))

#-----------------------Clasificacion para COBE CELESTE (canales cyan,azul,amarillo,violeta y negro)
for i in range(h):
    for j in range(w):
        pixel = imagen_rgb[i, j]
        r, g, b = pixel
        # Calcula el porcentaje de color rojo
        pR = r / 255.0 * 100  # PORCENTAJE DE ROJO
        pB = b / 255.0 * 100   # PORCENTAJE DE AZUL
        pG = g / 255.0 * 100  # PORCENTAJE DE VERDE
        #Amarillo Claro
        if 80 >= pR >= 40 and 100 >= pG >= 70 and 85 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 50
            py[i, j] = pixel
        # Amarillo
        elif 100 >= pR >= 70 and 100 >= pG >= 60 and 35 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 49
            py[i, j] = pixel
            # Amarillo Oscuro
        elif 80 >= pR >= 60 and 80 >= pG >= 60 and 50 >= pB >= 10:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 48
            py[i, j] = pixel
            # Verde Claro
        elif 5 >= pR >= 0 and 85 >= pG >= 70 and 85 >= pB >= 50:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 47
            pg[i, j] = pixel
            # Verde
        elif 70 >= pR >= 0 and 100 >= pG >= 60 and 50 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 46
            pg[i, j] = pixel
            # Verde Oscuro
        elif 75 >= pR >= 0 and 75 >= pG >= 30 and 45 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 45
            pg[i, j] = pixel
            # Violeta 
        elif 25 >= pR >= 10 and 12 >= pG >= 5 and 50 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 39
            pvi[i, j] = pixel
            # Azul Claro
        elif 50 >= pR >= 0 and 50 >= pG >= 0 and 100 >= pB >= 5:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 42
            pb[i, j] = pixel
            # azul
        elif 45 >= pR >= 0 and 25 >= pG >= 0 and 100 >= pB >= 5:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 41
            pb[i, j] = pixel
            # Azul Oscuro
        elif 35 >= pR >= 0 and 25 >= pG >= 0 and 65 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
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
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 45
            pc[i, j] = pixel
            # Cian
        elif 30 >= pR >= 0 and 100 >= pG >= 40 and 100 >= pB >= 40:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 8
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
                z[i, j] = 8
            else:
                x[i, j] = j
                y[i, j] = i
                z[i, j] = 43
            pc[i, j] = pixel
        # Negro
        elif pR == 0 and pG == 0 and pB == 0:
            x[i, j] = j
            y[i, j] = i
            z[i, j] = 8
            pbl[i, j] = pixel
        else:
            pe[i, j] = pixel

plt.figure(figsize=(12, 6))

plt.subplot(3, 3, 1)
plt.title('Canal Marron')
plt.imshow(pbr, cmap='gray')

plt.subplot(3, 3, 2)
plt.title('Canal Rojo')
plt.imshow(pr, cmap='gray')

plt.subplot(3, 3, 3)
plt.title('Canal Naranja')
plt.imshow(po, cmap='gray')

plt.subplot(3, 3, 4)
plt.title('Canal Yellow')
plt.imshow(py, cmap='gray')

plt.subplot(3, 3, 5)
plt.title('Canal Verde')
plt.imshow(pg, cmap='gray')

plt.subplot(3, 3, 6)
plt.title('Canal Cyan')
plt.imshow(pc, cmap='gray')

plt.subplot(3, 3, 7)
plt.title('Canal Azul')
plt.imshow(pb, cmap='gray')

plt.subplot(3, 3, 8)
plt.title('Canal Blanco')
plt.imshow(pw, cmap='gray')

plt.subplot(3, 3, 9)
plt.title('EXTRA')
plt.imshow(pe, cmap='gray')
plt.show()

x_base, y_base = np.meshgrid(range(w), range(h))
z_base = np.zeros_like(x_base)
x = np.stack((x_base, x), axis=0)
y = np.stack((y_base, y), axis=0)
z = np.stack((z_base, z), axis=0)

# Creamos la estructura
mesh = pv.StructuredGrid(-x, y, z)
mesh.points /= 10
# mesh_clean.points [:,0] *= 0.28
# mesh_clean.points [:,1] *= 0.28
# mesh_clean.points[:,2] *= 0.10
# ----------- Visualice the mesh
p = pv.Plotter()
p.add_mesh(mesh, color='lightblue')
p.show()


polydata = mesh.extract_geometry()
stl_file = 'cobe1280x720.stl'
polydata.save(stl_file)
print("se guardo la imagen como: ", stl_file)
