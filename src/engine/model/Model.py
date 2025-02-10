from abc import ABC

from src.base.points import draw_point
from src.engine.model.BaseModel import BaseModel
from src.engine.model.CoordinateFrame import CoordinateFrame
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import vertex


class Model(BaseModel, ABC):

    def __init__(self, plt_axis, *vertices):
        super().__init__(plt_axis, *vertices)

        self._pivot = vertex()
        self._is_draw_pivot = False

        self._coord_frame = CoordinateFrame(self.plt_axis)
        self._coord_frame.line_style = "-"
        self._coord_frame.line_width = 1.0
        self._coord_frame.color = ("red", "green", "blue")
        self._is_draw_local_frame = False

        self.color = "grey"

    def show_pivot(self, enabled=True):
        self._is_draw_pivot = enabled

    def pivot(self, tx, ty=None, tz=None):
        super().pivot(tx, ty, tz)
        self._coord_frame.pivot(tx, ty, tz)

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
            pivot = p * self.transformation * p.inverse() * self._pivot
            draw_point(self.plt_axis, pivot.xyz, color="red")

    def apply_transformation_to_geometry(self):
        super().apply_transformation_to_geometry()

        self._coord_frame.apply_transformation_to_geometry()

    def draw(self):
        self._draw_local_frame()
        self.draw_model()
        self._draw_pivot()
