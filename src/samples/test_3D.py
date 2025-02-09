import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Створюємо фігуру
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

# Координати трьох вершин трикутника
vertices = [
    [0, 0, 0],  # Вершина A
    [1, 0, 0],  # Вершина B
    [0, 1, 0],  # Вершина C
]

# Малюємо трикутник
triangle = Poly3DCollection([vertices], alpha=0.5, edgecolor="black", facecolor="cyan")
ax.add_collection3d(triangle)

# Налаштування меж графіка
ax.set_xlim([0, 1.5])
ax.set_ylim([0, 1.5])
ax.set_zlim([0, 1])

# Підписи осей
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
