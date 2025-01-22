import numpy as np
import matplotlib.pyplot as plt

# Вектори
v1 = np.array([2, 0])  # Перший вектор
v2 = np.array([-0.5, -0.866])  # Другий вектор (утворює 60 градусів з першим)

# Центр (початок координат)
origin = np.array([0, 0])

# Кути між векторами
theta1 = np.arctan2(v1[1], v1[0])  # Кут першого вектора
theta2 = np.arctan2(v2[1], v2[0])  # Кут другого вектора

# Генерація точок дуги
angles = np.linspace(theta1, theta2, 100)  # Усі кути між двома векторами
radius = 0.3  # Радіус дуги
x_arc = radius * np.cos(angles)  # X-координати дуги
y_arc = radius * np.sin(angles)  # Y-координати дуги

# Створення графіка
plt.figure(figsize=(6, 6))

# Малювання векторів
plt.quiver(*origin, *v1, angles='xy', scale_units='xy', scale=1, color='blue', label="Вектор 1")
plt.quiver(*origin, *v2, angles='xy', scale_units='xy', scale=1, color='green', label="Вектор 2")

# Малювання дуги
plt.plot(x_arc, y_arc, color='red', linestyle='--', linewidth=2, label="Дуга")

# Налаштування меж
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# Легенда та підписи
plt.legend()
plt.title("Дуга між двома векторами")
plt.grid(True)
plt.show()
