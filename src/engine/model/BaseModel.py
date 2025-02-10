from abc import abstractmethod, ABCMeta

import numpy as np

from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4, vertex


class BaseModel(metaclass=ABCMeta):

    def __init__(self, plt_axis, *vertices):
        self.plt_axis = plt_axis

        self._pivot = vertex()
        self._geometry = self.build_geometry(*vertices)
        self._transformation = Mat4x4()

    def set_geometry(self, *vertices):
        self._geometry = self.build_geometry(*vertices)

    def __getitem__(self, item):
        return Vec4(self._geometry[item])

    def build_geometry(self, *vertices):
        if len(vertices) == 0:
            geometry = []
        elif all(isinstance(item, (float, int)) for item in vertices) and len(vertices) % 3 == 0:
            geometry = [vertex(vertices[i], vertices[i + 1], vertices[i + 2]) for i in range(0, len(vertices), 3)]
        elif all(isinstance(item, Vec4) for item in vertices):
            geometry = list(vertices)
        elif all(isinstance(item, np.ndarray) and item.shape == (3,) for item in vertices):
            geometry = [vertex(*item) for item in vertices]
        elif all(isinstance(item, (tuple, list)) and len(item) == 3 for item in vertices):
            geometry = [vertex(*item) for item in vertices]
        else:
            raise ValueError("Data corrupted")

        return geometry

    def set_transformation(self, transformation):
        self._transformation = transformation

    @property
    def transformation(self):
        return self._transformation

    @property
    def transformed_geometry(self):
        p = Mat4x4.translation(self._pivot)
        p_inv = p.inverse()
        transformation = p * self.transformation * p_inv
        transformed_data = [transformation * point for point in self._geometry]

        return transformed_data

    def apply_transformation_to_geometry(self):
        self._geometry = self.transformed_geometry
        self.set_transformation(Mat4x4.identity())

    def pivot(self, tx, ty, tz):
        if ty is None and isinstance(tx, Vec4):
            self._pivot = Vec4(tx.xyz)
        else:
            self._pivot = Vec4(tx, ty, tz, 1)

    def draw(self):
        self.draw_model()

    @abstractmethod
    def draw_model(self):
        pass
