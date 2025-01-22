import matplotlib.pyplot as plt
import numpy as np

from src.utils.lines import draw_vector, draw_broken_line
from src.utils.utils import create_coordinate_system

if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(-1.5, -1.5, 1.5, 1.5),
        # grid_show=False,
        grid_line_linestyle="-.",
        axis_show=True,
        base_axis_show=False,
    )

    # Центр (початок координат)
    origin = np.array([0.5, -1])

    # Вектори
    v1 = np.array([-1, -1.5])  # Перший вектор
    v2 = np.array([-1, 1])  # Другий вектор
    draw_vector(origin, v1, color='blue', label=r"$v_1$")
    draw_vector(origin, v2, color='red', label=r"$v_2$")

    # Розрахунок координат для прямого кута
    scale = 0.4  # Масштаб для відображення прямого кута
    v1_unit = v1 / np.linalg.norm(v1)  # Одиничний вектор v1
    v2_unit = v2 / np.linalg.norm(v2)  # Одиничний вектор v2

    corner = origin + scale * v1_unit  # Перша точка кута (вздовж v1)
    corner2 = corner + scale * v2_unit  # Друга точка кута (вздовж v2)
    corner3 = origin + scale * v2_unit

    draw_broken_line([corner, corner2, corner3],
                     color="blue",
                     line_style="--", linewidth=1.0,
                     labels=['A',
                             ('B', (-0.1, 0.1)),
                             'C'
                             ],  # Підписи вершин
                     vertex_color="red",
                     )

    ############
    plt.show()
