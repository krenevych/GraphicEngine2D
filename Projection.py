import matplotlib.pyplot as plt
import numpy as np

# Вектори
u = np.array([3.5, 1])  # Вектор u
v = np.array([1, 3])  # Вектор v

# Проекція вектора v на u
proj_v_on_u = (np.dot(v, u) / np.dot(u, u)) * u

# Початкові точки
origin = np.array([0, 0])

# Малювання фігури
plt.figure(figsize=(8, 8))

label_size = 28

plt.text(u[0] - 0.25, u[1] - 0.44, r"$u$", fontsize=label_size, color="black", weight="bold")
plt.text(v[0] - 0.3, v[1] + 0.1, r"$v$", fontsize=label_size, color="black", weight="bold")
plt.text(proj_v_on_u[0]/2 + 0.5, proj_v_on_u[1] / 2 - 0.3, r'$\mathrm{proj}_{{u}} {v}$', fontsize=label_size,
         color="black", weight="bold")

plt.text(0.25, 0.3, "$\phi$", fontsize=label_size, color="black", weight="bold")
# Малювання векторів
plt.quiver(*origin, *u, angles='xy', scale_units='xy', scale=1, color='blue', linewidth=1.5)
plt.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color='brown', linewidth=1.5)
plt.quiver(*origin, *proj_v_on_u, angles='xy', scale_units='xy', scale=1, color='red', linestyle='dashed',
           linewidth=1.5)

# Пунктирна лінія для з'єднання
plt.plot([v[0], proj_v_on_u[0]], [v[1], proj_v_on_u[1]], 'k--', linewidth=0.8)

# # Відображення осей
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)

# Налаштування меж
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.gca().set_aspect('equal', adjustable='box')

# Підписи до осей
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Додавання легенди
# plt.legend()

# Відображення графіка
plt.title("Проекція вектора $\mathbf{v}$ на вектор $\mathbf{u}$")
plt.grid(False)
plt.show()
