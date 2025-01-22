import numpy as np
from matplotlib import pyplot as plt

from src.utils.text import DEFAULT_LABEL_FONT_SIZE, print_label
from src.utils.utils import create_coordinate_system


def draw_point(start, size=50, color="black",
               label="", label_color="black", label_fontsize=DEFAULT_LABEL_FONT_SIZE, label_offset=(0, 0)):
    plt.scatter(*start, color=color, label=label, s=size)  # s - розмір точки

    print_label(start=start, label=label, label_color=label_color, label_fontsize=label_fontsize,
                label_offset=label_offset)


if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(0, 0, 1, 1),
    )

    p1 = np.array([0.2, .2])

    draw_point(p1, size=100, color="blue", label=r"$R$", label_color="blue", label_offset=(-0.02, 0.05))

    plt.show()