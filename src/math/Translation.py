import numpy as np


def translationMatrix2d(t_x, t_y):
    translation_matrix = np.array([
        [1, 0, t_x],
        [0, 1, t_y],
        [0, 0, 1]
    ])
    return translation_matrix


def translationMatrix(t_x, t_y, t_z):
    translation_matrix_3d = np.array([
        [1, 0, 0, t_x],
        [0, 1, 0, t_y],
        [0, 0, 1, t_z],
        [0, 0, 0, 1]
    ])
    return translation_matrix_3d


if __name__ == '__main__':
    # Зсуви
    T = translationMatrix(t_x=3,  # Зсув уздовж осі X
                          t_y=4,  # Зсув уздовж осі Y
                          t_z=5  # Зсув уздовж осі Z
                          )
    print(T)
