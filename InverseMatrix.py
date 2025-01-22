import numpy as np

# Квадратна матриця
A = np.array([
    [1, 0, 0, 3],
    [0, 1, 0, 5],
    [0, 0, 1, 9],
    [0, 0, 0, 1],
])

# Обчислення оберненої матриці
A_inv = np.linalg.inv(A)

print("Оригінальна матриця A:")
print(A)
print("\nОбернена матриця A:")
print(A_inv)
