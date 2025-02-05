from abc import abstractmethod, ABCMeta

from src.base.axes import draw_axis
from src.base.points import draw_point
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex, Vec3


class Base(metaclass=ABCMeta):
    AVAILABLE_PARAMETERS = []

    def __init__(self, *vertices):
        self._geometry = []
        self._transformation = Mat3x3()
        self.color = "black"

        self.__pivot = Vec3.point(0, 0)
        self.__is_draw_pivot = False
        self.__is_draw_local_frame = False

        self._parameters = {}
        self._availible_parameters = Base.AVAILABLE_PARAMETERS

    def set_parameters(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = value

    def __setitem__(self, param, value):
        if param not in self._availible_parameters:
            raise ValueError("Недопустимий параметер")
        self._parameters[param] = value

    def set_transformation(self, transformation):
        self._transformation = transformation

    @property
    def transformation(self):
        return self._transformation

    @property
    def transformed_geometry(self):
        P = self.pivot_transform
        P_inv = P.inverse()
        transformation = P * self.transformation * P_inv
        transformed_data = [transformation * point for point in self._geometry]

        return transformed_data

    def apply_transformation_to_geometry(self):
        self._geometry = self.transformed_geometry
        self.set_transformation(Mat3x3.identity())

    def pivot(self, tx, ty):
        if ty is None and isinstance(tx, Vec3):
            self.__pivot = Vec3(tx.xy)
        else:
            self.__pivot = Vec3(tx, ty, 1)

    def show_pivot(self, enabled=True):
        self.__is_draw_pivot = enabled

    def show_local_frame(self, enabled=True):
        self.__is_draw_local_frame = enabled

    @property
    def pivot_transform(self):
        pivot_tr = Mat3x3.translation(self.__pivot)
        return pivot_tr

    def _draw_local_frame(self):
        if self.__is_draw_local_frame:
            P = self.pivot_transform
            P_inv = P.inverse()

            M = P * self.transformation * P_inv

            origin = M * self.__pivot
            ox = self.__pivot + self.transformation * vertex(1, 0)
            oy = self.__pivot + self.transformation * vertex(0, 1)

            draw_axis(origin, ox, color="red", linewidth=2.)
            draw_axis(origin, oy, color="green", linewidth=2.)

    def _draw_pivot(self):
        if self.__is_draw_pivot:
            P = self.pivot_transform
            P_inv = P.inverse()

            pivot = P * self.transformation * P_inv * self.__pivot
            draw_point(pivot.xy, color="red")

    def draw(self):
        self.draw_model()
        self._draw_pivot()
        self._draw_local_frame()

    @abstractmethod
    def draw_model(self):
        pass