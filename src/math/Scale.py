import numpy as np


def scale_matrix(s_x, s_y, s_z):
    translation_matrix_3d = np.array([
        [s_x, 0, 0, 0],
        [0, s_y, 0, 0],
        [0, 0, s_z, 0],
        [0, 0,   0, 1]
    ])
    return translation_matrix_3d


if __name__ == '__main__':
    pass
