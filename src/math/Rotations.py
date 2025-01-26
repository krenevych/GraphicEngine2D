import numpy as np
from scipy.spatial.transform import Rotation as R

def rotationMatrix2d(phi):
    """
    Формує матрицю обертання навколо осі Z на заданий кут.

    Parameters:
    theta (float): Кут обертання у радіанах.

    Returns:
    numpy.ndarray: Матриця обертання 3x3.
    """
    return np.array([
        [np.cos(phi), -np.sin(phi), 0],
        [np.sin(phi),  np.cos(phi), 0],
        [0,                      0, 1]
    ])

def rotation_matrix_x(phi):
    """
    Формує матрицю обертання навколо осі X на заданий кут.

    Parameters:
    theta (float): Кут обертання у радіанах.

    Returns:
    numpy.ndarray: Матриця обертання 3x3.
    """
    return np.array([
        [1, 0, 0],
        [0, np.cos(phi), -np.sin(phi)],
        [0, np.sin(phi),  np.cos(phi)]
    ])

def rotation_matrix_y(phi):
    """
    Формує матрицю обертання навколо осі Y на заданий кут.

    Parameters:
    theta (float): Кут обертання у радіанах.

    Returns:
    numpy.ndarray: Матриця обертання 3x3.
    """
    return np.array([
        [np.cos(phi),  0, np.sin(phi)],
        [0,            1,           0],
        [-np.sin(phi), 0, np.cos(phi)]
    ])

def rotation_matrix_z(phi):
    """
    Формує матрицю обертання навколо осі Z на заданий кут.

    Parameters:
    theta (float): Кут обертання у радіанах.

    Returns:
    numpy.ndarray: Матриця обертання 3x3.
    """
    return np.array([
        [np.cos(phi), -np.sin(phi), 0],
        [np.sin(phi),  np.cos(phi), 0],
        [0,                      0, 1]
    ])


def get_rotation_angle(matrix):

    # Перевірка ортогональності R
    if not np.allclose(np.dot(rotation.T, rotation), np.eye(2)) or not np.isclose(np.linalg.det(rotation), 1):
        raise ValueError("Матриця не є коректною матрицею повороту.")

    """
    Обчислює кут повороту (в радіанах) із 2D матриці повороту.
    """
    if matrix.shape != (2, 2) and matrix.shape != (3, 3):
        raise ValueError("Некоректна матриця повороту!")

    if matrix.shape == (3, 3):
        matrix = matrix[:2, :2]

    # Витягуємо значення sin і cos
    cos_theta = matrix[0, 0]
    sin_theta = matrix[1, 0]

    # Обчислення кута через arctan2
    angle = np.arctan2(sin_theta, cos_theta)
    return angle


# Приклад використання:
if __name__ == "__main__":
    euler_angles_45_45_30 = [45, 15, 30]
    x = np.radians(euler_angles_45_45_30[0])  # Кут у градусах конвертується в радіани
    y = np.radians(euler_angles_45_45_30[1])  # Кут у градусах конвертується в радіани
    z = np.radians(euler_angles_45_45_30[2])  # Кут у градусах конвертується в радіани

    Rx = rotation_matrix_x(x)
    Ry = rotation_matrix_y(y)
    Rz = rotation_matrix_z(z)

    print("\nМатриця обертання послідовно по кутах ейлера:")
    # print(Rxyz)
    print()
    print(Rx @ Ry @ Rz)

    EU = 'XYZ'

    # Створення об'єкта обертання
    rotation = R.from_euler(EU, euler_angles_45_45_30, degrees=True)
    rotation_matrix_45_45_30 = rotation.as_matrix()
    print("\nМатриця обертання через scipy:")
    print(rotation_matrix_45_45_30)

    # # Отримання кватерніона
    # quaternion = rotation.as_quat()  # Порядок: [x, y, z, w]
    # print("Кватерніон:", quaternion)
    #
    # euler_angles_xyz = rotation.as_euler(EU, degrees=True)
    # print(f"Кути Ейлера {EU} :", euler_angles_xyz)
