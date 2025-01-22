import matplotlib.pyplot as plt
import numpy as np

# Вектори
u = np.array([4, 2])  # Вектор u
v = np.array([3, 5])  # Вектор v

# Проекція вектора v на u
proj_v_on_u = (np.dot(v, u) / np.dot(u, u)) * u

# Початкові точки
origin = np.array([0, 0])

# Малювання фігури
plt.figure(figsize=(8, 8))

# Малювання векторів
plt.quiver(*origin, *u, angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\mathbf{u}$', linewidth=1.5)
plt.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color='green', label=r'$\mathbf{v}$', linewidth=1.5)
plt.quiver(*origin, *proj_v_on_u, angles='xy', scale_units='xy', scale=1, color='red', label=r'$\mathrm{proj}_{\mathbf{u}} \mathbf{v}$', linestyle='dashed', linewidth=1.5)

# Пунктирна лінія для з'єднання
plt.plot([v[0], proj_v_on_u[0]], [v[1], proj_v_on_u[1]], 'k--', linewidth=0.8)

# Малювання перпендикуляра
plt.quiver(proj_v_on_u[0], proj_v_on_u[1], v[0] - proj_v_on_u[0], v[1] - proj_v_on_u[1],
           angles='xy', scale_units='xy', scale=1, color='black', linestyle='dotted', linewidth=1.2)

# Додавання прямого кута
plt.plot([proj_v_on_u[0], proj_v_on_u[0] + 0.5], [proj_v_on_u[1], proj_v_on_u[1]], 'k-', linewidth=1)
plt.plot([proj_v_on_u[0] + 0.5, proj_v_on_u[0] + 0.5], [proj_v_on_u[1], proj_v_on_u[1] + 0.5], 'k-', linewidth=1)

# Додавання підписів
plt.text(u[0] / 2, u[1] / 2, r'$\mathbf{u}$', fontsize=12, color='blue')
plt.text(v[0] / 2, v[1] / 2, r'$\mathbf{v}$', fontsize=12, color='green')
plt.text(proj_v_on_u[0] / 2, proj_v_on_u[1] / 2, r'$\mathrm{proj}_{\mathbf{u}} \mathbf{v}$', fontsize=12, color='red')
plt.text((v[0] + proj_v_on_u[0]) / 2, (v[1] + proj_v_on_u[1]) / 2, r'$\perp$', fontsize=12, color='black')

# Відображення осей
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Налаштування меж
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.gca().set_aspect('equal', adjustable='box')

# Підписи до осей
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Додавання легенди
plt.legend()

# Відображення графіка
plt.title("Проекція вектора $\mathbf{v}$ на вектор $\mathbf{u}$ з прямим кутом")
plt.grid(False)
plt.show()
