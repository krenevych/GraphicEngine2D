# from matplotlib import pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')
#
# # Відображення поверхні
# surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
#
# # Анімація
# def update(frame):
#     ax.view_init(elev=30, azim=frame)
#     return fig,
#
# ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Глобальний фрейм
origin_global = np.array([0, 0])
x_global = np.array([1, 0])
y_global = np.array([0, 1])



# Локальний фрейм
origin_local = np.array([2, 2])
x_local = np.array([0.866, 0.5])  # Поворот на 30 градусів
y_local = np.array([-0.5, 0.866])

# Створення графіка
plt.figure(figsize=(6, 6))

# Глобальний фрейм
plt.quiver(*origin_global, *x_global, angles='xy', scale_units='xy', scale=1, color='blue', label="X Global")
plt.quiver(*origin_global, *y_global, angles='xy', scale_units='xy', scale=1, color='green', label="Y Global")

# Локальний фрейм
plt.quiver(*origin_local, *x_local, angles='xy', scale_units='xy', scale=1, color='red', label="X Local")
plt.quiver(*origin_local, *y_local, angles='xy', scale_units='xy', scale=1, color='orange', label="Y Local")

# Налаштування меж
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title("Глобальний та локальний фрейми")
plt.show()
