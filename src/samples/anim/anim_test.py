import matplotlib
import numpy as np

from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import Vec3, vertex

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# # Увімкнення інтерактивного режиму
coordinate_rect = (-1, -1, 4, 4)
# # Створення фігури та осей
# # fig, ax = plt.subplots()
fig = plt.figure(figsize=(5, 5))
# # fig, ax = plt.subplots()
# # ax.set_xlim(0, 10)  # Межі для осі x
# # ax.set_ylim(0, 5)   # Межі для осі y
plt.xlim(coordinate_rect[0], coordinate_rect[2])
plt.ylim(coordinate_rect[1], coordinate_rect[3])
#
rect = SimplePolygon(
        0, 0,
        1, 0,
        1, 1,
        0, 1
    )
rect.color = "blue"
rect.line_style = "-"
rect.draw()

# Створюємо прямокутник
# rectangle = plt.Rectangle((0, 2), 2, 1, color='blue')
# ax.add_patch(rectangle)
x = np.linspace(0, 2 * np.pi, 100)
# Функція для оновлення кадру

start = vertex(0, 0)
end = vertex(2, 3)


def update(frame):
    print(f"Frame {frame}")
    fig.clear()  # Очищення фігури
    plt.xlim(coordinate_rect[0], coordinate_rect[2])
    plt.ylim(coordinate_rect[1], coordinate_rect[3])
    ax = fig.add_subplot(111)  # Додаємо нову вісь
    ax.plot(x, np.sin(x + frame / 10))  # Малюємо оновлену лінію
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    ax.set_title(f"Frame {frame}")

    vect = start +  (end - start) * (frame / 100)
    T = Mat3x3.translation(vect)
    rect.transformation = T
    rect.draw()
    return fig,

# Створення анімації
# ani = FuncAnimation(fig, update, frames=100, blit=True, interval=50)
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

# Відображення анімації
plt.show()
