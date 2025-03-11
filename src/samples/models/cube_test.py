import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

matplotlib.use("TkAgg")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Вершини куба
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Грані куба
faces = [[vertices[j] for j in [0, 1, 2, 3]],
         [vertices[j] for j in [4, 5, 6, 7]],
         [vertices[j] for j in [0, 1, 5, 4]],
         [vertices[j] for j in [2, 3, 7, 6]],
         [vertices[j] for j in [1, 2, 6, 5]],
         [vertices[j] for j in [4, 7, 3, 0]]]

ax.add_collection3d(Poly3DCollection(faces,
                                     facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Встановлення меж для осей
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Підписи осей
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
