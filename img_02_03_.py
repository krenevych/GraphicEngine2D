# import matplotlib.pyplot as plt
# import numpy as np
#
# FONT_SIZE = 20
#
# # Створення графіка
# plt.figure(figsize=(6, 6))
#
# P1 = np.array([0.5, 1])
# U1 = np.array([0.4, 0.5])
# plt.quiver(P1[0], P1[1], U1[0], U1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='First Set')
#
# v1 = P1 + U1 * 0.5 + np.array([-0.1, 0.1])
# plt.text(v1[0], v1[1], r'$v$', fontsize=FONT_SIZE, color='black', ha='right')
#
# alpha = 2.4
# P2 = np.array([1.25, 0.7])
# U2 = U1 * alpha
# plt.quiver(P2[0], P2[1], U2[0], U2[1], angles='xy', scale_units='xy', scale=1, color='brown', label='First Set')
#
# v2 = P2 + U2 * 0.5 + np.array([-0.2, 0.3])
# plt.text(v2[0], v2[1], r'$-v$', fontsize=FONT_SIZE, color='black', ha='left')
#
#
# # Налаштування меж графіка
# plt.xlim(-1, 3)
# plt.ylim(-1, 5)
# # plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
# # plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
# # plt.gca().set_aspect('equal', adjustable='box')
#
# # Назва графіка
# # plt.title("Паралельні вектори")
#
# plt.grid(False)
# plt.show()


from matplotlib.patches import FancyArrowPatch
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 6))

# Кастомна стрілка
arrow = FancyArrowPatch(
    (0, 0), (1, 1),
    arrowstyle='Simple,head_length=15,head_width=7,tail_width=1',
    color='brown',
    linewidth=2
)

arrow1 = FancyArrowPatch(
    (1, 0), (1, 0.5),
    arrowstyle='|-|',
    # arrowstyle='|-|,head_length=15,head_width=7,tail_width=1',
    color='blue',
    linewidth=2
)

# Додавання стрілки
ax.add_patch(arrow)
ax.add_patch(arrow1)

# Налаштування осей
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.grid(False)

plt.title("Кастомна стрілка")
plt.show()
