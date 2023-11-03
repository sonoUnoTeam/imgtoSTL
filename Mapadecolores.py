import cv2
import numpy as np
import pyvista as pv
from pyvista import StructuredGrid
import matplotlib.pyplot as plt
'''
# Tamaño de la imagen
width, height = 400, 400

# Crear una imagen con fondo negro
pixels = np.zeros((height, width, 3), dtype=np.uint8)  # Fondo negro

# Número de tiras de colores
num_tiras = 8
strip_width = width // num_tiras

# Color de cada tira
colors = [
    (255, 255, 255),  # Blanco
    (255, 0, 0),      # Rojo
    (255, 0, 255),    # Magenta
    (255, 255, 0),    # Amarillo
    (0, 255, 0),      # Verde
    (0, 255, 255),    # Cyan
    (0, 0, 255),      # Azul
    (0, 0, 0)         # Negro
]
espacio = 1
for i in range(num_tiras):
    start_x = i * (strip_width + espacio)
    end_x = (i + 1) * strip_width + i * espacio

    for x in range(start_x, end_x):
        if x < width:  # Asegurarse de que no se salga de los límites de la imagen
            pixels[:, x] = colors[i]  # Color de la tira
plt.imshow(pixels)
plt.show()
# Guardo las imágenes
plt.imsave("imagen_referencia.png", pixels)'''

# ---------Extraccion de canales y asignacion de alturas----

# Cargo imagen creada
imagen_original = cv2.imread('imagen_referencia.png')
imagen_rgb = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
matriz = np.asarray(imagen_rgb)
h, w, c = matriz.shape
# Creo matrices para los pixeles
pr = np.zeros((h, w, c), dtype=np.uint8)
pp = np.zeros((h, w, c), dtype=np.uint8)
py = np.zeros((h, w, c), dtype=np.uint8)
pg = np.zeros((h, w, c), dtype=np.uint8)
pc = np.zeros((h, w, c), dtype=np.uint8)
pb = np.zeros((h, w, c), dtype=np.uint8)
pbl = np.zeros((h, w, c), dtype=np.uint8)
pw = np.zeros((h, w, c), dtype=np.uint8)

'''
     R  G  B
W = [X, X, X] Blanco
R = [X, 0, 0] Rojo
M = [X, 0, X] Rojo + Azul
A = [X, X, 0] Rojo + Verde
G = [0, X, 0] Verde
C = [0, X, X] Azul + Verde
B = [0, 0, X] Azul
Bl = [0, 0, 0] Negro
'''
# Recorremos la matriz de la imagen y extraigo los pixeles por color
for i in range(h):
    for j in range(w):
        pixel = matriz[i, j]
        if pixel[0] > 0 and pixel[1] == 0 and pixel[2] == 0:
            pr[i, j] = pixel
        elif pixel[0] > 0 and pixel[1] == 0 and pixel[2] > 0:
            pp[i, j] = pixel
        elif pixel[0] > 0 and pixel[1] > 0 and pixel[2] == 0:
            py[i, j] = pixel
        elif pixel[0] == 0 and pixel[1] > 0 and pixel[2] == 0:
            pg[i, j] = pixel
        elif pixel[0] == 0 and pixel[1] > 0 and pixel[2] > 0:
            pc[i, j] = pixel
        elif pixel[0] == 0 and pixel[1] == 0 and pixel[2] > 0:
            pb[i, j] = pixel
        elif pixel[0] > 0 and pixel[1] > 0 and pixel[2] > 0:
            pw[i, j] = pixel
        elif pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            pbl[i, j] = pixel
'''
# Muestra los canales
plt.figure(figsize=(12, 6))

plt.subplot(2, 4, 1)
plt.title('Canal Azul')
plt.imshow(pb, cmap='gray')

plt.subplot(2, 4, 2)
plt.title('Canal Verde')
plt.imshow(pg, cmap='gray')

plt.subplot(2, 4, 3)
plt.title('Canal Rojo')
plt.imshow(pr, cmap='gray')

plt.subplot(2, 4, 4)
plt.title('Canal Pink')
plt.imshow(pp, cmap='gray')

plt.subplot(2, 4, 5)
plt.title('Canal Cyan')
plt.imshow(pc, cmap='gray')

plt.subplot(2, 4, 6)
plt.title('Canal Yellow')
plt.imshow(py, cmap='gray')

plt.subplot(2, 4, 7)
plt.title('Blanco')
plt.imshow(pw, cmap='gray')

plt.subplot(2, 4, 8)
plt.title('Negro')
plt.imshow(pbl, cmap='gray')

plt.show()'''

# ------------------------Representacion en 3D
# pasamos las imagens a blanco y negro
irg = cv2.cvtColor(pr, cv2.COLOR_BGR2GRAY)
iyg = cv2.cvtColor(py, cv2.COLOR_BGR2GRAY)
ipg = cv2.cvtColor(pp, cv2.COLOR_BGR2GRAY)
igg = cv2.cvtColor(pg, cv2.COLOR_BGR2GRAY)
icg = cv2.cvtColor(pc, cv2.COLOR_BGR2GRAY)
ibg = cv2.cvtColor(pb, cv2.COLOR_BGR2GRAY)
iwg = cv2.cvtColor(pw, cv2.COLOR_BGR2GRAY)
iblg = cv2.cvtColor(pbl, cv2.COLOR_BGR2GRAY)

hr, wr = irg.shape
hb, wb = ibg.shape
hg, wg = igg.shape
hp, wp = ipg.shape
hc, wc = icg.shape
hy, wy = iyg.shape
hw, ww = iwg.shape
hbl, wbl = iblg.shape

xr = np.zeros((hr, wr))
yr = np.zeros((hr, wr))
zr = np.zeros((hr, wr))

xb = np.zeros((hb, wb))
yb = np.zeros((hb, wb))
zb = np.zeros((hb, wb))

xg = np.zeros((hg, wg))
yg = np.zeros((hg, wg))
zg = np.zeros((hg, wg))

xp = np.zeros((hp, wp))
yp = np.zeros((hp, wp))
zp = np.zeros((hp, wp))

xc = np.zeros((hc, wc))
yc = np.zeros((hc, wc))
zc = np.zeros((hc, wc))

xy = np.zeros((hy, wy))
yy = np.zeros((hy, wy))
zy = np.zeros((hy, wy))

xw = np.zeros((hw, ww))
yw = np.zeros((hw, ww))
zw = np.zeros((hw, ww))

xbl = np.zeros((hbl, wbl))
ybl = np.zeros((hbl, wbl))
zbl = np.zeros((hbl, wbl))

maxW = np.max(pw)
minW = np.min(pw)
maxR = np.max(pr)
minR = np.min(pr)
maxY = np.max(py)
minY = np.min(py)
maxG = np.max(pg)
minG = np.min(pg)
maxP = np.max(pp)
minP = np.min(pp)
maxB = np.max(pb)
minB = np.min(pb)
maxC = np.max(pc)
minC = np.min(pc)
maxBl = np.max(pbl)
minBl = np.min(pbl)
# Blanco
for i in range(hw):
    for j in range(ww):
        pix = (iwg[i, j]-minW)/(maxW-minW)
        xw[i, j] = j  # Coordenada X0
        yw[i, j] = i  # Coordenada Y
        zw[i, j] = (pix * 32)

# Altura para Rojo

for i in range(hr):
    for j in range(wr):
        pix = (irg[i, j]-minR)/(maxR-minR)
        xr[i, j] = j  # Coordenada X0
        yr[i, j] = i  # Coordenada Y
        if pix != 0:
            zr[i, j] = (pix * 28) + 25
        else:
            zr[i, j] = (pix * 0)
# Altura para Magenta
for i in range(hp):
    for j in range(wp):
        pix = ((ipg[i, j]-minP))/(maxP-minP)
        xp[i, j] = j  # Coordenada X0
        yp[i, j] = i  # Coordenada Y
        if pix != 0:
            zp[i, j] = (pix * 20) + 15
        else:
            zp[i, j] = (pix * 0)
print(maxP)
# Altura para Amarillo
for i in range(hy):
    for j in range(wy):
        pix = ((iyg[i, j]-minY))/(maxY-minY)
        xy[i, j] = j  # Coordenada X0
        yy[i, j] = i  # Coordenada Y
        if pix != 0:
            zy[i, j] = (pix * 10) + 10
        else:
            zy[i, j] = (pix * 0)
# Altura para Verde
for i in range(hg):
    for j in range(wg):
        pix = ((igg[i, j]-minG))/(maxG-minG)
        xg[i, j] = j  # Coordenada X0
        yg[i, j] = i  # Coordenada Y
        if pix != 0:
            zg[i, j] = (pix * 12) + 5
        else:
            zg[i, j] = (pix * 0)
# Altura para Cyan
for i in range(hc):
    for j in range(wc):
        pix = ((icg[i, j]-minC))/(maxC-minC)
        xc[i, j] = j  # Coordenada X0
        yc[i, j] = i  # Coordenada Y
        if pix != 0:
            zc[i, j] = (pix * 10) + 1
        else:
            zc[i, j] = (pix * 0)

# Altura para Azul
for i in range(hb):
    for j in range(wb):
        pix = ((ibg[i, j]-minB))/(maxB-minB)
        xb[i, j] = j  # Coordenada X0
        yb[i, j] = i  # Coordenada Y
        if pix != 0:
            zb[i, j] = (pix * 8)
        else:
            zb[i, j] = (pix * 0)
# Altura para Negro
for i in range(hbl):
    for j in range(wbl):
        pix = iblg[i, j]
        xbl[i, j] = j  # Coordenada X0
        ybl[i, j] = i  # Coordenada Y
        zbl[i, j] = (pix * 0)
# Base
x_base, y_base = np.meshgrid(range(hbl), range(hbl))
z_base = np.zeros_like(x_base)

xwb = np.stack((xw, x_base), axis=0)
ywb = np.stack((yw, y_base), axis=0)
zwb = np.stack((zw, z_base), axis=0)

xrb = np.stack((xr, x_base), axis=0)
yrb = np.stack((yr, y_base), axis=0)
zrb = np.stack((zr, z_base), axis=0)

xpb = np.stack((xp, x_base), axis=0)
ypb = np.stack((yp, y_base), axis=0)
zpb = np.stack((zp, z_base), axis=0)

xyb = np.stack((xy, x_base), axis=0)
yyb = np.stack((yy, y_base), axis=0)
zyb = np.stack((zy, z_base), axis=0)

xgb = np.stack((xg, x_base), axis=0)
ygb = np.stack((yg, y_base), axis=0)
zgb = np.stack((zg, z_base), axis=0)

xcb = np.stack((xc, x_base), axis=0)
ycb = np.stack((yc, y_base), axis=0)
zcb = np.stack((zc, z_base), axis=0)

xbb = np.stack((xb, x_base), axis=0)
ybb = np.stack((yb, y_base), axis=0)
zbb = np.stack((zb, z_base), axis=0)

xblb = np.stack((xbl, x_base), axis=0)
yblb = np.stack((ybl, y_base), axis=0)
zblb = np.stack((zbl, z_base), axis=0)
# unimos los puntos
meshw = StructuredGrid(xwb, ywb, zwb)
meshr = StructuredGrid(xrb, yrb, zrb)
meshp = StructuredGrid(xpb, ypb, zpb)
meshy = StructuredGrid(xyb, yyb, zyb)
meshg = StructuredGrid(xgb, ygb, zgb)
meshc = StructuredGrid(xcb, ycb, zcb)
meshb = StructuredGrid(xbb, ybb, zbb)
meshbl = StructuredGrid(xblb, yblb, zblb)
mesht = meshw + meshr + meshp + meshy + meshg + meshc + meshb + meshbl
# Visualiza la malla combinada
p = pv.Plotter()
p.add_floor(face='-z', i_resolution=400, j_resolution=400, color='black', line_width=None, opacity=2.0)
'''p.add_mesh(meshw, color="white")
p.add_mesh(meshr, color="red")
p.add_mesh(meshp, color="pink")
p.add_mesh(meshy, color="yellow")
p.add_mesh(meshg, color="green")
p.add_mesh(meshc, color="lightblue")
p.add_mesh(meshb, color="blue")
p.add_mesh(meshbl, color="black")'''
p.add_mesh(mesht, color='lightblue')
p.add_floor()
p.show()
polydata = mesht.extract_geometry()
stl_file = 'mapa.stl'
polydata.save(stl_file)
print("guardado")
