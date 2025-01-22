import matplotlib.pyplot as plt

# Координати точок
P1 = [0, 0]
P2 = [-2, 1]
P3 = [2, 2]

# Вектори
v2 = [P2[0] - P1[0], P2[1] - P1[1]]
v3 = [P3[0] - P1[0], P3[1] - P1[1]]

# Створення графіка
plt.figure(figsize=(6, 6))

font_size = 20

# Малювання векторів
plt.quiver(P1[0], P1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\mathbf{v_2}$')
plt.quiver(P1[0], P1[1], v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='brown', label=r'$\mathbf{v_3}$')

# Підписи точок
plt.text(P1[0] + 0.3, P1[1] - 0.4, r'$P_1$', fontsize=font_size, color='black', ha='right')
plt.text(P2[0], P2[1] + 0.1, r'$P_2$', fontsize=font_size, color='blue', ha='right')
plt.text(P3[0], P3[1] + 0.1, r'$P_3$', fontsize=font_size, color='brown', ha='left')

# Підписи векторів
plt.text(v2[0] / 2 + 0.2, v2[1] / 2 + 0.2, r'$v_2$', fontsize=font_size, color='black', ha='right')
plt.text(v3[0] / 2 - 0.3, v3[1] / 2 + 0.2, r'$v_3$', fontsize=font_size, color='black', ha='left')

# Налаштування меж графіка
plt.xlim(-3, 4)
plt.ylim(-3, 4)
# plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
# plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.gca().set_aspect('equal', adjustable='box')

# Назва і легенда
plt.title("Вектори та точки")
plt.legend()
plt.grid(False)
plt.show()
