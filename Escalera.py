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
espacio = 2
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
imagen_original = cv2.imread("COBE_1.png")   # cambiar para las distintas imagenes
imagen_rgb = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
matriz = np.asarray(imagen_rgb)
h, w, c = matriz.shape

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
pr = np.zeros((h, w, c), dtype=np.uint8)
pp = np.zeros((h, w, c), dtype=np.uint8)
py = np.zeros((h, w, c), dtype=np.uint8)
pg = np.zeros((h, w, c), dtype=np.uint8)
pc = np.zeros((h, w, c), dtype=np.uint8)
pb = np.zeros((h, w, c), dtype=np.uint8)
pbl = np.zeros((h, w, c), dtype=np.uint8)
pw = np.zeros((h, w, c), dtype=np.uint8)
pe = np.zeros((h, w, c), dtype=np.uint8)
x = np.zeros((h, w))
y = np.zeros((h, w))

xr = np.zeros((h, w))
yr = np.zeros((h, w))
zr = np.zeros((h, w))


xb = np.zeros((h, w))
yb = np.zeros((h, w))
zb = np.zeros((h, w))


xg = np.zeros((h, w))
yg = np.zeros((h, w))
zg = np.zeros((h, w))


xp = np.zeros((h, w))
yp = np.zeros((h, w))
zp = np.zeros((h, w))


xc = np.zeros((h, w))
yc = np.zeros((h, w))
zc = np.zeros((h, w))


xy = np.zeros((h, w))
yy = np.zeros((h, w))
zy = np.zeros((h, w))


xw = np.zeros((h, w))
yw = np.zeros((h, w))
zw = np.zeros((h, w))


xbl = np.zeros((h, w))
ybl = np.zeros((h, w))
zbl = np.zeros((h, w))
for i in range(h):
    for j in range(w):
        pixel = imagen_rgb[i, j]
        r, g, b = pixel
        # Calcula el porcentaje de color rojo
        pR = r / 255.0 * 100  # PORCENTAJE DE ROJO
        pB = b / 255.0 * 100   # PORCENTAJE DE AZUL
        pG = g / 255.0 * 100  # PORCENTAJE DE VERDE
        promedio = sum(pixel) / len(pixel)
        # Blanco
        if pR == 100 and pG == 100 and pB == 100:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zw[i, j] = 20
            else:
                x[i, j] = j
                y[i, j] = i
                zw[i, j] = 100
            pw[i, j] = pixel
        # Rojo Claro
        if 100 >= pR and 10 >= pG >= 0 and 50 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0]==0 and pixel[1]==0 and pixel[2]==0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zr[i, j] = 90
            
            # Rojo
        elif 100 >= pR and 10 >= pG >= 0 and 30 >= pB >= 0:
            pr[i, j] = pixel
            if pixel[0]==0 and pixel[1]==0 and pixel[2]==0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zr[i, j] = 80
            # Rojo Oscuro
        elif 50 >= pR >= 10 and 5 >= pG >= 0 and 10 >= pB >= 0:
            
            pr[i, j] = pixel
            if pixel[0]==0 and pixel[1]==0 and pixel[2]==0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zr[i, j] = 70
            # Verde Claro
        elif 40 >= pR >= 5 and 100 >= pG >= 70 and 40 >= pB >= 5:
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
        elif 5 >= pR >= 0 and 100 >= pG >= 70 and 5 >= pB >= 0:
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
        elif 10 >= pR >= 0 and 50 >= pG >= 10 and 5 >= pB >= 0:
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
        elif 35 >= pR >= 0 and 40 >= pG >= 0 and 100 >= pB >= 80:
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
        elif 10 >= pR >= 0 and 10 >= pG >= 0 and 100 >= pB >= 80:
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
        elif 10 >= pR >= 0 and 10 >= pG >= 0 and 50 >= pB >= 30:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zb[i, j] = 8
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
        elif 100 >= pR >= 30 and 30 >= pG >= 0 and 100 >= pB >= 30:
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
        elif 80 >= pR >= 30 and 30 >= pG >= 0 and 100 >= pB >= 30:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zp[i, j] = 70
            pp[i, j] = pixel
            # Cian Claro
        elif 50 >= pR >= 0 and 100 >= pG >= 50 and 100 >= pB >= 50:
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
            #Amarillo claro
        elif 100 >= pR >= 80 and 100 >= pG >= 80 and 60 >= pB >= 30:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zy[i, j] = 70
            py[i, j] = pixel
           #Amarillo 
        elif 100 >= pR >= 80 and 100 >= pG >= 80 and 20 >= pB >= 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 10
            else:
                x[i, j] = j
                y[i, j] = i
                zy[i, j] = 50
            py[i, j] = pixel
            #Amarillo Oscuro
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
            #Negro
        elif pR == 0 and pG == 0 and pB == 0:
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 30
            else:
                x[i, j] = j
                y[i, j] = i
                zbl[i, j] = 30
            pbl[i, j] = pixel
        else:
            pe[i,j]=pixel

# Muestra los canales
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
plt.title('Canal Pink')
plt.imshow(pp, cmap='gray')

plt.subplot(3, 3, 5)
plt.title('Canal Cyan')
plt.imshow(pc, cmap='gray')

plt.subplot(3,3, 6)
plt.title('Canal Yellow')
plt.imshow(py, cmap='gray')

plt.subplot(3, 3, 7)
plt.title('Blanco')
plt.imshow(pw, cmap='gray')

plt.subplot(3, 3, 8)
plt.title('Negro')
plt.imshow(pbl, cmap='gray')

plt.subplot(3, 3, 9)
plt.title('EXTRA')
plt.imshow(pe, cmap='gray') 
plt.show()
# Estructura 3D

x_base, y_base = np.meshgrid(range(w), range(h))
z_base = np.zeros_like(x_base)
xwb = np.stack((x_base, x), axis=0)
ywb = np.stack((y_base, y), axis=0)
zwb = np.stack((z_base, zw), axis=0)

xr = np.stack((x_base, x), axis=0)
yr = np.stack((y_base, y), axis=0)
zr = np.stack((z_base, zr), axis=0)

xbl = np.stack((x_base, x), axis=0)
ybl = np.stack((y_base, y), axis=0)
zbl = np.stack((z_base, zbl), axis=0)

xb = np.stack((x_base, x), axis=0)
yb = np.stack((y_base, y), axis=0)
zb = np.stack((z_base, zb), axis=0)

xy = np.stack((x_base, x), axis=0)
yy = np.stack((y_base, y), axis=0)
zy = np.stack((z_base, zy), axis=0)

xp = np.stack((x_base, x), axis=0)
yp = np.stack((y_base, y), axis=0)
zp = np.stack((z_base, zp), axis=0)

xg = np.stack((x_base, x), axis=0)
yg = np.stack((y_base, y), axis=0)
zg = np.stack((z_base, zg), axis=0)

xc = np.stack((x_base, x), axis=0)
yc = np.stack((y_base, y), axis=0)
zc = np.stack((z_base, zc), axis=0)
# unimos los puntos
meshw = StructuredGrid(xwb, ywb, zwb)
meshr = StructuredGrid(xr, yr, zr)
meshbl = StructuredGrid(xbl, ybl, zbl)
meshy = StructuredGrid(xy, yy, zy)
meshp = StructuredGrid(xp, yp, zp)
meshb = StructuredGrid(xb, yb, zb)
meshc = StructuredGrid(xc, yc, zc)
meshg = StructuredGrid(xg, yg, zg)
#mesht = pv.merge([meshw, meshr, meshbl, meshb, meshy, meshp, meshc, meshg])

mesht = pv.merge([meshp, meshbl])
p = pv.Plotter()
p.add_mesh(meshw, color="white")
p.add_mesh(meshr, color="red")
p.add_mesh(meshp, color="magenta")
p.add_mesh(meshy, color="yellow")
p.add_mesh(meshg, color="green")
p.add_mesh(meshc, color="lightblue")
p.add_mesh(meshb, color="blue")
p.add_mesh(meshbl, color="black")
#p.add_mesh(mesht, color='lightblue')
p.show()

polydata = mesht.extract_geometry()
stl_file = 'COBEmagentnegro.stl'
polydata.save(stl_file)
print("guardado")
