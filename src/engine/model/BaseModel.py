from abc import abstractmethod, ABCMeta

import numpy as np

from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex, Vec3
from src.math.utils_matrix import decompose_affine3, is_orthogonal


class BaseModel(metaclass=ABCMeta):

    def __init__(self, *vertices):
        self._pivot = vertex(0, 0)
        self._geometry = self.build_geometry(*vertices)
        self._transformation = Mat3x3()

        self._parameters = {}
        self._availible_parameters = []

    def set_geometry(self, *vertices):
        self._geometry = self.build_geometry(*vertices)

    def __getitem__(self, item):
        if isinstance(item, int):
            return Vec3(self._geometry[item])
        return None

    def build_geometry(self, *vertices):
        if len(vertices) == 0:
            geometry = []
        elif all(isinstance(item, (float, int)) for item in vertices) and len(vertices) % 2 == 0:
            geometry = [vertex(vertices[i], vertices[i + 1]) for i in range(0, len(vertices), 2)]
        elif all(isinstance(item, Vec3) for item in vertices):
            geometry = list(vertices)
        elif all(isinstance(item, np.ndarray) and item.shape == (2,) for item in vertices):
            geometry = [vertex(*item) for item in vertices]
        elif all(isinstance(item, (tuple, list)) and len(item) == 2 for item in vertices):
            geometry = [vertex(*item) for item in vertices]
        else:
            raise ValueError("Data corrupted")

        return geometry

    def __setitem__(self, param, value):
        pass

    @property
    def transformation(self):
        return self._transformation

    @transformation.setter
    def transformation(self, transformation):
        self._transformation = transformation

    @property
    def transformed_geometry(self):
        p = Mat3x3.translation(self._pivot)
        p_inv = p.inverse()
        transformation = p * self.transformation * p_inv
        transformed_data = [transformation * point for point in self._geometry]

        return transformed_data

    @property
    def rotation(self):
        translation, angle, scales = decompose_affine3(self._transformation)
        return angle

    @rotation.setter
    def rotation(self, rotation):
        translation, angle, scales = decompose_affine3(self._transformation)
        T = Mat3x3.translation(translation)
        S = Mat3x3.scale(scales)
        if isinstance(rotation, Mat3x3):
            assert is_orthogonal(rotation), "Matrix of rotarion has to be orthogonal"
            R = rotation
        elif isinstance(rotation, (float, int)):
            R = Mat3x3.rotation(rotation)
        else:
            raise ValueError("Parameter 'rotation' isn't actually rotation")

        self.transformation = T * R * S

    @property
    def scale(self):
        translation, angle, scales = decompose_affine3(self._transformation)
        return scales

    @scale.setter
    def scale(self, scale):
        translation, angle, current_scales = decompose_affine3(self._transformation)
        T = Mat3x3.translation(translation)
        S = Mat3x3.scale(scale)
        R = Mat3x3.rotation(angle)
        self.transformation = T * R * S

    @property
    def translation(self):
        translation, angle, scales = decompose_affine3(self._transformation)
        return translation

    @translation.setter
    def translation(self, translation):
        current_translation, angle, scales = decompose_affine3(self._transformation)
        T = Mat3x3.translation(translation)
        S = Mat3x3.scale(scales)
        R = Mat3x3.rotation(angle)
        self.transformation = T * R * S

    def apply_transformation_to_geometry(self):
        self._geometry = self.transformed_geometry
        self.transformation = Mat3x3.identity()

    def pivot(self, tx, ty):
        if ty is None and isinstance(tx, Vec3):
            self._pivot = Vec3(tx.xy)
        else:
            self._pivot = Vec3(tx, ty, 1)


    def draw(self):
        self.draw_model()

    @abstractmethod
    def draw_model(self):
        pass
