import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Початкові точки
origin = np.array([0, 0, 0])

# Вектори осей
x_axis = np.array([1, 0, 0])
y_axis = np.array([0, 1, 0])
z_axis = np.array([0, 0, 1])

# Створення графіка
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
# ax = plt
# Малювання осей
ax.quiver(*origin, *x_axis, color=['red',], linewidth=1.5, label='X-axis', linestyle='--', arrow_length_ratio=0.1,)
ax.quiver(*origin, *y_axis, color='green', linewidth=1.5, label='Y-axis', linestyle='--', arrow_length_ratio=0.1)
ax.quiver(*origin, *z_axis, color='blue', linewidth=1.5, label='Z-axis', linestyle='-.', arrow_length_ratio=0.1)

# # Додавання підписів
# ax.text(1.1, 0, 0, 'X', color='red', fontsize=12)
# ax.text(0, 1.1, 0, 'Y', color='green', fontsize=12)
# ax.text(0, 0, 1.1, 'Z', color='blue', fontsize=12)

# Налаштування меж
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Вимкнення сітки та рамок
# ax.grid(False)
# ax.axis('off')

# Назва графіка
# ax.set_title("3D система координат (ручне малювання осей)")
plt.show()
