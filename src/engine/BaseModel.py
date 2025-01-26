from abc import ABC, abstractmethod

from src.base.scene import draw_axis
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import Vec3, vertex


class BaseModel(ABC):

    def __init__(self):
        self.__translation = Vec3.point()
        self.__rotation = 0.0
        self.__scale = Vec3(1, 1, 1)
        self.__pivot = Vec3.point(0, 0)
        self._geometry = []
        self._parameters = {}
        self._availible_parameters = []

    def set_parameters(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = value

    def __setitem__(self, param, value):
        if param not in self._availible_parameters:
            raise ValueError("Недопустимий параметер")
        self._parameters[param] = value

    def scale(self, sx, sy=None):
        if sy is None and isinstance(sx, Vec3):
            self.__scale = Vec3(*sx)
        else:
            self.__scale = Vec3(sx, sy, 1)

    def translation(self, tx, ty=None):
        if ty is None and isinstance(tx, Vec3):
            self.__translation = Vec3(*tx)
        else:
            self.__translation = Vec3(tx, ty, 1)

    def rotation(self, angle):
        self.__rotation = angle

    def pivot(self, tx, ty):
        # TODO: take into account...
        if ty is None and isinstance(tx, Vec3):
            self.__pivot = Vec3(tx.xy)
        else:
            self.__pivot = Vec3(tx, ty, 1)

    def set_transformation(self, transition):
        self.__translation, self.__rotation, self.__scale = Mat3x3.decompose_affine(transition)

    @property
    def transformation(self):
        T = Mat3x3.translation(self.__translation)
        R = Mat3x3.rotation(self.__rotation, True)
        S = Mat3x3.scale(self.__scale)

        return T * R * S

    def draw_local_frame(self):
        M = self.transformation

        origin = M * vertex(0, 0)
        ox = M * vertex(1, 0)
        oy = M * vertex(0, 1)

        draw_axis(origin, ox, color="red", linewidth=2.)
        draw_axis(origin, oy, color="green", linewidth=2.)

    @property
    def transformed_geometry(self):
        M = self.transformation
        transformed_data = []
        for point in self._geometry:
            _p = M * point
            transformed_data.append(_p)

        return transformed_data

    @abstractmethod
    def draw(self):
        pass
