import numpy as np
from matplotlib import pyplot as plt

from src.base.scene import draw_scene

DEFAULT_LABEL_FONT_SIZE = 20


def print_label(start,
                label="", label_color="black", label_fontsize=DEFAULT_LABEL_FONT_SIZE, label_offset=(0, 0)):
    if label is not None and label != "":
        label_pos = np.array(start) + label_offset
        plt.text(float(label_pos[0]), float(label_pos[1]), label, fontsize=label_fontsize, color=label_color,
                 ha='left')


def scene():
    print_label(start=(0.5, 0.5),
                label=r"Hello $R_2^4$", label_color="red", label_fontsize=22,
                label_offset=(-0.2, 0.1))

    print_label(start=(0.5, 0.2),
                label=r"Water $H_20$", label_color="green", label_fontsize=13,
                label_offset=(-0.2, 0.1))


if __name__ == '__main__':
    draw_scene(
        scene=scene,
        coordinate_rect=(0, 0, 1, 1),
        grid_show=True,
    )
