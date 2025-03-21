import pytest
import numpy as np
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4
from src.math.Vec3 import Vec3

# ========================  АРИФМЕТИЧНІ ОПЕРАЦІЇ  ===========================
# 1. Тест додавання двох матриць
def test_matrix_addition():
    mat1 = Mat4x4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    mat2 = Mat4x4(16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    result = mat1 + mat2
    expected = np.full((4, 4), 17, dtype=float)  # Сума відповідних елементів
    assert np.allclose(result.data, expected), "Помилка у додаванні матриць"

# 2. Тест віднімання двох матриць
def test_matrix_subtraction():
    mat1 = Mat4x4(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    mat2 = Mat4x4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    result = mat1 - mat2
    expected = np.full((4, 4), 10, dtype=float) - np.arange(1, 17).reshape(4, 4)
    assert np.allclose(result.data, expected), "Помилка у відніманні матриць"

# 3. Тест унарного мінуса
def test_matrix_negation():
    mat = Mat4x4(1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16)
    result = -mat
    expected = -mat.data
    assert np.allclose(result.data, expected), "Помилка у зміні знаку матриці"

# ========================  МНОЖЕННЯ  ===========================
# 4. Тест множення двох матриць
def test_matrix_multiplication():
    mat1 = Mat4x4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    mat2 = Mat4x4.identity()
    result = mat1 @ mat2
    assert np.allclose(result.data, mat1.data), "Помилка у множенні матриці на одиничну"

# 5. Тест множення матриці на вектор Vec4
def test_matrix_vector_multiplication():
    mat = Mat4x4.identity()
    vec = Vec4(3, 4, 5, 1)
    result = mat @ vec
    assert np.allclose(result.data, vec.data), "Помилка у множенні матриці на вектор"

# 6. Тест множення матриці на вектор Vec3
def test_matrix_vector3_multiplication():
    mat = Mat4x4.identity()
    vec = Vec3(3, 4, 5)
    result = mat * vec  # Має автоматично перевести Vec3 у Vec4 (з w=0)
    expected = Vec4(3, 4, 5)
    assert np.allclose(result.data, expected.data), "Помилка у множенні матриці на Vec3"

# ========================  ІНВЕРСІЯ І ТРАНСПОНУВАННЯ  ===========================
# 7. Тест знаходження оберненої матриці
def test_matrix_inverse():
    mat = Mat4x4(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2)
    inverse_mat = mat.inverse()
    expected = np.linalg.inv(mat.data)
    assert np.allclose(inverse_mat.data, expected), "Помилка у знаходженні оберненої матриці"

# 8. Тест транспонування матриці
def test_matrix_transpose():
    mat = Mat4x4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    transposed = mat.transpose()
    expected = mat.data.T
    assert np.allclose(transposed.data, expected), "Помилка у транспонуванні матриці"

# ========================  ОПЕРАЦІЇ З ОБЕРТАННЯМ  ===========================
# 9. Тест обертання навколо X
def test_rotation_x():
    mat = Mat4x4.rotation_x(90, is_radians=False)
    expected = np.array([[1, 0, 0, 0],
                         [0, 0, -1, 0],
                         [0, 1, 0, 0],
                         [0, 0, 0, 1]], dtype=float)
    assert np.allclose(mat.data, expected, atol=1e-6), "Помилка у матриці обертання навколо X"

# 10. Тест обертання навколо Y
def test_rotation_y():
    mat = Mat4x4.rotation_y(90, is_radians=False)
    expected = np.array([[0, 0, 1, 0],
                         [0, 1, 0, 0],
                         [-1, 0, 0, 0],
                         [0, 0, 0, 1]], dtype=float)
    assert np.allclose(mat.data, expected, atol=1e-6), "Помилка у матриці обертання навколо Y"

# 11. Тест обертання навколо Z
def test_rotation_z():
    mat = Mat4x4.rotation_z(90, is_radians=False)
    expected = np.array([[0, -1, 0, 0],
                         [1, 0, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]], dtype=float)
    assert np.allclose(mat.data, expected, atol=1e-6), "Помилка у матриці обертання навколо Z"

# ========================  МАСШТАБУВАННЯ І ТРАНСЛЯЦІЯ  ===========================
# 12. Тест масштабування
def test_matrix_scaling():
    mat = Mat4x4.scale(2, 3, 4)
    expected = np.array([[2, 0, 0, 0],
                         [0, 3, 0, 0],
                         [0, 0, 4, 0],
                         [0, 0, 0, 1]], dtype=float)
    assert np.allclose(mat.data, expected), "Помилка у матриці масштабування"

# 13. Тест трансляції
def test_matrix_translation():
    mat = Mat4x4.translation(3, 4, 5)
    expected = np.array([[1, 0, 0, 3],
                         [0, 1, 0, 4],
                         [0, 0, 1, 5],
                         [0, 0, 0, 1]], dtype=float)
    assert np.allclose(mat.data, expected), "Помилка у матриці трансляції"

# ========================  ПРОДОВЖЕННЯ ТЕСТІВ  ===========================

# 14. Тест множення матриці на скаляр (недозволена операція)
def test_matrix_scalar_multiplication():
    mat = Mat4x4.identity()
    with pytest.raises(TypeError, match="Множення можливе лише з іншими об'єктами Matrix4x4 або numpy.ndarray 4x4"):
        m2 = mat * 2  # Помилка: множення на число не підтримується

# 15. Тест знаходження норми матриці
def test_matrix_norm():
    mat = Mat4x4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    expected = np.linalg.norm(mat.data)
    assert np.isclose(mat.norm(), expected), "Помилка у знаходженні норми матриці"

# 16. Тест помилки при знаходженні оберненої матриці, якщо вона вироджена
def test_singular_matrix_inverse():
    singular_mat = Mat4x4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)  # Визначник = 0
    with pytest.raises(ValueError, match="Матриця не має оберненої"):
        singular_mat.inverse()

# 17. Тест правильності транспонування через `.T`
def test_matrix_transpose_property():
    mat = Mat4x4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    transposed = mat.T  # Використання властивості
    expected = mat.data.T
    assert np.allclose(transposed.data, expected), "Помилка у транспонуванні через .T"

# 18. Тест обертання у `Euler`-координатах (XYZ)
def test_rotation_euler_xyz():
    mat = Mat4x4.rotation_euler(30, 45, 60, configuration="xyz")
    assert mat is not None, "Помилка: обертання у системі Euler не працює"

# 19. Тест обертання у `Euler`-координатах (ZXZ)
def test_rotation_euler_zxz():
    mat = Mat4x4.rotation_euler(90, 45, 30, configuration="zxz")
    assert mat is not None, "Помилка: обертання у системі Euler (ZXZ) не працює"

# 20. Тест помилки для невідомої конфігурації `Euler`-обертання
def test_invalid_rotation_euler():
    with pytest.raises(ValueError, match=Mat4x4.ERROR_MESSAGE_EULER_CONFIG_UNKNOWN):
        Mat4x4.rotation_euler(30, 45, 60, configuration="abc")

# 21. Тест `toEuler()` для конфігурації XYZ
def test_toEuler_xyz():
    mat = Mat4x4.rotation_euler(30, 45, 60, configuration="xyz")
    angles = mat.toEuler("XYZ")
    assert len(angles) == 3, "Помилка у отриманні Euler-координат"

# 22. Тест `toEuler()` для конфігурації ZXZ
def test_toEuler_zxz():
    mat = Mat4x4.rotation_euler(30, 45, 60, configuration="zxz")
    angles = mat.toEuler("ZXZ")
    assert len(angles) == 3, "Помилка у отриманні Euler-координат (ZXZ)"

# 23. Тест помилки `toEuler()` для невідомої конфігурації
def test_toEuler_invalid():
    mat = Mat4x4.identity()
    with pytest.raises(ValueError, match=Mat4x4.ERROR_MESSAGE_EULER_CONFIG_UNKNOWN):
        mat.toEuler("ABC")

# 24. Тест масштабування з одним числом (рівномірний скейлінг)
def test_matrix_uniform_scaling():
    mat = Mat4x4.scale(3)
    expected = np.array([[3, 0, 0, 0],
                         [0, 3, 0, 0],
                         [0, 0, 3, 0],
                         [0, 0, 0, 1]], dtype=float)
    assert np.allclose(mat.data, expected), "Помилка у рівномірному масштабуванні"

# 25. Тест масштабування з `Vec3`
def test_matrix_scaling_vec3():
    vec = Vec3(2, 3, 4)
    mat = Mat4x4.scale(vec)
    expected = np.array([[2, 0, 0, 0],
                         [0, 3, 0, 0],
                         [0, 0, 4, 0],
                         [0, 0, 0, 1]], dtype=float)
    assert np.allclose(mat.data, expected), "Помилка у масштабуванні через Vec3"

# 26. Тест помилки для некоректного масштабування
def test_invalid_matrix_scaling():
    with pytest.raises(ValueError, match=Mat4x4.ERROR_MESSAGE_SCALE):
        Mat4x4.scale("invalid")

# 27. Тест трансляції за допомогою `Vec3`
def test_matrix_translation_vec3():
    vec = Vec3(3, 4, 5)
    mat = Mat4x4.translation(vec)
    expected = np.array([[1, 0, 0, 3],
                         [0, 1, 0, 4],
                         [0, 0, 1, 5],
                         [0, 0, 0, 1]], dtype=float)
    assert np.allclose(mat.data, expected), "Помилка у трансляції через Vec3"

# 28. Тест множення матриці на `numpy.ndarray`
def test_matrix_numpy_multiplication():
    mat = Mat4x4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    array = np.eye(4, dtype=float)
    result = mat @ array
    expected = np.dot(mat.data, array)
    assert np.allclose(result.data, expected), "Помилка у множенні матриці на numpy-масив"

# 29. Тест помилки при множенні на `numpy.ndarray` неправильного розміру
def test_invalid_numpy_multiplication():
    mat = Mat4x4.identity()
    invalid_array = np.eye(3)  # Некоректний розмір (3×3 замість 4×4)
    with pytest.raises(TypeError, match=Mat4x4.ERROR_MESSAGE_MULT):
        mat @ invalid_array

# 30. Тест помилки при обертанні навколо некоректного вектора
def test_invalid_rotation_vector():
    with pytest.raises(ValueError, match=Mat4x4.ERROR_MESSAGE_ROTATION):
        Mat4x4.rotation(45, [1, 2])  # Некоректний розмір вектора
