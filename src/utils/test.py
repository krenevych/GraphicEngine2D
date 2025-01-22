import matplotlib.pyplot as plt

# Дані
vectors = [
    {'start': (0, 0), 'dx': 1, 'dy': 2, 'linewidth': 2},
    {'start': (1, 1), 'dx': 2, 'dy': 1, 'linewidth': 4},
]

# Створення графіка
plt.figure(figsize=(6, 6))
for vec in vectors:
    plt.arrow(
        vec['start'][0], vec['start'][1], vec['dx'], vec['dy'],
        head_width=0.2, head_length=0.3, fc='blue', ec='blue', linewidth=vec['linewidth']
    )

# Налаштування меж графіка
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.title("Вектори з різною товщиною")
plt.show()
