import numpy as np

from src.math.Mat4x4 import Mat4x4
from src.math.Quaternion import Quaternion


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


def slerp(q0: Quaternion, q1: Quaternion, t):
    """
    Виконує сферичну лінійну інтерполяцію (SLERP) між двома кватерніонами q1 і q2.

    Параметри:
    q1, q2 : np.array (4,) - початковий та кінцевий кватерніони у форматі [x, y, z, w]
    t : float - параметр інтерполяції (0 ≤ t ≤ 1)

    Повертає:
    np.array (4,) - інтерпольований кватерніон
    """

    dot = q0.toVec4() * q1.toVec4()

    # Якщо косинус від'ємний, змінюємо знак одного кватерніона (коротший шлях)
    if dot < 0.0:
        q1 = -q1
        dot = -dot

    # Якщо кватерніони майже однакові, використовуємо лінійну інтерполяцію
    if dot > 0.9995:
        result = q0 * (1 - t) +  q1 * t
        return result.normalized()  # Нормалізація

    # Обчислення кута між кватерніонами
    theta_0 = np.arccos(dot)
    sin_theta_0 = np.sin(theta_0)

    # Вагові коефіцієнти
    s0 = np.sin((1 - t) * theta_0) / sin_theta_0
    s1 = np.sin(t * theta_0) / sin_theta_0

    # SLERP інтерполяція
    return q0 * s0 + q1 * s1



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


    q0 = Quaternion.rotation_y(phi)
    q1 = Quaternion.rotation_y(2 * phi)
    print("======================")
    print(q0)
    print(q1)
    print("======================")


    T = 10
    for i in range(T + 1):
        qt = slerp(q0, q1, i/T)
        # print(qt, qt.norm())
        print(qt)
