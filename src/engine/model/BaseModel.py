from abc import abstractmethod, ABCMeta

import numpy as np

from src.base.axes import draw_axis
from src.base.points import draw_point
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4, vertex


class BaseModel(metaclass=ABCMeta):
    AVAILABLE_PARAMETERS = []

    def __init__(self, plt_axis, *vertices):
        self.plt_axis = plt_axis

        self._geometry = self.build_geometry(*vertices)

        self._transformation = Mat4x4()
        self.color = "black"
        self.alpha = 1.0

        self.__pivot = Vec4.point()
        self.__is_draw_pivot = False
        self.__is_draw_local_frame = False

        self.__axis_color = ("red", "green", "blue")  # колір осей координат
        self.__axis_line_width = 1.0  # товщина осей координат
        self.__axis_line_style = "--"  # стиль ліній осей координат

        self._parameters = {}
        self._availible_parameters = BaseModel.AVAILABLE_PARAMETERS

    def set_geometry(self, *vertices):
        self._geometry = self.build_geometry(*vertices)

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
        self.set_transformation(Mat4x4.identity())

    def pivot(self, tx, ty, tz):
        if ty is None and isinstance(tx, Vec4):
            self.__pivot = Vec4(tx.xyz)
        else:
            self.__pivot = Vec4(tx, ty, tz, 1)

    def show_pivot(self, enabled=True):
        self.__is_draw_pivot = enabled

    def show_local_frame(self, enabled=True):
        self.__is_draw_local_frame = enabled

    @property
    def pivot_transform(self):
        pivot_tr = Mat4x4.translation(self.__pivot)
        return pivot_tr

    def set_local_frame_parameters(self,
                                   color=None,
                                   line_width=None,
                                   line_style=None
                                   ):
        if color is not None:
            if isinstance(color, str):
                self.__axis_color = (color, color)
            elif isinstance(color, (tuple, list)) and len(color) == 2:
                self.__axis_color = tuple(color)  # колір осей координат

        if line_width is not None:
            self.__axis_line_width = line_width  # товщина осей координат
        if line_style is not None:
            self.__axis_line_style = line_style  # стиль ліній осей координат

    def _draw_local_frame(self):
        if self.__is_draw_local_frame:
            P = self.pivot_transform
            P_inv = P.inverse()

            M = P * self.transformation * P_inv

            origin = M * self.__pivot
            ox = origin + self.transformation * Vec4.vect(1, 0, 0)
            oy = origin + self.transformation * Vec4.vect(0, 1, 0)
            oz = origin + self.transformation * Vec4.vect(0, 0, 1)

            draw_axis(
                self.plt_axis,
                origin, ox,
                color=self.__axis_color[0],
                linewidth=self.__axis_line_width,
                linestyle=self.__axis_line_style
            )

            draw_axis(
                self.plt_axis,
                origin, oy,
                color=self.__axis_color[1],
                linewidth=self.__axis_line_width,
                linestyle=self.__axis_line_style
            )

            draw_axis(
                self.plt_axis,
                origin, oz,
                color=self.__axis_color[2],
                linewidth=self.__axis_line_width,
                linestyle=self.__axis_line_style
            )

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
