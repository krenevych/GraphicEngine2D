import pytest
import numpy as np
from src.math.Vec3 import Vec3  # Переконайся, що шлях правильний!

# 1. Створення вектора з двох чисел (третьою координатою має бути 0)
def test_vector_from_two_numbers():
    vec = Vec3(1, 2)
    expected = np.array([1, 2, 0], dtype=float)
    assert np.allclose(vec.data, expected), "Помилка: має бути вектор (1, 2, 0)"

# 2. Створення точки через статичний метод point()
def test_vector_point():
    vec = Vec3.point(3, 4)
    expected = np.array([3, 4, 1], dtype=float)
    assert np.allclose(vec.data, expected), "Помилка: point() має створити вектор (3, 4, 1)"

# 3. Створення точки point() без аргументів (має бути (0, 0, 1))
def test_vector_point_default():
    vec = Vec3.point()
    expected = np.array([0, 0, 1], dtype=float)
    assert np.allclose(vec.data, expected), "Помилка: point() без аргументів має створити (0, 0, 1)"

# 4. Перевірка нормалізації вектора (довжина має стати 1)
def test_vector_normalization():
    vec = Vec3(3, 4, 0)
    vec.normalize()
    expected_length = 1.0
    assert np.isclose(vec.norm(), expected_length), "Помилка: нормалізований вектор має мати довжину 1"

# 5. Перевірка повернення нового нормалізованого вектора (метод normalized)
def test_vector_normalized():
    vec = Vec3(3, 4, 0)
    normalized_vec = vec.normalized()
    expected_length = 1.0
    assert np.isclose(normalized_vec.norm(), expected_length), "Помилка: нормалізований вектор має мати довжину 1"
    assert not np.allclose(vec.data, normalized_vec.data), "Оригінальний вектор не має змінюватися"

# 6. Перевірка векторного добутку (cross product)
def test_vector_cross_product():
    vec1 = Vec3(1, 0, 0)
    vec2 = Vec3(0, 1, 0)
    cross_product = vec1.cross(vec2)
    expected = np.array([0, 0, 1], dtype=float)
    assert np.allclose(cross_product.data, expected), "Помилка: векторний добуток має бути (0, 0, 1)"

# 7. Перевірка помилки при некоректному вхідному значенні в cross()
def test_vector_cross_invalid():
    vec = Vec3(1, 0, 0)
    with pytest.raises(TypeError, match="Потрібен Vec3 або список із 4 елементів"):
        vec.cross([1, 2])  # Некоректний розмір вектора

# 8. Перевірка доступу до x, y, z через властивості
def test_vector_properties():
    vec = Vec3(5, 6, 7)
    assert vec.x == 5, "Помилка: x має бути 5"
    assert vec.y == 6, "Помилка: y має бути 6"
    assert vec.z == 7, "Помилка: z має бути 7"

# 9. Перевірка встановлення значень через властивості x, y, z
def test_vector_set_properties():
    vec = Vec3(0, 0, 0)
    vec.x = 9
    vec.y = 8
    vec.z = 7
    expected = np.array([9, 8, 7], dtype=float)
    assert np.allclose(vec.data, expected), "Помилка: значення x, y, z мають оновлювати вектор"

# 10. Перевірка правильного повернення підвекторів xy, xz, yz
def test_vector_subvectors():
    vec = Vec3(1, 2, 3)
    assert np.allclose(vec.xy, [1, 2]), "Помилка: xy має бути (1, 2)"
    assert np.allclose(vec.xz, [1, 3]), "Помилка: xz має бути (1, 3)"
    assert np.allclose(vec.yz, [2, 3]), "Помилка: yz має бути (2, 3)"
