from matplotlib import pyplot as plt

from utils.text_utils import print_label, FONT_SIZE


def draw_point(start, size=50, color="black",
               label="", label_color="black", label_fontsize=FONT_SIZE, label_offset=(0, 0)):
    plt.scatter(*start, color=color, label=label, s=size)  # s - розмір точки

    print_label(start=start, label=label, label_color=label_color, label_fontsize=label_fontsize,
                label_offset=label_offset)