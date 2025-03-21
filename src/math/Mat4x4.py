import numpy as np

from src.math.Mat3x3 import Mat3x3
from src.math.Rotations import rotation_matrix_z, rotation_matrix_x, rotation_matrix_y
from src.math.Scale import scale_matrix
from src.math.Translation import translation_matrix
from src.math.Vec3 import Vec3
from src.math.Vec4 import Vec4


class Mat4x4:
    ERROR_MESSAGE_CONSTRUCTOR = "Непідтриманий тип даних для ініціалізації або недостатньо елементів для побудови матриці 4x4."

    def __init__(self, *data):
        """
        Конструктор класу Matrix3x3.
        Якщо дані не передані, створює одиничну матрицю.
        Приймає:
        - 3x3 матрицю (numpy.ndarray),
        - список списків 2x2 або 3x3,
        - інший об'єкт Matrix3x3.
        """
        if len(data) == 0:
            # Якщо дані не передані, створюємо одиничну матрицю
            self.data = np.eye(4, dtype=float)
        elif len(data) == 16:
            elements = np.array(data, dtype=float)
            self.data = elements.reshape((4, 4))
        elif len(data) == 9:
            elements = np.array(data, dtype=float)
            elements = elements.reshape((3, 3))
            self.data = np.eye(4, dtype=float)
            self.data[:3, :3] = elements
        elif len(data) == 4:
            if all(isinstance(vec, Vec4) for vec in data):
                self.data = np.vstack([vec.data for vec in data])
            elif all(isinstance(vec, (np.ndarray, tuple, list)) for vec in data):
                self.data = np.vstack([vec for vec in data])
            elif all(isinstance(el, (float, int)) for el in data):
                elements = np.array(data, dtype=float)
                elements = elements.reshape((2, 2))
                self.data = np.eye(4, dtype=float)
                self.data[:2, :2] = elements
        elif len(data) == 1:
            data = data[0]
            if isinstance(data, Mat4x4):
                # Якщо переданий об'єкт Matrix4x4
                self.data = np.copy(data.data)
            elif isinstance(data, Mat3x3):
                # Якщо переданий об'єкт Matrix3x3
                self.data = np.eye(4, dtype=float)
                self.data[:3, :3] = data.data
            elif isinstance(data, (list, tuple, np.ndarray)):
                try:
                    data = np.array(data)
                    if data.shape == (4, 4):
                        # Якщо передана 4x4 матриця
                        self.data = np.array(data, dtype=float)
                    elif data.shape == (3, 3):
                        # Якщо передана 3x3 матриця, доповнюємо до 4x4
                        self.data = np.eye(4, dtype=float)
                        self.data[:3, :3] = data
                    elif data.shape == (2, 2):
                        # Якщо передана 2x2 матриця, доповнюємо до 4x4
                        self.data = np.eye(4, dtype=float)
                        self.data[:2, :2] = data
                    else:
                        raise ValueError(Mat4x4.ERROR_MESSAGE_CONSTRUCTOR)
                except ValueError:
                    raise ValueError(Mat4x4.ERROR_MESSAGE_CONSTRUCTOR)

            else:
                raise ValueError(Mat4x4.ERROR_MESSAGE_CONSTRUCTOR)
        else:
            raise ValueError(Mat4x4.ERROR_MESSAGE_CONSTRUCTOR)

    def __getitem__(self, indices):
        """
        Отримання елемента матриці по індексах (рядок, стовпчик).
        """
        row, col = indices
        return self.data[row, col]

    def __setitem__(self, indices, value):
        """
        Встановлення значення елемента матриці по індексах (рядок, стовпчик).
        """
        row, col = indices
        self.data[row, col] = value

    def __repr__(self):
        return str(self)

    def __str__(self):
        """
        Повертає строкове представлення матриці.
        """
        return np.array2string(self.data, formatter={'float_kind': lambda x: f"{x:8.3f}"})

    def __matmul__(self, other):
        """
        Реалізує множення матриці на іншу Matrix3x3, numpy.ndarray 3x3, або Vector3.
        """
        if not isinstance(other, (Mat4x4, np.ndarray, Vec3, Vec4)):
            raise TypeError("Множення можливе лише з іншими об'єктами Matrix4x4 або numpy.ndarray 4x4.")

        if isinstance(other, (np.ndarray,)) and other.shape != (4, 4):
            raise TypeError("Множення можливе лише з іншими об'єктами Matrix4x4 або numpy.ndarray 4x4.")

        if isinstance(other, Mat4x4):
            return Mat4x4(np.dot(self.data, other.data))
        elif isinstance(other, Vec4):
            v = Vec4(np.dot(self.data, other.data))
            # print(v)
            return v
        elif isinstance(other, Vec3):
            return self @ Vec4(other)
        return Mat4x4(np.dot(self.data, other))

    def __add__(self, other):
        """
        Реалізує додавання двох матриць Matrix3x3 або numpy.ndarray 3x3.
        """
        if not isinstance(other, (Mat4x4, np.ndarray)):
            raise TypeError("Додавання можливе лише з іншими об'єктами Matrix3x3 або numpy.ndarray 3x3.")
        if isinstance(other, Mat4x4):
            return Mat4x4(self.data + other.data)
        return Mat4x4(self.data + other)

    def __sub__(self, other):
        if not isinstance(other, (Mat4x4, np.ndarray)):
            raise TypeError("Додавання можливе лише з іншими об'єктами Matrix3x3 або numpy.ndarray 3x3.")
        if isinstance(other, Mat4x4):
            return Mat4x4(self.data - other.data)
        return Mat4x4(self.data - other)

    def __neg__(self):
        return Mat4x4(-self.data)

    def __mul__(self, other):
        """
        Реалізує множення матриці на іншу Matrix3x3, numpy.ndarray 3x3, або Vector3.
        """
        return self.__matmul__(other)

    def inverse(self):
        """
        Обчислює обернену матрицю.
        """
        det = np.linalg.det(self.data)
        if np.isclose(det, 0):
            raise ValueError("Матриця не має оберненої (визначник дорівнює нулю).")
        return Mat4x4(np.linalg.inv(self.data))

    def norm(self):
        return np.linalg.norm(self.data)

    @staticmethod
    def identity():
        return Mat4x4()

    @property
    def T(self):
        return Mat4x4(self.data.T)

    def transpose(self):
        return Mat4x4(self.data.transpose())

    @staticmethod
    def rotation_x(angle, is_radians=True):
        if not is_radians:
            angle = np.radians(angle)
        m = rotation_matrix_x(angle)
        return Mat4x4(m)

    @staticmethod
    def rotation_y(angle, is_radians=True):
        if not is_radians:
            angle = np.radians(angle)
        m = rotation_matrix_y(angle)
        return Mat4x4(m)

    @staticmethod
    def rotation_z(angle, is_radians=True):
        if not is_radians:
            angle = np.radians(angle)

        m = rotation_matrix_z(angle)
        return Mat4x4(m)

    @staticmethod
    def rotation(angle, v, is_radians=True):
        if not is_radians:
            angle = np.radians(angle)

        if isinstance(v, (Vec4,)):
            v = v.xyz
        elif isinstance(v, (np.ndarray, tuple, list,)):
            v = np.array(v)
            if v.shape == (3,):
                v = v.astype(float)
            else:
                raise ValueError("Вектор повороту повинен містити рівно 3 дійсних елементи.")

        norm = np.linalg.norm(v)

        # Нормалізований вектор
        if norm != 0:
            normalized_v = v.data / norm
        else:
            normalized_v = v  # Для нульового вектора нормалізація не визначена

        ux, uy, uz = normalized_v

        phy = np.arctan2(ux, uz)
        # print(np.degrees(phy))
        len_ux_uz = np.linalg.norm((ux, uz))
        theta = np.arctan2(uy, len_ux_uz)
        # print(np.degrees(theta))

        Ry = Mat4x4.rotation_y(-phy)
        Rx = Mat4x4.rotation_x(theta)
        Rz = Mat4x4.rotation_z(angle)

        Ry_1 = Ry.inverse()
        Rx_1 = Rx.inverse()

        return Ry_1 * Rx_1 * Rz * Rx * Ry

    @staticmethod
    def rotation_euler(phi, theta, psi, configuration="xyz"):
        configuration = configuration.upper()
        if configuration == "XYZ":
            return Mat4x4.rotation_x(phi) * Mat4x4.rotation_y(theta) * Mat4x4.rotation_z(psi)
        elif configuration == "ZXZ":
            return Mat4x4.rotation_z(phi) * Mat4x4.rotation_x(theta) * Mat4x4.rotation_z(psi)
        else:
            raise ValueError("Unknown Euler configuration")

    def toEuler(self, configuration="XYZ"):
        configuration = configuration.upper()
        if configuration == "XYZ":
            return Mat4x4.toEulerXYZ(self)
        elif configuration == "ZXZ":
            return Mat4x4.toEulerZXZ(self)
        else:
            raise ValueError("Unknown Euler configuration")

    @staticmethod
    def toEulerXYZ(r):
        phi = np.arctan2(-r[1, 2], r[2, 2])
        theta = np.arcsin(r[0, 2])
        psi = np.arctan2(-r[0, 1], r[0, 0])
        return float(phi), float(theta), float(psi)

    @staticmethod
    def toEulerZXZ(r):
        phi = np.arctan2(r[0, 2], -r[1, 2])
        theta = np.arccos(r[2, 2])
        psi = np.arctan2(r[2, 0], r[2, 1])
        return float(phi), float(theta), float(psi)

    @staticmethod
    def translation(tx, ty=None, tz=None):
        if ty is None and isinstance(tx, (Vec3, Vec4)):
            m = translation_matrix(*tx.xyz)
        elif ty is None and isinstance(tx, np.ndarray):
            m = translation_matrix(tx[0], tx[1], tx[2])
        else:
            m = translation_matrix(tx, ty, tz)
        return Mat4x4(m)

    @staticmethod
    def scale(sx, sy=None, sz=None):
        if sy is None and isinstance(sx, (int, float)):
            m = scale_matrix(sx, sx, sx)
        elif sy is None and isinstance(sx, (Vec4, Vec3)):
            m = scale_matrix(*sx.xyz)
        elif sy is None and isinstance(sx, np.ndarray) and len(sx) == 3:
            m = scale_matrix(sx[0], sx[1], sx[2])
        elif isinstance(sx, (int, float)) and isinstance(sy, (int, float)) and isinstance(sz, (int, float)):
            m = scale_matrix(sx, sy, sz)
        else:
            raise ValueError("Недостатньо даних, щоб сформувати матрицю розтягу")
        return Mat4x4(m)


# Приклад використання
if __name__ == "__main__":
    # # Ініціалізація різними способами
    # m1 = Mat4x4([[1, 2], [3, 4]])  # 2x2
    # print("Матриця 2x2, доповнена до 4x4:")
    # print(m1)
    #
    # m2 = Mat4x4([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 4x4
    # print("Матриця 3x3, доповнена до 4x4:")
    # print(m2)
    #
    m44 = Mat4x4(1, 4, 6, 5,
                 1, 3, 5, 6,
                 34, 5, -7, 2,
                 7, 1, 9, 8
                 )
    print("Матриця 4x4 з послідовним задаванням елементів:")
    print(m44)
    #
    # m3 = Mat4x4(m44)  # Копіювання об'єкта
    # print("Копія матриці 4x4:")
    # print(m3)
    #
    # # Доступ до елементів і їх зміна
    # print("Елемент [1, 2]:", m3[1, 2])
    # m3[1, 2] = 42
    # print("Матриця після зміни елемента [1, 2]:")
    # print(m3)
    #
    # # Множення матриць
    # m4 = m1 @ m2
    # print("Результат множення матриць:")
    # print(m4)
    #
    # # Додавання матриць
    # m5 = m1 + m1
    # print("Результат додавання матриць:")
    # print(m5)
    #
    # # Поелементне множення матриць
    # m6 = m2 * m2
    # print("Результат поелементного множення матриць:")
    # print(m6)

    # Обчислення оберненої матриці
    m44_inv = Mat4x4()
    try:
        m44_inv = m44.inverse()
        print("Обернена матриця до m1:")
        print(m44_inv)

        m8 = m44_inv @ m44
        print("m7 * m44:")
        print(m8)


    except ValueError as e:
        print(f"Помилка: {e}")

    print("======== розвʼязання системи алгебраїчних рівнянь ===============")
    print("A:")
    print(m44)

    b = Vec4(1, 2, 3, 4)
    print("b =", b)

    x = m44_inv @ b
    print("x = ", x)

    b1 = m44 @ x
    print("b1 =", b1)

    print("-===================")
    m55 = Mat4x4(1, 2, 3, 4,
                 5, 6, 7, 8,
                 9, 10, 11, 12,
                 13, 14, 15, 16
                 )
    print(m55)
    print()
    print(m55.T)
    # print()
    # m55 = m55.transpose()
    print(m55)

    m1 = Mat4x4()

    print(m55 - m1)
