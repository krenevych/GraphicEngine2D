import matplotlib.pyplot as plt
import numpy as np

from utils.lines import draw_vector
from utils.text_utils import print_label
from utils.utils import create_coordinate_system

if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(-3, -3, 4, 4),
        grid_show=False
    )

    # Координати точок
    P1 = np.array([0, 0])
    P2 = np.array([-2, 1])
    P3 = np.array([2, 2])

    # Вектори
    v2 = P2 - P1
    v3 = P3 - P1

    draw_vector(P1, v2, color="blue")
    draw_vector(P1, v3, color="brown")

    print_label(P1,
               label_color="green",
               label=r"$P1$",
               label_offset=(-0.3, -0.7)
               )

    print_label(P2,
               label_color="green",
               label=r"$P2$",
               label_offset=(-0.5, 0.2)
               )

    print_label(P3,
               label_color="green",
               label=r"$P3$",
               label_offset=(-0.3, 0.2)
               )

    plt.show()
