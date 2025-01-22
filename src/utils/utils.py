import numpy as np
from matplotlib import pyplot as plt

def calc_normal(start, end=None):
    if end is None:
        direction = start
        direction = direction / np.linalg.norm(direction)  # Нормалізація вектора

        # Обчислення перпендикулярного вектора
        __perpendicular = np.array([-direction[1], direction[0]])
        return __perpendicular
    else:
        # Вектор напряму лінії
        direction = end - start
        return calc_normal(direction)


def create_coordinate_system(image_size=(5, 5),
                             coordinate_rect=(-1, -1, 1, 1),
                             title=("Picture"),
                             grid_show=True,
                             keep_aspect_ratio=False,
                             ):
    plt.figure(figsize=image_size)
    plt.xlim(coordinate_rect[0], coordinate_rect[2])
    plt.ylim(coordinate_rect[1], coordinate_rect[3])
    if keep_aspect_ratio:
        plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.grid(grid_show)


if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(-0.5, -1, 2, 2),
        grid_show=False
    )

    ##########################
    # Draw here
    ##########################

    plt.show()

