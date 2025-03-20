import numpy as np
from PIL.ImageOps import scale


def scale_matrix(s_x, s_y=1, s_z=1):
    scale = np.array([
        [ s_x,   0,      0 ],
        [ 0,    s_y,     0 ],
        [ 0,      0,   s_z ]
    ])
    return scale


if __name__ == '__main__':
    pass
