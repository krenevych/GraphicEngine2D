import numpy as np


class Vec4:

    def __init__(self, *data):
        """
        Конструктор класу Vector3.
        Якщо дані не передані, створює нульовий вектор.
        Приймає:
        - список або масив із трьох елементів,
        - інший об'єкт Vector3.
        """
        if len(data) == 0:
            self.data = np.zeros(4, dtype=float)
        elif len(data) == 4:
            self.data = np.array(data, dtype=float)
        elif len(data) == 1:
            data = data[0]
            if isinstance(data, Vec4):
                self.data = np.copy(data.data)
            elif isinstance(data, (list, tuple, np.ndarray)):
                data = np.array(data)
                if data.shape == (4,):
                    self.data = data.astype(float)
                else:
                    raise ValueError("Вектор повинен містити рівно 3 елементи.")
            else:
                raise TypeError("Непідтриманий тип даних для ініціалізації.")
        else:
            raise TypeError("Непідтриманий тип даних для ініціалізації.")

    def __getitem__(self, index):
        """
        Отримання елемента вектора по індексу.
        """
        return self.data[index]

    def __setitem__(self, index, value):
        """
        Встановлення значення елемента вектора по індексу.
        """
        self.data[index] = value

    def __str__(self):
        """
        Повертає строкове представлення вектора.
        """
        return np.array2string(self.data, formatter={'float_kind': lambda x: f"{x:8.3f}"})

    def __add__(self, other):
        """
        Реалізує додавання двох векторів Vector3 або numpy.ndarray з 3 елементів.
        """
        if not isinstance(other, (Vec4, np.ndarray)):
            raise TypeError("Додавання можливе лише з іншими об'єктами Vector3 або numpy.ndarray із 3 елементів.")
        if isinstance(other, Vec4):
            return Vec4(self.data + other.data)
        return Vec4(self.data + other)

    def __sub__(self, other):
        """
        Реалізує віднімання двох векторів Vector3 або numpy.ndarray з 3 елементів.
        """
        if not isinstance(other, (Vec4, np.ndarray)):
            raise TypeError("Віднімання можливе лише з іншими об'єктами Vector3 або numpy.ndarray із 3 елементів.")
        if isinstance(other, Vec4):
            return Vec4(self.data - other.data)
        return Vec4(self.data - other)

    def __mul__(self, other):
        return self.dot(other)

    def dot(self, other):
        """
        Обчислює скалярний добуток з іншим вектором Vector3 або numpy.ndarray з 3 елементів.
        """
        if not isinstance(other, (Vec4, np.ndarray)):
            raise TypeError(
                "Скалярний добуток можливий лише з іншими об'єктами Vector3 або numpy.ndarray із 3 елементів.")
        if isinstance(other, Vec4):
            return np.dot(self.data, other.data)
        return np.dot(self.data, other)

    def cross(self, other):
        """
        Обчислює векторний добуток з іншим вектором Vector3 або numpy.ndarray з 3 елементів.
        """
        if not isinstance(other, (Vec4, np.ndarray)):
            raise TypeError(
                "Векторний добуток можливий лише з іншими об'єктами Vector3 або numpy.ndarray із 3 елементів.")
        if isinstance(other, Vec4):
            return Vec4(np.cross(self.data, other.data))
        return Vec4(np.cross(self.data, other))

    # def __matmul__(self, other):
    #     """
    #     Реалізує множення вектора на матрицю Matrix3x3.
    #     """
    #     if not isinstance(other, Matrix3x3):
    #         raise TypeError("Множення можливе лише з об'єктами Matrix3x3.")
    #     return Vector3(np.dot(self.data, other.data))

    @property
    def xy(self):
        return self.data[:2]

    @property
    def xyz(self):
        return self.data[:3]

    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]

    @property
    def z(self):
        return self.data[2]


if __name__ == '__main__':
    v1 = Vec4()
    print(v1)

    v2 = Vec4(1, 2, 3, 4)
    print(v2)

    # v22 = Vec4((1, 2, 3, 4))
    # print(v2)

    v3 = Vec4(v2)
    print(v3)

    v4 = Vec4([1, 3, 5, 4])
    print(v4)

    v5 = Vec4(np.array((1, 4, 7, 5)))
    print(v5)

    print(v1 + v3)
    print(v2 * v3)

    v9 = Vec4(1, "232", 8, 3)
    print(v9)
