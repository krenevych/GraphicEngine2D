import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

# # Створення 3D-фігури за допомогою plt.subplots()
# fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"projection": "3d"})
#
# # Генеруємо точки
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X**2 + Y**2))
#
# # Малюємо поверхню
# ax.plot_surface(X, Y, Z, cmap='viridis')
#
# plt.show()

# Створюємо 3D-фігуру
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Генеруємо точки
X, Y, Z = np.meshgrid(np.arange(0, 5, 2), np.arange(0, 5, 2), np.arange(0, 5, 2))
U, V, W = np.ones_like(X), np.zeros_like(Y), np.zeros_like(Z)

# Малюємо вектори у 3D-просторі
ax.quiver(X, Y, Z, U, V, W, color="red")

plt.show()
