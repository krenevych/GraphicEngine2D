import matplotlib

matplotlib.use("TkAgg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Створюємо фігуру та одну область координат (одна вісь)
fig, ax = plt.subplots(figsize=(6, 6))

# Генеруємо дані
x = np.linspace(0, 2 * np.pi, 100)

# Додаємо дві лінії на один графік
line1, = ax.plot(x, np.sin(x), label="sin(x)", color="blue")
line2, = ax.plot(x, np.cos(x), label="cos(x)", color="red")

# Налаштовуємо межі графіка та легенду
ax.set_ylim(-1.2, 1.2)
ax.set_title("Анімація синусоїди та косинусоїди")
ax.legend()


# Функція оновлення для обох ліній
def update(frame):
    line1.set_ydata(np.sin(x + frame / 10))  # Оновлення синусоїди
    line2.set_ydata(np.cos(x + frame / 10))  # Оновлення косинусоїди
    return line1, line2


# Створюємо анімацію
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()  # Запускаємо анімацію
