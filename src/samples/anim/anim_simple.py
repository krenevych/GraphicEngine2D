import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

matplotlib.use("TkAgg")

# Створюємо фігуру та вісь
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))  # Лінія синусоїди

# Налаштування меж
ax.set_ylim(-1.5, 1.5)

# Функція для оновлення графіка
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # Оновлення даних
    return fig,

# Створюємо анімацію
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
