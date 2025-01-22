import numpy as np
from scipy.spatial.transform import Rotation as R


EU = 'XYZ'
euler_angles_45_45_30 = [45, 45, 30]
# Створення об'єкта обертання
rotation = R.from_euler(EU, euler_angles_45_45_30, degrees=True)

rotation_matrix_45_45_30 = rotation.as_matrix()
print(rotation_matrix_45_45_30.T)


# Отримання кватерніона
quaternion = rotation.as_quat()  # Порядок: [x, y, z, w]
print("Кватерніон:", quaternion)

euler_angles_xyz = rotation.as_euler(EU, degrees=True)
print(f"Кути Ейлера {EU} :", euler_angles_xyz)
