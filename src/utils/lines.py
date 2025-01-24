import matplotlib.pyplot as plt
import numpy as np

from src.math.utils import calc_normal
from src.utils.points import draw_point
from src.utils.text import DEFAULT_LABEL_FONT_SIZE, print_label
from src.utils.scene import draw_scene

def draw_vector(p, u,
                color="black",
                label="", label_color="black", label_fontsize=DEFAULT_LABEL_FONT_SIZE, label_offset=(0, 0)):
    # малювання вектора
    plt.quiver(p[0], p[1], u[0], u[1],
               angles='xy',
               scale_units='xy',
               scale=1, color=color, )

    print_label(start=np.array(p) + u * 0.5,
                label=label,
                label_color=label_color,
                label_fontsize=label_fontsize,
                label_offset=label_offset)


def draw_arrow(p, u,
               color="black", linewidth=2.0,
               head_width=0.01, head_length=0.01, head_color="black",
               label="", label_color="black", label_fontsize=DEFAULT_LABEL_FONT_SIZE, label_offset=(0, 0)):
    # малювання вектора
    plt.arrow(
        p[0], p[1], u[0], u[1],
        head_width=head_width, head_length=head_length,
        fc=head_color, ec=color, linewidth=linewidth
    )

    print_label(start=np.array(p) + u * 0.5,
                label=label,
                label_color=label_color,
                label_fontsize=label_fontsize,
                label_offset=label_offset)


def draw_line(
        start, end,
        color="black",
        linestyle="solid", linewidth=1.0,
):
    plt.plot([start[0], end[0]], [start[1], end[1]], color=color, linestyle=linestyle, linewidth=linewidth)


def scene():
    p1 = np.array([0.2, .2])
    u1 = np.array([0.6, 0.2])
    draw_vector(p1, u1, color="green", label=r"$T$",
                label_color="red",
                label_offset=(-0.05, 0.02),
                )

    p2 = p1 - (0.0, 0.15)

    draw_arrow(p2, u1, color="green", label=r"$T$",
               label_color="red",
               label_offset=(-0.05, 0.02),
               linewidth=2,
               head_width=0.1,
               head_length=0.1,
               head_color="red"
               )

    draw_point(p1, size=100, color="blue", label=r"$R$", label_color="blue", label_offset=(-0.02, 0.05))

    draw_line((0.5, .8), (.8, 0.9), linewidth=3, linestyle="--")
    draw_length_with_perpendiculars_on_edges((0.2, 0.6), (.8, 0.6), edge_length=0.03, linestyle="--")


def draw_length_with_perpendiculars_on_edges(start, end, color_line="black", linestyle="--", linewidth=1.0,
                                             edge_length=0.1,
                                             label="", label_color="black", label_fontsize=DEFAULT_LABEL_FONT_SIZE,
                                             label_offset=(0, 0)):
    start = np.array(start)
    end = np.array(end)

    # Малювання лінії довжини
    draw_line(start, end, color=color_line, linestyle=linestyle, linewidth=linewidth)

    # Малювання перпендикулярних ліній на кінцях
    # Довжина перпендикулярних ліній
    perpendicular = calc_normal(end - start)
    # Для початкової точки
    perp_start = start + edge_length * perpendicular
    perp_end = start - edge_length * perpendicular
    plt.plot([perp_start[0], perp_end[0]], [perp_start[1], perp_end[1]], color=color_line, linewidth=linewidth)

    draw_line(perp_start, perp_end, color=color_line, linewidth=linewidth)

    # Для кінцевої точки
    perp_start = end + edge_length * perpendicular
    perp_end = end - edge_length * perpendicular
    draw_line(perp_start, perp_end, color=color_line, linewidth=linewidth)

    print_label(start=(start + end) * 0.5,
                label=label,
                label_color=label_color, label_fontsize=label_fontsize,
                label_offset=label_offset)


if __name__ == '__main__':
    draw_scene(
        scene=scene,
        coordinate_rect=(0, 0, 1, 1),
    )


