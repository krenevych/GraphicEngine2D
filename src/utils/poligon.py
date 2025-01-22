import numpy
import matplotlib.pyplot as plt

from src.utils.text import DEFAULT_LABEL_FONT_SIZE, print_label
from src.utils.utils import create_coordinate_system




def draw_poly(x, y=None,
              fill_color='none', alpha=1.0,
              vertex_color="black", vertex_size=50,
              edgecolor='black', linewidth=2, solid_line=False,
              labels=(), labels_color="black", labels_font_size=DEFAULT_LABEL_FONT_SIZE,
              ):
    if y is None:
        x1 = []
        y1 = []
        for a, b in x:
            x1.append(a)
            y1.append(b)

        draw_poly(x1, y1, fill_color, alpha, vertex_color, vertex_size, edgecolor, linewidth, solid_line, labels,
                  labels_color, labels_font_size)

        return

    plt.fill(x, y,
             facecolor=fill_color,
             alpha=alpha,
             edgecolor=edgecolor,
             linewidth=linewidth,
             )

    if solid_line:
        plt.fill(x, y,
                 facecolor="none",
                 edgecolor=edgecolor,
                 linewidth=linewidth,
                 )

    if labels is None or len(labels) == 0:
        return

    # Малювання точок вершин
    plt.scatter(x, y, color=vertex_color, s=vertex_size, zorder=5)

    # Додавання підписів
    for i, label in enumerate(labels):
        print_label((x[i], y[i]), label=label, label_fontsize=labels_font_size, label_color=labels_color, label_offset=(.1, 0.1))


if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(0, 0, 5, 5),
    )

    # Координати вершин багатокутника
    # x = [1, 3, 4, 2]
    # y = [1, 1, 3, 4]

    vertices = [
        numpy.array((1, 1)),
        numpy.array((3, 1)),
        numpy.array((4, 3)),
        numpy.array((2, 4)),
    ]

    labels = ['A', 'B', 'C', 'D']  # Підписи вершин
    draw_poly(
        # x, y,
        vertices,
        labels=labels,
        alpha=0.1,
        solid_line=True,
        vertex_size=100,
        vertex_color="red",
        linewidth=2,
        fill_color="red"
    )

    plt.show()
