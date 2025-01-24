import numpy as np
from matplotlib import pyplot as plt

from src.utils.text import DEFAULT_LABEL_FONT_SIZE, print_label
from src.utils.scene import draw_scene

def draw_point(start, size=50, color="black",
               label="", label_color="black", label_fontsize=DEFAULT_LABEL_FONT_SIZE, label_offset=(0, 0)):
    plt.scatter(*start, color=color, label=label, s=size)  # s - розмір точки

    print_label(start=start, label=label, label_color=label_color, label_fontsize=label_fontsize,
                label_offset=label_offset)

def draw_points(
        x, y=None,
        vertex_color="black", vertex_size=50,
        labels=(), labels_color="black", labels_font_size=DEFAULT_LABEL_FONT_SIZE,
):
    if y is None:
        x1 = []
        y1 = []
        for a, b in x:
            x1.append(a)
            y1.append(b)

        draw_points(x1, y1,
                    vertex_color=vertex_color,
                    vertex_size=vertex_size,
                    labels=labels,
                    labels_color=labels_color,
                    labels_font_size=labels_font_size,
                    )

        return

    if labels is None or len(labels) == 0:
        return

    # Малювання точок вершин
    plt.scatter(x, y, color=vertex_color, s=vertex_size, zorder=5)

    # Додавання підписів
    for i, label in enumerate(labels):
        label_offset = (0, 0)
        if type(label) != str:
            try:
                label, label_offset = label[0], label[1]
            except IndexError:
                pass

        print_label((x[i], y[i]),
                    label=label,
                    label_offset=label_offset,
                    label_fontsize=labels_font_size,
                    label_color=labels_color,
                    )


def scene():
    p1 = np.array([0.2, .2])

    draw_point(p1, size=100, color="blue", label=r"$R$", label_color="blue", label_offset=(-0.02, 0.05))

    points = (
        (-1, 2), (-1, 3), (3, 1), (2, -3), (-3, -2)
    )

    draw_points(points,
                labels=[('A', (-0.1, -0.6)),
                        ('B', (-0.1, 0.1)),
                        'C',
                        "D",
                        # "Hello"
                        ("H", (-0.2, 0.15))
                        ],  # Підписи вершин
                vertex_color="red",
                )


if __name__ == '__main__':
    draw_scene(
        scene=scene,
        coordinate_rect=(-4, -4, 4, 4),
        # grid_show=False,
        grid_line_linestyle="-.",
        axis_show=True,
        base_axis_show=False,
    )



