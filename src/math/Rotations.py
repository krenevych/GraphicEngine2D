import numpy as np


def rotation_matrix_x(phi):
    """
    Формує матрицю обертання навколо осі X на заданий кут.

    Parameters:
    theta (float): Кут обертання у радіанах.

    Returns:
    numpy.ndarray: Матриця обертання 3x3.
    """
    return np.array([
        [1,              0,               0,      0],
        [0,    np.cos(phi),    -np.sin(phi),      0],
        [0,    np.sin(phi),     np.cos(phi),      0],
        [0,              0,               0,      1]
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
        [ np.cos(phi),     0,     np.sin(phi),    0],
        [           0,     1,               0,    0],
        [-np.sin(phi),     0,     np.cos(phi),    0],
        [           0,     0,               0,    1]
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
        [np.cos(phi),   -np.sin(phi),     0,     0],
        [np.sin(phi),    np.cos(phi),     0,     0],
        [          0,              0,     1,     0],
        [          0,              0,     0,     1]
    ])


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
    print()
    print(Rx @ Ry @ Rz)

