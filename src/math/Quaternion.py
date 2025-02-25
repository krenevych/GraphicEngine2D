import numpy as np

class Quaternion:
    def __init__(self, *a):
        """
        Ініціалізація кватерніона з підтримкою копіювання.
        Якщо передано один аргумент і це інший кватерніон, створюється його копія.
        Якщо передано 4 аргументи - створюється відповідний кватерніон.
        Якщо аргументи відсутні - створюється тривіальний кватерніон (1, 0, 0, 0).
        Додано підтримку списків, кортежів та numpy-масивів.
        """
        if len(a) == 1:
            if isinstance(a[0], Quaternion):
                self.q = np.array(a[0].q)
            elif isinstance(a[0], (list, tuple, np.ndarray)) and len(a[0]) == 4:
                self.q = np.array(a[0])
            else:
                self.q = np.array([1, 0, 0, 0])  # Тривіальний кватерніон
        elif len(a) == 4:
            self.q = np.array(a)
        else:
            self.q = np.array([1, 0, 0, 0])  # Тривіальний кватерніон

    def __add__(self, other):
        """Додавання двох кватерніонів."""
        return Quaternion(self.q + other.q)

    def __mul__(self, other):
        """Множення двох кватерніонів."""
        q0, q1, q2, q3 = self.q
        p0, p1, p2, p3 = other.q

        return Quaternion(
            q0 * p0 - q1 * p1 - q2 * p2 - q3 * p3,
            q0 * p1 + q1 * p0 + q2 * p3 - q3 * p2,
            q0 * p2 - q1 * p3 + q2 * p0 + q3 * p1,
            q0 * p3 + q1 * p2 - q2 * p1 + q3 * p0
        )

    def conjugate(self):
        """Повертає спряжений кватерніон."""
        return Quaternion(self.q[0], -self.q[1], -self.q[2], -self.q[3])

    @staticmethod
    def rotate_vector(u, v, theta):
        """Поворот 3D-вектора u навколо осі v на кут theta за допомогою кватерніона."""
        theta_rad = np.radians(theta / 2)
        cos_theta = np.cos(theta_rad)
        sin_theta = np.sin(theta_rad)
        v = v / np.linalg.norm(v)  # Нормалізація осі обертання
        rotation_quaternion = Quaternion(cos_theta, *(v * sin_theta))
        rotation_conjugate = rotation_quaternion.conjugate()
        vector_quaternion = Quaternion(0, *u)
        rotated_vector = rotation_quaternion * vector_quaternion * rotation_conjugate
        return np.array([rotated_vector.q[1], rotated_vector.q[2], rotated_vector.q[3]])

    def __repr__(self):
        """Повертає строкове представлення кватерніона."""
        return f"({self.q[0]} + {self.q[1]}i + {self.q[2]}j + {self.q[3]}k)"

if __name__ == "__main__":
    # Приклад використання
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    q3 = Quaternion(q1)  # Копіювання
    q4 = Quaternion()  # Тривіальний кватерніон
    q5 = Quaternion([9, 10, 11, 12])  # Ініціалізація зі списку
    q6 = Quaternion(np.array([13, 14, 15, 16]))  # Ініціалізація з numpy

    u = np.array([1, 0, 0])
    v = np.array([0, 0, 1])
    theta = 90
    rotated_u = Quaternion.rotate_vector(u, v, theta)
    print("Повернутий вектор:", rotated_u)

    print("q1:", q1)
    print("q2:", q2)
    print("q3 (копія q1):", q3)
    print("q4 (тривіальний кватерніон):", q4)
    print("q5 (ініціалізований зі списку):", q5)
    print("q6 (ініціалізований з numpy-масиву):", q6)
    print("q1 + q2:", q1 + q2)
    print("q1 * q2:", q1 * q2)
    print("Спряжений q1:", q1.conjugate())
