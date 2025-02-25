import numpy as np

from src.math.Mat4x4 import Mat4x4
from src.math.Quaternion import Quaternion
from src.math.Vec4 import Vec4

if __name__ == '__main__':
    t1 = Vec4(0, 0, 1)

    angle_x = np.radians(30)
    angle_y = np.radians(45)
    angle_z = np.radians(60)

    Rx = Mat4x4.rotation_x(angle_x)
    Ry = Mat4x4.rotation_y(angle_y)
    Rz = Mat4x4.rotation_z(angle_z)

    t1_m = Rz * Ry * Rx * t1
    print(f"{t1_m=}")

    OX = (1, 0, 0)
    OY = (0, 1, 0)
    OZ = (0, 0, 1)
    # qx = Quaternion.rotation(OX, angle_x)
    # qy = Quaternion.rotation(OY, angle_y)
    # qz = Quaternion.rotation(OZ, angle_z)
    qx = Quaternion.rotation_x(angle_x)
    qy = Quaternion.rotation_y(angle_y)
    qz = Quaternion.rotation_z(angle_z)

    print(f"{qx=}")
    print(f"{qy=}")
    print(f"{qz=}")

    q = qz * qy * qx
    print(f"{q=}")

    h1 = q.rotate_vector(t1)
    print(f"{h1=}")
    h1 = q.rotate_vector([0, 0, 1])
    print(f"{h1=}")
