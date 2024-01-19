import cv2
import numpy as np
import pyvista as pv
from pyvista import StructuredGrid
import matplotlib.pyplot as plt


# Add the image to process
imagen_original = cv2.imread('WMAP.jpg')
imagen_rgb = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
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
x = np.zeros((h, w))
y = np.zeros((h, w))
xr = np.zeros((h, w))
yr = np.zeros((h, w))
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
for i in range(h):
    for j in range(w):
        pixel = imagen_rgb[i, j]
        r, g, b = pixel
        # Calcula el porcentaje de color rojo
        pR = r / 255.0 * 100  # PORCENTAJE DE ROJO
        pB = b / 255.0 * 100   # PORCENTAJE DE AZUL
        pG = g / 255.0 * 100  # PORCENTAJE DE VERDE
        # Blanco
        if pR == 100 and pG == 100 and pB == 100:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zw[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zw[i, j] = 100
            pw[i, j] = pixel
        # Rojo Claro
        if 100 >= pR >= 20 and 30 >= pG >= 0 and 50 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zr[i, j] = 90
            # Rojo
        elif 100 >= pR >= 20 and 25 >= pG >= 0 and 30 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zr[i, j] = 80
            # Rojo Oscuro
        elif 70 >= pR >= 20 and 25 >= pG >= 0 and 10 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zr[i, j] = 70
            # Verde Claro
        elif 80 >= pR >= 40 and 100 >= pG >= 70 and 85 >= pB >= 15:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zg[i, j] = 40
            pg[i, j] = pixel
            # Verde
        elif 70 >= pR >= 0 and 100 >= pG >= 60 and 50 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zg[i, j] = 30
            pg[i, j] = pixel
            # Verde Oscuro
        elif 75 >= pR >= 0 and 75 >= pG >= 50 and 45 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zg[i, j] = 20
            pg[i, j] = pixel
            # Azul Claro
        elif 50 >= pR >= 0 and 50 >= pG >= 0 and 100 >= pB >= 5:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zb[i, j] = 15
            pb[i, j] = pixel
            # azul
        elif 45 >= pR >= 0 and 25 >= pG >= 0 and 100 >= pB >= 5:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zb[i, j] = 10
            pb[i, j] = pixel
            # Azul Oscuro
        elif 35 >= pR >= 0 and 25 >= pG >= 0 and 65 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zb[i, j] = 10
            pb[i, j] = pixel
            # Magenta Claro
        elif 100 >= pR >= 70 and 40 >= pG >= 15 and 100 >= pB >= 70:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zp[i, j] = 50
            pp[i, j] = pixel
            # Magenta
        elif 100 >= pR >= 80 and 30 >= pG >= 0 and 100 >= pB >= 80:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zp[i, j] = 60
            pp[i, j] = pixel
            # Magenta Oscuro
        elif 100 >= pR >= 30 and 30 >= pG >= 0 and 100 >= pB >= 30:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zp[i, j] = 65
            pp[i, j] = pixel
            # Cian Claro
        elif 65 >= pR >= 0 and 100 >= pG >= 50 and 100 >= pB >= 50:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zc[i, j] = 20
            pc[i, j] = pixel
            # Cian
        elif 30 >= pR >= 0 and 100 >= pG >= 40 and 100 >= pB >= 40:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zc[i, j] = 30
            pc[i, j] = pixel
            # Cian Oscuro
        elif 40 >= pR >= 0 and 50 >= pG >= 20 and 50 >= pB >= 20:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zc[i, j] = 40
            pc[i, j] = pixel
            # Amarillo claro
        elif 100 >= pR >= 80 and 100 >= pG >= 60 and 70 >= pB >= 20:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zy[i, j] = 70
            py[i, j] = pixel
        # Amarillo
        elif 100 >= pR >= 70 and 100 >= pG >= 60 and 35 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zy[i, j] = 50
            py[i, j] = pixel
            # Amarillo Oscuro
        elif 80 >= pR >= 60 and 80 >= pG >= 60 and 50 >= pB >= 10:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zy[i, j] = 40
            py[i, j] = pixel
        # Marron Claro
        elif 100 >= pR >= 50 and 60 >= pG >= 40 and 40 >= pB >= 10:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zbr[i, j] = 40
            pbr[i, j] = pixel
        # Marron
        elif 80 >= pR >= 50 and 60 >= pG >= 35 and 10 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zbr[i, j] = 40
            pbr[i, j] = pixel
        # Marron Oscuro
        elif 65 >= pR >= 30 and 55 >= pG >= 15 and 30 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zbr[i, j] = 40
            pbr[i, j] = pixel
        # Naranja Claro
        elif 100 >= pR >= 65 and 65 >= pG >= 30 and 35 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zo[i, j] = 40
            po[i, j] = pixel
        # Naranja Medio
        elif 85 >= pR >= 55 and 45 >= pG >= 20 and 20 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zo[i, j] = 40
            po[i, j] = pixel
        # Naranja Oscuro
        elif 90 >= pR >= 55 and 45 >= pG >= 25 and 15 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zo[i, j] = 40
            po[i, j] = pixel
            # Negro
        elif pR == 0 and pG == 0 and pB == 0:
            x[i, j] = j
            y[i, j] = i
            zbl[i, j] = 10
            pbl[i, j] = pixel
        else:
            pe[i, j] = pixel


plt.figure(figsize=(12, 6))

plt.subplot(3, 3, 1)
plt.title('Canal Azul')
plt.imshow(pb, cmap='gray')

plt.subplot(3, 3, 2)
plt.title('Canal Verde')
plt.imshow(pg, cmap='gray')

plt.subplot(3, 3, 3)
plt.title('Canal Rojo')
plt.imshow(pr, cmap='gray')

plt.subplot(3, 3, 4)
plt.title('Canal Magenta')
plt.imshow(pp, cmap='gray')

plt.subplot(3, 3, 5)
plt.title('Canal Cyan')
plt.imshow(pc, cmap='gray')

plt.subplot(3, 3, 6)
plt.title('Canal Yellow')
plt.imshow(py, cmap='gray')

plt.subplot(3, 3, 7)
plt.title('Naranja')
plt.imshow(po, cmap='gray')

plt.subplot(3, 3, 8)
plt.title('Canal Marron')
plt.imshow(pbr, cmap='gray')

plt.subplot(3, 3, 9)
plt.title('EXTRA')
plt.imshow(pe, cmap='gray')
plt.show()

# x_base, y_base = np.meshgrid(range(w), range(h))
# z_base = np.zeros_like(x_base)

# xi = np.stack((x_base, x), axis=0)
# yi = np.stack((y_base, y), axis=0)
# zbll = np.stack((z_base, zbl), axis=0)
# zrr = np.stack((z_base, zr), axis=0)
# zcc = np.stack((z_base, zc), axis=0)
# zpp = np.stack((z_base, zp), axis=0)
# zbb = np.stack((z_base, zb), axis=0)
# zgb = np.stack((z_base, zg), axis=0)
# zyy = np.stack((z_base, zy), axis=0)
# zww = np.stack((z_base, zw), axis=0)
# meshr = StructuredGrid(-xi, yi, zrr)  # mesh red
# meshp = StructuredGrid(-xi, yi, zpp)  # mesh magenta
# meshg = StructuredGrid(-xi, yi, zgb)  # mesh green
# meshc = StructuredGrid(-xi, yi, zcc)  # mesh cyan
# meshb = StructuredGrid(-xi, yi, zbb)  # mesh blue
# meshbl = StructuredGrid(-xi, yi, zbll)  # mesh black
# meshy = StructuredGrid(-xi, yi, zyy)  # mesh yellow
# meshw = StructuredGrid(-xi, yi, zww) # mesh white
# base = StructuredGrid(-x_base, y_base, zbl)
# mesht = pv.merge([meshw, meshr, meshb, meshy, meshp, meshc, meshg, meshbl, base]) # Add mesh
# mesh_clean = mesht.clean()
# mesh_clean.points /= 10

# ----------- Visualice the mesh
# p = pv.Plotter()
# p.add_floor(face='-z', i_resolution=400, j_resolution=400, color='black',
#             line_width=None, opacity=2.0)
# p.add_mesh(meshw, color="white")
# p.add_mesh(meshr, color="red")
# p.add_mesh(meshp, color="magenta")
# p.add_mesh(meshy, color="yellow")
# p.add_mesh(meshg, color="green")
# p.add_mesh(meshc, color="cyan")
# p.add_mesh(meshb, color="blue")
# p.add_mesh(meshbl, color="black")
# p.add_mesh(mesh_clean, color='lightblue')
# p.add_floor()
# p.show()


# polydata = mesh_clean.extract_geometry()
# stl_file = 'cobe1.stl'
# polydata.save(stl_file)
# print("se guardo la imagen como: ", stl_file)
