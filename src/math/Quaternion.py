import numpy as np

from src.math.Vec4 import Vec4


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
            elif isinstance(a[0], Vec4):
                self.q = np.array(a[0].xyzw)
            elif isinstance(a[0], (list, tuple, np.ndarray)) and len(a[0]) == 4:
                self.q = np.array(a[0])
            else:
                self.q = np.array([1, 0, 0, 0])  # Тривіальний кватерніон
        elif len(a) == 4:
            self.q = np.array(a)
        else:
            self.q = np.array([1, 0, 0, 0])  # Тривіальний кватерніон

    @property
    def w(self):
        return self.q[0]

    @property
    def x(self):
        return self.q[1]

    @property
    def y(self):
        return self.q[2]

    @property
    def z(self):
        return self.q[3]

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
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def norm2(self):
        return np.dot(self.q, self.q)

    def norm(self):
        return self.norm2() ** 0.5

    def normalize(self):
        norm_squared = self.norm()
        if norm_squared == 0:
            raise ZeroDivisionError("Неможливо нормалізувати нульовий кватерніон")
        self.q = self.q / float(norm_squared)

    def inverse(self):
        """Повертає обернений кватерніон."""
        norm_squared = np.dot(self.q, self.q)
        if norm_squared == 0:
            raise ZeroDivisionError("Неможливо обернути нульовий кватерніон")
        return Quaternion(self.conjugate().q / norm_squared)

    @staticmethod
    def rotation(axis, theta):
        """Створює кватерніон для обертання на кут theta навколо заданої осі."""
        cos_theta = np.cos(theta / 2)
        sin_theta = np.sin(theta / 2)
        axis = axis / np.linalg.norm(axis)  # Нормалізація осі
        return Quaternion(cos_theta, *(axis * sin_theta))

    @staticmethod
    def rotation_x(theta):
        """Створює кватерніон для обертання на кут theta навколо заданої осі."""
        cos_theta = np.cos(theta / 2)
        sin_theta = np.sin(theta / 2)
        axis = np.array((1, 0, 0))
        return Quaternion(cos_theta, *(axis * sin_theta))

    @staticmethod
    def rotation_y(theta):
        """Створює кватерніон для обертання на кут theta навколо заданої осі."""
        cos_theta = np.cos(theta / 2)
        sin_theta = np.sin(theta / 2)
        axis = np.array((0, 1, 0))
        return Quaternion(cos_theta, *(axis * sin_theta))

    @staticmethod
    def rotation_z(theta):
        """Створює кватерніон для обертання на кут theta навколо заданої осі."""
        cos_theta = np.cos(theta / 2)
        sin_theta = np.sin(theta / 2)
        axis = np.array((0, 0, 1))
        return Quaternion(cos_theta, *(axis * sin_theta))

    def rotate_vector(self, u):
        """Поворот 3D-вектора u навколо осі v на кут theta за допомогою кватерніона."""
        if isinstance(u, Vec4):
            vector_quaternion = Quaternion(0, *u.xyz)
        elif isinstance(u, (tuple, list, np.ndarray)) and len(u) == 3:
            vector_quaternion = Quaternion(0, *u)
        else:
            vector_quaternion = Quaternion()

        rotated = self * vector_quaternion * self.conjugate()
        return Vec4(rotated.x, rotated.y, rotated.z)

    def __str__(self):
        """Повертає строкове представлення кватерніона."""
        return f"({self.w} + {self.x}i + {self.y}j + {self.z}k)"

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    # Приклад використання
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    q3 = Quaternion(q1)  # Копіювання
    q4 = Quaternion()  # Тривіальний кватерніон
    q5 = Quaternion([9, 10, 11, 12])  # Ініціалізація зі списку
    q6 = Quaternion(np.array([13, 14, 15, 16]))  # Ініціалізація з numpy

    print("q1:", q1)
    print("q2:", q2)
    print("q3 (копія q1):", q3)
    print("q4 (тривіальний кватерніон):", q4)
    print("q5 (ініціалізований зі списку):", q5)
    print("q6 (ініціалізований з numpy-масиву):", q6)
    print("q1 + q2:", q1 + q2)
    print("q1 * q2:", q1 * q2)
    print("Спряжений q1:", q1.conjugate())

    q7 = Quaternion(q6)
    print("||q7||^2 =  ", q7.norm2())
    print("||q7|| =  ", q7.norm())
    print()
    q7.normalize()
    print("q7:", q7)
    print("||q7||^2 =  ", q7.norm2())
    print("||q7|| =  ", q7.norm())
