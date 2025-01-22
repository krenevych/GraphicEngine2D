import matplotlib.pyplot as plt
import numpy as np

from utils.lines import draw_vector
from utils.utils import create_coordinate_system

if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(-1, -1, 3, 5),
        grid_show=False
    )

    U = np.array((1, 1))
    P1 = np.array((0, 0))
    P2 = np.array((0.5,1))
    P3 = np.array((0, 1.4))

    draw_vector(P1, U, color="blue")
    draw_vector(P2, U, color="blue")
    draw_vector(P3, U, color="blue")

    plt.show()
