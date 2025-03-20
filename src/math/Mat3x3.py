import numpy as np

from src.math.Rotations import rotation_matrix_x, rotation_matrix_y, rotation_matrix_z, get_rotation_angle
from src.math.Scale import scale_matrix
from src.math.Translation import translationMatrix2d
from src.math.Vec3 import Vec3


class Mat3x3:

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
            self.data = np.eye(3, dtype=float)
        elif len(data) == 9:
            elements = np.array(data, dtype=float)
            self.data = elements.reshape((3, 3))
        elif len(data) == 4:
            elements = np.array(data, dtype=float)
            elements = elements.reshape((2, 2))
            self.data = np.eye(3, dtype=float)
            self.data[:2, :2] = elements
            pass
        elif len(data) == 1:
            data = data[0]
            if isinstance(data, Mat3x3):
                # Якщо переданий об'єкт Matrix3x3
                self.data = np.copy(data.data)
            elif isinstance(data, (list, tuple, np.ndarray)):
                data = np.array(data)
                if data.shape == (3, 3):
                    # Якщо передана 3x3 матриця
                    self.data = np.array(data, dtype=float)
                elif data.shape == (2, 2):
                    # Якщо передана 2x2 матриця, доповнюємо до 3x3
                    self.data = np.eye(3, dtype=float)
                    self.data[:2, :2] = data
                else:
                    raise ValueError("Матриця повинна бути розміром 2x2 або 3x3.")
            else:
                raise TypeError("Непідтриманий тип даних для ініціалізації.")
        elif len(data) == 3 and all(isinstance(vec, Vec3) for vec in data):
            self.data = np.vstack([vec.data for vec in data])
        else:
            raise TypeError(
                "Непідтриманий тип даних для ініціалізації або недостатньо елементів для побудови матриці 3x3.")

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

    def __add__(self, other):
        """
        Реалізує додавання двох матриць Matrix3x3 або numpy.ndarray 3x3.
        """
        if not isinstance(other, (Mat3x3, np.ndarray)):
            raise TypeError("Додавання можливе лише з іншими об'єктами Matrix3x3 або numpy.ndarray 3x3.")
        if isinstance(other, Mat3x3):
            return Mat3x3(self.data + other.data)
        return Mat3x3(self.data + other)

    def __matmul__(self, other):
        """
        Реалізує множення матриці на іншу Matrix3x3, numpy.ndarray 3x3, або Vector3.
        """
        if not isinstance(other, (Mat3x3, np.ndarray, Vec3)):
            raise TypeError("Множення можливе лише з іншими об'єктами Matrix3x3 або numpy.ndarray 3x3.")
        if isinstance(other, Mat3x3):
            return Mat3x3(np.dot(self.data, other.data))
        if isinstance(other, Mat3x3):
            return Mat3x3(np.dot(self.data, other.data))
        elif isinstance(other, Vec3):
            return Vec3(np.dot(self.data, other.data))
        return Mat3x3(np.dot(self.data, other))

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
        return Mat3x3(np.linalg.inv(self.data))

    @staticmethod
    def identity():
        return Mat3x3(np.eye(3, dtype=float))

    @staticmethod
    def rotation(angle, is_radians=True):
        if not is_radians:
            angle = np.radians(angle)

        m = rotation_matrix_z(angle)
        return Mat3x3(m)

    @staticmethod
    def rotation_x(angle, is_radians=True):
        if not is_radians:
            angle = np.radians(angle)
        m = rotation_matrix_x(angle)
        return Mat3x3(m)

    @staticmethod
    def rotation_y(angle, is_radians=True):
        if not is_radians:
            angle = np.radians(angle)
        m = rotation_matrix_y(angle)
        return Mat3x3(m)

    @staticmethod
    def rotation_z(angle, is_radians=True):
        if not is_radians:
            angle = np.radians(angle)

        m = rotation_matrix_z(angle)
        return Mat3x3(m)

    @staticmethod
    def translation(tx, ty=None):
        if ty is None and isinstance(tx, Vec3):
            m = translationMatrix2d(*tx.xy)
        elif ty is None and isinstance(tx, np.ndarray):
            m = translationMatrix2d(tx[0], tx[1])
        else:
            m = translationMatrix2d(tx, ty)
        return Mat3x3(m)

    @staticmethod
    def scale(sx, sy=None):
        if sy is None and isinstance(sx, Vec3):
            m = scale_matrix(*sx.xy)
        elif sy is None and isinstance(sx, np.ndarray):
            m = scale_matrix(sx[0], sx[1])
        else:
            m = scale_matrix(sx, sy)
        return Mat3x3(m)

    @staticmethod
    def decompose_affine(transition):

        if not isinstance(transition, (np.ndarray, Mat3x3)):
            raise TypeError("Transformation error.")

        if isinstance(transition, Mat3x3):
            transition = transition.data

        if transition.shape != (3, 3):
            raise ValueError("Матриця повинна бути розміром 3x3.")

        # Виділення переносу
        translation = transition[:2, 2]

        # Виділення матриці RS
        rs = transition[:2, :2]

        # Обчислення масштабу
        scale_x = np.linalg.norm(rs[:, 0])
        scale_y = np.linalg.norm(rs[:, 1])
        scales = np.array([scale_x, scale_y])

        # Обчислення повороту
        rotation = rs / scales

        angle = get_rotation_angle(rotation)

        return translation, angle, scales


# Приклад використання
if __name__ == "__main__":
    # Ініціалізація різними способами
    m1 = Mat3x3([[1, 2], [3, 4]])  # 2x2
    print("Матриця 2x2, доповнена до 3x3:")
    print(m1)

    m2 = Mat3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 3x3
    print("Матриця 3x3:")
    print(m2)

    m22 = Mat3x3(([1, 2, 3], [4, 5, 6], [7, 8, 9]))  # 3x3 ########
    print("Матриця 3x3:")
    print(m22)

    m3 = Mat3x3(m2)  # Копіювання об'єкта
    print("Копія матриці 3x3:")
    print(m3)

    # Доступ до елементів і їх зміна
    print("Елемент [1, 2]:", m2[1, 2])
    m2[1, 2] = 42
    print("Матриця після зміни елемента [1, 2]:")
    print(m2)

    # Множення матриць
    m4 = m1 @ m2  # @ == *
    print("Результат множення матриць:")
    print(m4)

    # Додавання матриць
    m5 = m1 + m1
    print("Результат додавання матриць:")
    print(m5)

    # Поелементне множення матриць
    m6 = m2 * m2
    print("Результат множення матриць:")
    print(m6)

    # Обчислення оберненої матриці
    try:
        m1_inv = m1.inverse()
        print("Обернена матриця до m1:")
        print(m1_inv)

        m8 = m1_inv * m1
        print("m7 * m1:")
        print(m8)
    except ValueError as e:
        print(f"Помилка: {e}")

    # v = Vector3(1, 2, 3)

    m33 = Mat3x3(1, 4, 6,
                 1, 3, 5,
                 34, 5, -7
                 )

    print(m33)

    m11 = Mat3x3(55, 66,
                 77, 88)
    print(m11)

    print("======== розвʼязання системи алгебраїчних рівнянь ===============")
    # print("A:")
    # print(m44)

    b = Vec3(1, 2, 4)
    print("b =", b)

