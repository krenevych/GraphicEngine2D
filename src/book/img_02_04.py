import matplotlib.pyplot as plt
import numpy as np

from src.utils.lines import draw_vector
from src.utils.scene import draw_scene


def scene():
    P1 = np.array([0.5, 1.3])
    U1 = np.array([1.1, 0.5])
    draw_vector(P1, U1, color="blue",
                label=r'$v$',
                label_offset=(-0.15, 0.1),
                )

    P2 = np.array([1.25, 0.7])
    U2 = -U1

    draw_vector(P2, U2, color="brown", label=r'$-v$',
                label_offset=(-0.3, 0.10),
                )

if __name__ == '__main__':
    draw_scene(
        scene=scene,
        coordinate_rect=(-1, -1, 3, 3),
        grid_show=False
    )

