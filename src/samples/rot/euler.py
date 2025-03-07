import numpy as np

from src.math.Mat4x4 import Mat4x4
from src.math.Vec3 import Vec3
from src.math.utils_matrix import is_same_matrix


def euler_xyz(phi, theta, psi):
    return Mat4x4.rotation_x(phi) * Mat4x4.rotation_y(theta) * Mat4x4.rotation_z(psi)


def euler_xyz_rotation_matrix(phi, theta, psi):
    """
    Генерує матрицю обертання на основі кутів Ейлера (XYZ конфігурація) без множення матриць.

    Вхід:
    - phi: кут обертання навколо осі X
    - theta: кут обертання навколо осі Y
    - psi: кут обертання навколо осі Z

    Вихід:
    - 3x3 матриця обертання
    """
    cos_phi, sin_phi = np.cos(phi), np.sin(phi)
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)
    cos_psi, sin_psi = np.cos(psi), np.sin(psi)

    return Mat4x4(
        np.array([
            [cos_theta * cos_psi, -cos_theta * sin_psi, sin_theta],
            [cos_phi * sin_psi + sin_phi * sin_theta * cos_psi, cos_phi * cos_psi - sin_phi * sin_theta * sin_psi,
             -sin_phi * cos_theta],
            [sin_phi * sin_psi - cos_phi * sin_theta * cos_psi, sin_phi * cos_psi + cos_phi * sin_theta * sin_psi,
             cos_phi * cos_theta]
        ])
    )


def euler_zxz(phi, theta, psi):
    return Mat4x4.rotation_z(phi) * Mat4x4.rotation_x(theta) * Mat4x4.rotation_z(psi)


def euler_zxz_rotation_matrix(phi, theta, psi):
    """
    Генерує матрицю обертання на основі кутів Ейлера (ZXZ конфігурація) без множення матриць.

    Вхід:
    - alpha: кут обертання навколо осі Z
    - beta: кут обертання навколо нової осі X
    - gamma: кут обертання навколо нової осі Z

    Вихід:
    - 3x3 матриця обертання
    """
    cos_varphi, sin_varphi = np.cos(phi), np.sin(phi)
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)
    cos_psi, sin_psi = np.cos(psi), np.sin(psi)

    return np.array([
        [cos_varphi * cos_psi - sin_varphi * cos_theta * sin_psi,
         -cos_varphi * sin_psi - sin_varphi * cos_theta * cos_psi, sin_varphi * sin_theta],
        [sin_varphi * cos_psi + cos_varphi * cos_theta * sin_psi,
         -sin_varphi * sin_psi + cos_varphi * cos_theta * cos_psi, -cos_varphi * sin_theta],
        [sin_theta * sin_psi, sin_theta * cos_psi, cos_theta]
    ])


def rotation_matrix_to_euler_xyz(r):
    """
    Відновлює кути Ейлера (XYZ) з матриці обертання.

    Вхід:
        R - 3x3 матриця обертання
    Вихід:
        (phi, theta, psi) - кути Ейлера (рад)
    """
    # if np.isclose(r[0, 2], 1.0, atol=1e-6):  # Сингулярний випадок (Gimbal Lock) theta = np.pi / 2
    #     print("Case 0")
    #     phi = np.arctan2(r[1, 0], r[1, 1])
    #     theta = np.pi / 2
    #     psi = 0  # Азимут стає невизначеним
    # elif np.isclose(r[0, 2], -1.0, atol=1e-6):  # Інший сингулярний випадок (Gimbal Lock)  theta = -np.pi / 2
    # # elif np.isclose(r[ 2, 0], -1.0, atol=1e-6):  # Інший сингулярний випадок (Gimbal Lock)  theta = -np.pi / 2
    #     print("Case 1")
    #     phi = np.arctan2(-r[0, 1], -r[0, 2])
    #     # phi = np.arctan2(-r[1, 0], -r[1, 1])
    #     theta = -np.pi / 2
    #     psi = 0  # Азимут стає невизначеним
    # else:
    #     print("Case BASE")
    #     phi = -np.arctan2(r[1, 2], r[2, 2])
    #     theta = np.arcsin(r[0, 2])
    #     psi = -np.arctan2(r[0, 1], r[0, 0])
    # # print(float(phi), float(theta), float(psi))
    # print("inside func: ", np.degrees(phi), np.degrees(theta), np.degrees(psi))
    # return float(phi), float(theta), float(psi)


    print("Case BASE")
    phi = -np.arctan2(r[1, 2], r[2, 2])
    theta = np.arcsin(r[0, 2])
    psi = -np.arctan2(r[0, 1], r[0, 0])
    # print(float(phi), float(theta), float(psi))
    print("inside func: ", np.degrees(phi), np.degrees(theta), np.degrees(psi))
    return float(phi), float(theta), float(psi)


if __name__ == '__main__':
    # phi, theta, psi = np.radians(90), np.radians(90), np.radians(90)
    #
    # M1_xyz = euler_xyz_rotation_matrix(phi, theta, psi)
    # M2_xyz = euler_xyz(phi, theta, psi)
    # M3_xyz = Mat4x4.rotation_euler(phi, theta, psi, "XYZ")
    #
    # print(M1_xyz)
    # print()
    # print(M2_xyz)
    # print()
    # print(M3_xyz)
    #
    # print(is_same_matrix(M1_xyz, M2_xyz))
    # print(is_same_matrix(M1_xyz, M3_xyz))
    #
    # print("Euler base: ", phi, theta, psi)
    # print("Euler calc: ", *rotation_matrix_to_euler_xyz(M3_xyz))

    ################################
    phi, theta, psi = np.radians(30), np.radians(90), np.radians(45)
    M3_xyz = Mat4x4.rotation_euler(phi, theta, psi, "XYZ")
    phi1, theta1, psi1 = rotation_matrix_to_euler_xyz(M3_xyz)
    M4_xyz = Mat4x4.rotation_euler(phi1, theta1, psi1, "XYZ")
    M5_xyz = Mat4x4.rotation_euler(phi, theta, np.radians(44), "XYZ")

    print(M3_xyz)
    print()
    print(M4_xyz)
    print()
    print(M5_xyz)

    print("Euler base: ", np.degrees(phi), np.degrees(theta), np.degrees(psi))
    print("Euler calc: ", np.degrees(phi1), np.degrees(theta1), np.degrees(psi1))
    print(f"IS THE SAME: { is_same_matrix(M3_xyz, M4_xyz)}")


    u1 = Vec3(1, 0, 0)
    w1 = M3_xyz * u1
    u2 = Vec3(0, 1, 0)
    w2 = M3_xyz * u2

    print(w1)
    print(w2)

# ###########################
#     print("===========================")
#     M1_zxz = euler_zxz(phi, theta, psi)
#     M2_zxz = euler_zxz_rotation_matrix(phi, theta, psi)
#     M3_zxz = Mat4x4.rotation_euler(phi, theta, psi, "ZXZ")
#
#     print(M1_zxz)
#     print()
#     print(M2_zxz)
#     print(M2_zxz)
#
#     print(is_same_matrix(M1_zxz, M2_zxz))
#     print(is_same_matrix(M1_zxz, M3_zxz))
