import numpy as np

from src.math.Mat4x4 import Mat4x4
from src.math.Rotations import rotation
from src.math.Vec4 import vertex

if __name__ == '__main__':
    # transf = Mat3x3.translation(3, 4) * Mat3x3.rotation(33, False) * Mat3x3.scale(2, 3)
    #
    # print(transf)
    #
    # translation, angle, scales = Mat3x3.decompose_affine(transf)
    #
    # print(translation)
    # print(angle)
    # print(scales)
    #
    # print()
    #
    # T = Mat3x3.translation(*translation)
    # R = Mat3x3.rotation(angle)
    # S = Mat3x3.scale(*scales)
    #
    # transformation = T * R * S
    #
    # print(transformation)

    Rx = Mat4x4.rotation_x(np.radians(-30))
    Ry = Mat4x4.rotation_y(np.radians(40))

    print(Rx)
    print()
    print(Ry)
    print()

    R = Ry * Rx
    print(R)
    print()

    u = R * vertex(0, 0, 1)

    print(u)

    phy, theta = rotation(np.radians(40), u)

    print(np.degrees(phy), np.degrees(theta))
