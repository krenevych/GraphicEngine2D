import numpy as np

from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4

if __name__ == '__main__':


    transformation_matrix = (Mat4x4.translation(1, 2, 3)
                             * Mat4x4.rotation(np.radians(23), Vec4(1, 1, 1))
                             * Mat4x4.scale(3,
                                            4,
                                            5))
    T, S, R, axis, angle = Mat4x4.decompose_affine(transformation_matrix)
    
    # 🔹 Вивід результатів
    print("Трансляція (Translation):", T)
    print("Масштабування (Scale):", S)
    print("Матриця обертання (Rotation Matrix):\n", R)
    print("Вісь обертання (Rotation Axis):", axis)
    print("Кут обертання (Rotation Angle):", angle, "градусів")
