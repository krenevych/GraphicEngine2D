import matplotlib.pyplot as plt

from src.engine.drawer import line2d
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import Vec3
from src.utils.utils import create_coordinate_system

if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(-1, -1, 2, 2),
        # grid_show=False,
        base_axis_show=False,
        # axis_show=True,
        # axis_color="red",
        # axis_line_style="-."
    )

    O = Vec3(0, 0, 1)
    x = Vec3(1, 0, 0)
    y = Vec3(0, 1, 0)

    P1 = O
    P2 = O + x
    P3 = O + y

    labels = [
        ('P1', (-0.1, -0.3)),
        ('P2', (-0.15, 0.2)),
        ('P3', (-0.1, 0.1)),
    ]

    line2d(P1, P2, P3, closed=True, color="grey", labels=labels, line_style="--", labels_fontsize=16)

    T1 = Mat3x3.translation(0, -1, 1)

    R = Mat3x3.rotationZ(30, False)
    # T = Mat3x3.translation(2, 2, 1)
    T = Mat3x3.translation(0, -1, 1)
    S = Mat3x3.scale(2, 2)

    # transform = T1.inverse() @ T @ R @ S @ T1
    # transform = T.inverse() @ S @ T1
    # transform =  T1 @ S
    # transform = T1.inverse() @ R @ T1
    transform = R
    # transform =  S @ T1

    # trans_inv = transform.inv

    P1_ = transform @ P1
    P2_ = transform @ P2
    P3_ = transform @ P3

    x_ = transform @ x
    y_ = transform @ y

    line2d(P1_, P2_, P3_, closed=True, color="red", labels=labels, line_style="solid")

    T3 = Mat3x3.translation(0, -1, 1)
    transform = T1.inverse() @ R @ T3
    P1_ = transform @ P1
    P2_ = transform @ P2
    P3_ = transform @ P3

    line2d(P1_, P2_, P3_, closed=True, color="blue", labels=labels, line_style="solid")

    plt.show()
