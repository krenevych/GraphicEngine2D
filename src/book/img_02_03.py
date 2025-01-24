import numpy as np

from src.math.utils import normal2d
from src.base.lines import draw_vector, draw_length_with_perpendiculars_on_edges
from src.base.scene import draw_scene


def drawLineWithLength(p, u,
                       color="black",
                       edge_length=0.1,
                       label="", label_color="black",
                       label_offset=(0.0, 0.0)):
    draw_vector(p, u, color=color, )

    # Початок і кінець лінії
    start = p
    end = p + u

    perpendicular = normal2d(u)
    delta = perpendicular * 0.03
    start, end = start + delta, end + delta

    draw_length_with_perpendiculars_on_edges(start, end,
                                             linewidth=1.4,
                                             edge_length=edge_length,
                                             label_color=label_color, label=label,
                                             label_offset=label_offset)

def scene():
    p = np.array([0.2, .3])
    u = np.array([0.6, 0.4])

    edge_length = 0.05
    drawLineWithLength(p, u, color="red", label=r'$\alpha v$',
                       label_offset=(-0.07, 0.04),
                       edge_length=edge_length,
                       )

    p1 = np.array([0.6, 0.3])
    u1 = 0.3 * u

    drawLineWithLength(p1, u1, color="blue", label=r'$v$',
                       label_offset=(-0.05, 0.03),
                       edge_length=edge_length,
                       )

    ############


if __name__ == '__main__':
    draw_scene(
        scene=scene,
        coordinate_rect=(-0.1, -0.1, 1, 1),
        # grid_show=False,
        # grid_line_linestyle="-.",
        # axis_show=True,
        # base_axis_show=False,
    )


