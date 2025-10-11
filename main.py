import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pyvista as pv
import os

# Insertar imagen
img_path = r'C:\Users\cotif\Documents\GitHub\imgtoSTL\imgs\decrease (1).png'


# Convertir a escala se grises

image= Image.open(img_path).convert("L")
image.show()
# Armo matriz de la imagen
matriz = np.asarray(image)

# Crea una copia de la matriz para trabajar sobre los pixeles
matriz_mod = matriz.copy()
h, w = matriz.shape

for i in range(h):
    for j in range(w):
        if matriz_mod[i][j] == 255:
            matriz_mod[i][j] = 0  # Lo que esta blanco lo cambio a negro
        else:
            matriz_mod[i][j] = 255  # Cambio a blanco(255)

plt.imshow(matriz_mod, cmap='gray', vmin=0, vmax=255)
plt.title("Inversion de escalas")
plt.show()

# -------------------- Agrandar lineas -----------------------------
# mask = np.array([[1, 0, 1],
#                  [0, 0, 0],
#                  [1, 0, 1]])

alto, ancho = matriz_mod.shape
img_mask = matriz_mod.copy()

# # # Aplicar la máscara a píxeles blancos
# for y in range(alto):
#     for x in range(ancho):
#         if matriz_mod[y, x] > 0:  # Si el píxel es blanco se aplica la mascara
#             for i in range(-2, 1):  # Usamos el -3 para centrar la mascara
#                 for j in range(-2, 1):
#                     img_mask[y + i, x + j] = 255  # Píxel en blanco

# plt.imshow(img_mask, cmap='gray', vmin=0, vmax=255)
# plt.show()

# ---------- Visualizar en 3d y cambiar altura a los blancos con pyVista
# Crear una copia de la matriz
matriz2d = img_mask.copy()
height_m, width_m = img_mask.shape

# Creo variables para luego agregar las alturas
x = np.zeros((height_m, width_m))
y = np.zeros((height_m, width_m))
z = np.zeros((height_m, width_m))

# Creo un bucle for para agregarle las alturas dependiendo el valor de pixel
for i in range(height_m):
    for j in range(width_m):
        pixel = img_mask[i, j]
        x[i, j] = j  # Coordenada X
        y[i, j] = i  # Coordenada Y
        if pixel == 255:  # Si el pixel es blanco, establece la altura en 6
            z[i, j] = 6 # Altura Z
        else:  # Si el pixel es blanco, establece la altura en 6
            z[i, j] = 0 # Altura Z


# Creo una base con altura 0 y con igual dimesiones que la original
x_base, y_base = np.meshgrid(range(width_m), range(height_m))
z_base = np.zeros_like(x_base)

# Unimos los puntos de las 2 superficies (importante poner el axis=0)
x = np.stack((x_base, x), axis=0)
y = np.stack((y_base, y), axis=0)
z = np.stack((z_base, z), axis=0)

# Creamos la estructura
mesh = pv.StructuredGrid(-x, y, z)
mesh.points = mesh.points * 0.06

# Mostramos la estructura
p = pv.Plotter()
p.add_mesh(mesh, color="gray")
p.show()

# ------Para guarda la estructura a stl 

# polydata = mesh.extract_geometry()
# stl_file = 'lluvia_particulas.stl'
# polydata.save(stl_file)
# print("se guardo la imagen como: ", stl_file)
