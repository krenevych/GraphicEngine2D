from src.base.broken_line import draw_broken_line
from src.base.text import DEFAULT_LABEL_FONT_SIZE
from src.base.scene import draw_scene
from src.math.Vec3 import Vec3


def line2d(*poins,
           color="black", closed=False,
           linewidth=1.0, line_style="solid",
           vertex_color="black", vertex_size=50,
           labels=(), labels_color="black", labels_fontsize=DEFAULT_LABEL_FONT_SIZE):
    ps = []
    for el in poins:
        ps.append(el.xy)

    if closed:
        ps.append(poins[0].xy)

    draw_broken_line(ps,
                     color=color,
                     vertex_color=vertex_color,
                     vertex_size=vertex_size,
                     linewidth=linewidth,
                     line_style=line_style,
                     labels=labels,
                     labels_color=labels_color,
                     labels_font_size=labels_fontsize)


def debug_scene():

    O = Vec3(0, 0, 1)
    x = Vec3(1, 0, 0)
    y = Vec3(0, 1, 0)

    P1 = O
    P2 = O + x
    P3 = O + y

    labels = [
        ('P1', (-0.1, -0.3)),
        ('P2', (-0.15, 0.2)),
        ('P3', (-0.1, 0.1)),
    ]

    line2d(P1, P2, P3,
           closed=True, color="red",
           labels=labels, line_style="--", labels_fontsize=16)


if __name__ == '__main__':
    draw_scene(
        scene=debug_scene,
        coordinate_rect=(-1, -1, 2, 2),
        # grid_show=False,
        base_axis_show=False,
        # axis_show=True,
        # axis_color="red",
        # axis_line_style="-."
    )
