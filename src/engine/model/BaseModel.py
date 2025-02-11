from abc import abstractmethod, ABCMeta

import numpy as np

from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex, Vec3


class BaseModel(metaclass=ABCMeta):

    def __init__(self, *vertices):
        self._pivot = Vec3.point(0, 0)
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

    def set_parameters(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = value

    def __setitem__(self, param, value):
        if param in self._availible_parameters:
            self._parameters[param] = value
            return
        elif isinstance(param, int):
            pass # TODO:
        else:
            raise ValueError("Недопустимий параметер")

    def set_transformation(self, transformation):
        self._transformation = transformation

    @property
    def transformation(self):
        return self._transformation

    @property
    def transformed_geometry(self):
        p = Mat3x3.translation(self._pivot)
        p_inv = p.inverse()
        transformation = p * self.transformation * p_inv
        transformed_data = [transformation * point for point in self._geometry]

        return transformed_data

    def apply_transformation_to_geometry(self):
        self._geometry = self.transformed_geometry
        self.set_transformation(Mat3x3.identity())

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
