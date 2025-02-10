import numpy as np

from src.math.Rotations import rotation_matrix_z, rotation_matrix_x, rotation_matrix_y
from src.math.Scale import scale_matrix
from src.math.Translation import translation_matrix
from src.math.Vec4 import Vec4


class Mat4x4:

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
            elements = np.array(data, dtype=float)
            elements = elements.reshape((2, 2))
            self.data = np.eye(4, dtype=float)
            self.data[:2, :2] = elements
            pass
        elif len(data) == 1:
            data = data[0]
            if isinstance(data, Mat4x4):
                # Якщо переданий об'єкт Matrix4x4
                self.data = np.copy(data.data)
            elif isinstance(data, (list, tuple, np.ndarray)):
                data = np.array(data)
                if data.shape == (4, 4):
                    # Якщо передана 4x4 матриця
                    self.data = np.array(data, dtype=float)
                elif data.shape == (3, 3):
                    # Якщо передана 2x2 матриця, доповнюємо до 3x3
                    self.data = np.eye(4, dtype=float)
                    self.data[:3, :3] = data
                elif data.shape == (2, 2):
                    # Якщо передана 2x2 матриця, доповнюємо до 3x3
                    self.data = np.eye(4, dtype=float)
                    self.data[:2, :2] = data
                else:
                    raise ValueError("Матриця повинна бути розміром 2x2 або 3x3 a,j 4x4.")
            else:
                raise TypeError("Непідтриманий тип даних для ініціалізації.")
        else:
            raise TypeError(
                "Непідтриманий тип даних для ініціалізації або недостатньо елементів для побудови матриці 4x4.")

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

    def __str__(self):
        """
        Повертає строкове представлення матриці.
        """
        return np.array2string(self.data, formatter={'float_kind': lambda x: f"{x:8.3f}"})

    def __matmul__(self, other):
        """
        Реалізує множення матриці на іншу Matrix3x3, numpy.ndarray 3x3, або Vector3.
        """
        if not isinstance(other, (Mat4x4, np.ndarray, Vec4)):
            raise TypeError("Множення можливе лише з іншими об'єктами Matrix4x4 або numpy.ndarray 4x4.")
        if isinstance(other, Mat4x4):
            return Mat4x4(np.dot(self.data, other.data))
        if isinstance(other, Mat4x4):
            return Mat4x4(np.dot(self.data, other.data))
        elif isinstance(other, Vec4):
            # v = Vec4(np.dot(self.data, other.data))
            # return v
            return Vec4(np.dot(self.data, other.data))
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

    def __mul__(self, other):
        """
        Реалізує множення матриці на іншу Matrix3x3, numpy.ndarray 3x3, або Vector3.
        """
        return self.__matmul__(other)

    def inverse(self):
        """
        Обчислює обернену матрицю.
        """
        if np.linalg.det(self.data) == 0:
            raise ValueError("Матриця не має оберненої (визначник дорівнює нулю).")
        return Mat4x4(np.linalg.inv(self.data))


    @staticmethod
    def identity():
        return Mat4x4()

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
    def rotation(psi, v):
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
        Rz = Mat4x4.rotation_z(psi)

        Ry_1 = Ry.inverse()
        Rx_1 = Rx.inverse()

        return Ry_1 * Rx_1 * Rz * Rx * Ry

    @staticmethod
    def translation(tx, ty=None, tz=None):
        if ty is None and isinstance(tx, Vec4):
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
        elif sy is None and isinstance(sx, (Vec4,)):
            m = scale_matrix(*sx.xyz)
        elif sy is None and isinstance(sx, np.ndarray) and len(sx) == 3:
            m = scale_matrix(sx[0], sx[1], sx[2])
        elif isinstance(sx, (int, float)) and isinstance(sy, (int, float)) and isinstance(sz, (int, float)):
            m = scale_matrix(sx, sy, sz)
        else:
            raise ValueError("Недостатньо даних, щоб сформувати матрицю розтягу")
        return Mat4x4(m)


    @staticmethod
    def decompose_affine(transition):

        if not isinstance(transition, (np.ndarray, Mat4x4)):
            raise TypeError("Transformation error.")

        if isinstance(transition, Mat4x4):
            transition = transition.data

        if transition.shape != (4, 4):
            raise ValueError("Матриця повинна бути розміром 4x4.")

        # Виділення переносу
        translation = transition[:3, 3]

        # Виділення матриці RS
        rs = transition[:3, :3]

        # Обчислення масштабу
        scale_x = np.linalg.norm(rs[:, 0])
        scale_y = np.linalg.norm(rs[:, 1])
        scale_z = np.linalg.norm(rs[:, 2])
        scales = np.array([scale_x, scale_y, scale_z])

        # Обчислення повороту
        rotation = rs / scales

        # angle = get_rotation_angle(rotation)

        return translation, rotation, scales


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
