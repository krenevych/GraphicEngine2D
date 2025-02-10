from abc import ABC

from src.base.points import draw_point
from src.engine.model.BaseModel import BaseModel
from src.engine.model.CoordinateFrame import CoordinateFrame
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4


class Model(BaseModel, ABC):

    def __init__(self, plt_axis, *vertices):
        super().__init__(plt_axis, *vertices)

        self._pivot = Vec4.point()
        self._is_draw_pivot = False

        self._coord_frame = CoordinateFrame(self.plt_axis)
        self._coord_frame.line_style = "-"
        self._coord_frame.line_width = 1.0
        self._coord_frame.color = ("red", "green", "blue")
        self._is_draw_local_frame = False

        self.color = "grey"

    def show_pivot(self, enabled=True):
        self._is_draw_pivot = enabled

    def show_local_frame(self, enabled=True):
        self._is_draw_local_frame = enabled

    def set_local_frame_parameters(self,
                                   color=None,
                                   line_width=None,
                                   line_style=None
                                   ):
        self._coord_frame.set_parameters(
            color=color,
            line_width=line_width,
            line_style=line_style
        )

    def _draw_local_frame(self):
        if self._is_draw_local_frame:
            self._coord_frame.set_transformation(self._transformation)
            self._coord_frame.draw_model()

    def _draw_pivot(self):
        if self._is_draw_pivot:
            p = Mat4x4.translation(self._pivot)
            p_inv = p.inverse()

            pivot = p * self.transformation * p_inv * self._pivot
            draw_point(pivot.xy, color="red")

    def apply_transformation_to_geometry(self):
        super().apply_transformation_to_geometry()

        self._coord_frame.apply_transformation_to_geometry()

    def draw(self):
        self._draw_pivot()
        self._draw_local_frame()
        self.draw_model()
