import numpy as np

from src.math.Quaternion import Quaternion


@staticmethod
def euler_xyz_to_quaternion(phi, theta, psi):
    """Обчислює кватерніон для кутів Ейлера (XYZ)."""
    cos_phi, sin_phi = np.cos(phi / 2), np.sin(phi / 2)
    cos_theta, sin_theta = np.cos(theta / 2), np.sin(theta / 2)
    cos_psi, sin_psi = np.cos(psi / 2), np.sin(psi / 2)

    return Quaternion(
        cos_phi * cos_theta * cos_psi - sin_phi * sin_theta * sin_psi,
        sin_phi * cos_theta * cos_psi + cos_phi * sin_theta * sin_psi,
        cos_phi * sin_theta * cos_psi - sin_phi * cos_theta * sin_psi,
        cos_phi * cos_theta * sin_psi + sin_phi * sin_theta * cos_psi
    )

if __name__ == '__main__':
    phi, theta, psi = np.radians(32), np.radians(45), np.radians(44)

    qi = Quaternion.rotation_x(phi)
    qj = Quaternion.rotation_y(theta)
    qk = Quaternion.rotation_z(psi)
    q = qi * qj * qk
    print(q)
    q_euler = euler_xyz_to_quaternion(phi, theta, psi)
    print(q_euler)
    print(q_euler - q)


    # u = Vec4(1, 0, 0)
    # print(u)
    # w = q.rotate_vector(u)
    # print(w)
