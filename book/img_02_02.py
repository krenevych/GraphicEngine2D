import matplotlib.pyplot as plt
import numpy as np

# Створення графіка
plt.figure(figsize=(6, 6))

# Початкові точки для першого набору векторів
P1 = np.array([1, 1])
U1 = np.array([1, 0.5])

P2 = np.array([0.5, .5])
U2 = np.array([0.5, 1.7])

P = np.array([3, .5])
U = U1 + U2

# Малювання векторів першого набору (сині)
plt.quiver(P1[0], P1[1], U1[0], U1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='First Set')
plt.quiver(P2[0], P2[1], U2[0], U2[1], angles='xy', scale_units='xy', scale=1, color='brown', label='First Set')
# plt.quiver( X2, U2, angles='xy', scale_units='xy', scale=1, color='blue', label='First Set')

# додавання векторів
F = P + U1
plt.quiver(P[0], P[1], U1[0], U1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='First Set')
plt.quiver(F[0], F[1], U2[0], U2[1], angles='xy', scale_units='xy', scale=1, color='brown', label='First Set')
plt.quiver(P[0], P[1], U[0], U[1], angles='xy', scale_units='xy', scale=1, color='red', label='First Set')

# Налаштування меж графіка
plt.xlim(-1, 5)
plt.ylim(-1, 5)
# plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
# plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.gca().set_aspect('equal', adjustable='box')

# Назва графіка
plt.title("Два набори векторів")

# Легенда
plt.legend()
plt.grid(False)
plt.show()
