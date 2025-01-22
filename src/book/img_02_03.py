import matplotlib.pyplot as plt
import numpy as np

from src.utils.lines import draw_vector, draw_length_with_perpendiculars_on_edges, draw_arrow
from src.utils.utils import calc_normal, create_coordinate_system


def drawLineWithLength(p, u,
                       color="black",
                       edge_length=0.1,
                       label="", label_color="black",
                       label_offset=(0.0, 0.0)):
    draw_vector(p, u, color=color, )

    # Початок і кінець лінії
    start = p
    end = p + u

    perpendicular = calc_normal(u)
    delta = perpendicular * 0.03
    start, end = start + delta, end + delta

    draw_length_with_perpendiculars_on_edges(start, end,
                                             linewidth=1.4,
                                             edge_length=edge_length,
                                             label_color=label_color, label=label,
                                             label_offset=label_offset)


if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(0, 0, 1, 1),
        # grid_show=False
    )

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
                       edge_length = edge_length,
                       )

    ############
    plt.show()
