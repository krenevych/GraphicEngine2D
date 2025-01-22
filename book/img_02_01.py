import matplotlib.pyplot as plt

# Координати початкових точок стрілок
X = [0, 0.5, 0]  # X-координати початку
Y = [0, 1, 1.4]  # Y-координати початку

# Компоненти векторів (напрямок стрілок)
U = [1, 1, 1]  # X-компоненти
V = [1, 1, 1]  # Y-компоненти

# Створення графіка
plt.figure(figsize=(6, 6))

# Малювання векторів
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='blue')

# Налаштування меж графіка
plt.xlim(-1, 3)
plt.ylim(-1, 5)
# plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
# plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
# plt.gca().set_aspect('equal', adjustable='box')

# Назва графіка
# plt.title("Паралельні вектори")

plt.grid(False)
plt.show()
