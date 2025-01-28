import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use("TkAgg")

# Створення фігури та осей
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Функція для оновлення кадру
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # Оновлення лінії
    return line,

# Створення анімації
ani = FuncAnimation(fig, update, frames=100, interval=50)

# Відслідковування подій
def on_animation_start():
    print("Анімація стартувала!")

def on_animation_stop():
    print("Анімація завершена!")

def on_key(event):
    if event.key == "escape":  # Натиснення клавіші Escape для зупинки
        ani.event_source.stop()
        on_animation_stop()
    elif event.key == "enter":  # Натиснення Enter для старту
        ani.event_source.start()
        on_animation_start()

# Прив'язка подій до фігури
fig.canvas.mpl_connect("key_press_event", on_key)

plt.show()
