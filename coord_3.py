import matplotlib.pyplot as plt
import numpy as np

# Вершини паралелограма
origin = np.array([0, 0])  # Початок координат
point_a = np.array([2, 1])  # Вершина (a, b)
point_b = np.array([1, 3])  # Вершина (A, B)
point_c = point_a + point_b  # Протилежна вершина

# Координати всіх точок для з'єднання
points = np.array([origin, point_a, point_c, point_b, origin])

# Малювання паралелограма
plt.figure(figsize=(6, 6))
plt.fill(points[:, 0], points[:, 1], color='blue', alpha=0.3)  # Затінення фігури
plt.plot(points[:, 0], points[:, 1], color='black')  # Контур

# Додавання точок і підписів
plt.scatter([origin[0], point_a[0], point_b[0], point_c[0]],
            [origin[1], point_a[1], point_b[1], point_c[1]],
            color='black')
plt.text(origin[0] - 0.5, origin[1] - 0.3, '(0, 0)', fontsize=12)
plt.text(point_a[0] + 0.1, point_a[1], '(a, b)', fontsize=12)
plt.text(point_b[0] - 0.8, point_b[1] + 0.2, '(A, B)', fontsize=12)
plt.text(point_c[0] + 0.1, point_c[1], '(a+A, b+B)', fontsize=12)

# Додавання стрілок для осей
plt.arrow(0, 0, 4, 0, head_width=0.2, head_length=0.2, fc='black', ec='black', linewidth=0.8)
plt.arrow(0, 0, 0, 4, head_width=0.2, head_length=0.2, fc='black', ec='black', linewidth=0.8)

# Налаштування меж осей
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# Підписи до осей
plt.text(4.2, 0, 'X', fontsize=14, color='black')
plt.text(0.2, 4.2, 'Y', fontsize=14, color='black')

# Відключення стандартних осей
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Сітка
plt.grid(False)

# Назва графіка
plt.title('Паралелограм у декартовій системі координат')

# Відображення графіка
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
