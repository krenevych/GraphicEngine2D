import matplotlib.pyplot as plt
import numpy as np

from src.utils.lines import draw_vector
from src.utils.utils import create_coordinate_system

if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(-1, -1, 5, 5),
        grid_show=False
    )

    # # Початкові точки для першого набору векторів
    P1 = np.array([1, 1])
    U1 = np.array([1, 0.5])

    P2 = np.array([0.5, .5])
    U2 = np.array([0.5, 1.7])

    draw_vector(P1, U1, color="blue")
    draw_vector(P2, U2, color="brown")

    P = np.array([3, .5])
    U = U1 + U2
    F = P + U1
    draw_vector(P, U1, color="blue")
    draw_vector(F, U2, color="brown")
    draw_vector(P, U, color="red")

    plt.show()
