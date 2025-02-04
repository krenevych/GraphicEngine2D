import matplotlib.pyplot as plt
import numpy as np

from src.engine.Scene import Scene
from src.base.text import DEFAULT_LABEL_FONT_SIZE, print_label
from src.math.utils import normal2d


def draw_line(
        start, end,
        color="black",
        linestyle="solid", linewidth=1.0,
):
    plt.plot([start[0], end[0]], [start[1], end[1]], color=color, linestyle=linestyle, linewidth=linewidth)


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
    perpendicular = normal2d(end - start)
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
    class SampleScene(Scene):
        def draw_figures(self):
            draw_line((0.5, .8), (.8, 0.9), linewidth=3, linestyle="--")
            draw_length_with_perpendiculars_on_edges((0.2, 0.6), (.8, 0.6), edge_length=0.03, linestyle="--")


    scene = SampleScene(
        coordinate_rect=(0, 0, 1, 1),
    ).prepare()
    scene.draw_figures()
    scene.finalize()
