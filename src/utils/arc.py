import matplotlib.pyplot as plt
import numpy as np

from src.utils.lines import draw_vector
from src.utils.utils import create_coordinate_system

def draw_arc(origin, v1, v2,
             radius=1.0,  # Радіус дуги
             color="black",
             linestyle="solid", linewidth=1.0,

             ):
    # Кути між векторами
    theta1 = np.arctan2(v1[1], v1[0])  # Кут першого вектора
    theta2 = np.arctan2(v2[1], v2[0])  # Кут другого вектора

    # Генерація точок дуги
    angles = np.linspace(theta1, theta2, 10)  # Усі кути між двома векторами

    x_arc = origin[0] + radius * np.cos(angles)  # X-координати дуги
    y_arc = origin[1] + radius * np.sin(angles)  # Y-координати дуги

    # Малювання дуги
    plt.plot(x_arc, y_arc, color=color, linestyle=linestyle, linewidth=linewidth, label="Дуга")

if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(-2, -2, 2, 2),
        # grid_show=False,
        base_axis_show=False,
        axis_show=True,
        axis_color="red",
        axis_line_style="-."
    )

    # Центр (початок координат)
    origin = np.array([0.5, 0.5])

    # Вектори
    v1 = np.array([1, -1.3])  # Перший вектор
    v2 = np.array([0.5, 0.866])  # Другий вектор (утворює 60 градусів з першим)

    draw_arc(origin, v1, v2,
             radius=0.25,
             color="red",
             linestyle="--", linewidth=1.0,
             )



    # # Малювання векторів
    draw_vector(origin, v1, color='blue', label=r"$v_1$")
    draw_vector(origin, v2, color='green', label=r"$v_2$")





    plt.show()




