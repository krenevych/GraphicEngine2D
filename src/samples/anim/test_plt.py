import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

matplotlib.use("TkAgg")
# Створюємо фігуру
fig = plt.figure(figsize=(5, 5))

# Дані
x = np.linspace(0, 2 * np.pi, 100)

# Функція для оновлення кадру
def update(frame):
    print(f"Frame {frame}")
    fig.clear()  # Очищення фігури
    ax = fig.add_subplot(111)  # Додаємо нову вісь
    ax.plot(x, np.sin(x + frame / 10))  # Малюємо оновлену лінію
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    ax.set_title(f"Frame {frame}")
    return fig,

# Створення анімації
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

plt.show()
