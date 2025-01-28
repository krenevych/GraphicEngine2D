from abc import ABC, abstractmethod

from src.base.axes import draw_axis
from src.base.points import draw_point
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import Vec3, vertex


class BaseModel(ABC):
    BASE_AVAILABLE_PARAMETERS = [
    ]

    def __init__(self):
        self.__translation = Vec3.point()
        self.__rotation = 0.0
        self.__scale = Vec3(1, 1, 1)
        self.__pivot = Vec3.point(0, 0)
        self._geometry = []
        self._parameters = {}
        self._availible_parameters = BaseModel.BASE_AVAILABLE_PARAMETERS
        self.__is_draw_pivot = False
        self.__is_draw_local_frame = False

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
        if ty is None and isinstance(tx, Vec3):
            self.__pivot = Vec3(tx.xy)
        else:
            self.__pivot = Vec3(tx, ty, 1)

    def show_pivot(self, enabled=True):
        self.__is_draw_pivot = enabled

    def show_local_frame(self, enabled=True):
        self.__is_draw_local_frame = enabled

    def set_transformation(self, transformation):
        self.__translation, self.__rotation, self.__scale = Mat3x3.decompose_affine(transformation)

    @property
    def transformation(self):
        P = Mat3x3.translation(self.__pivot)
        P_inv = P.inverse()

        T = Mat3x3.translation(self.__translation)
        R = Mat3x3.rotation(self.__rotation, True)
        S = Mat3x3.scale(self.__scale)

        return P * T * R * S * P_inv

    def __draw_local_frame(self):
        if self.__is_draw_local_frame:
            M = self.transformation

            origin = M * vertex(0, 0)
            ox = M * vertex(1, 0)
            oy = M * vertex(0, 1)

            draw_axis(origin, ox, color="red", linewidth=2.)
            draw_axis(origin, oy, color="green", linewidth=2.)

    def __draw_pivot(self):
        if self.__is_draw_pivot:
            pivot = self.transformation * self.__pivot
            draw_point(pivot.xy, color="red")

    @property
    def transformed_geometry(self):
        M = self.transformation
        transformed_data = []
        for point in self._geometry:
            _p = M * point
            transformed_data.append(_p)

        return transformed_data

    @abstractmethod
    def draw_model(self):
        pass

    def draw(self):
        self.draw_model()
        self.__draw_pivot()
        self.__draw_local_frame()
