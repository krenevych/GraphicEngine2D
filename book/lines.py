import matplotlib.pyplot as plt
import numpy as np

from book.point_utils import draw_point
from book.text_utils import FONT_SIZE, print_label
from book.utils import calc_normal, create_coordinate_system


def draw_vector(p, u,
                color="black",
                label="", label_color="black", label_fontsize=FONT_SIZE, label_offset=(0, 0)):

    # малювання вектора
    plt.quiver(p[0], p[1], u[0], u[1], angles='xy', scale_units='xy', scale=1, color=color, label='First Set')

    print_label(start=p + u * 0.5,
                label=label,
                label_color=label_color, label_fontsize=label_fontsize,
                label_offset=label_offset)


def drawLength(start, end, color_line="black", linestyle="--",
               label="", label_color="black", label_fontsize=FONT_SIZE, label_offset=(0, 0)):
    # Малювання лінії довжини
    plt.plot([start[0], end[0]], [start[1], end[1]], color=color_line, linestyle=linestyle, linewidth=1.4)

    # Малювання перпендикулярних ліній на кінцях
    # Довжина перпендикулярних ліній
    length = 0.05
    perpendicular = calc_normal(end - start)
    # Для початкової точки
    perp_start = start + length * perpendicular
    perp_end = start - length * perpendicular
    plt.plot([perp_start[0], perp_end[0]], [perp_start[1], perp_end[1]], color=color_line, linewidth=1.4)

    # Для кінцевої точки
    perp_start = end + length * perpendicular
    perp_end = end - length * perpendicular
    plt.plot([perp_start[0], perp_end[0]], [perp_start[1], perp_end[1]], color=color_line, linewidth=1.4)

    print_label(start=(start + end) * 0.5,
                label=label,
                label_color=label_color, label_fontsize=label_fontsize,
                label_offset=label_offset)




if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(0, 0, 1, 1),
    )

    p1 = np.array([0.2, .1])
    u1 = np.array([0.6, 0.4]) * 0.4
    draw_vector(p1, u1, color="green", label=r"$T$",
                label_color="red",
                label_offset=(-0.05,0.02),
                )

    draw_point(p1, size=100, color="blue", label=r"$R$", label_color="blue", label_offset=(-0.02, 0.05))

    plt.show()
