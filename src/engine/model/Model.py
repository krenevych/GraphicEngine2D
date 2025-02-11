from abc import ABC

from src.base.points import draw_point
from src.engine.model.BaseModel import BaseModel
from src.engine.model.CoordinateFrame import CoordinateFrame
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex


class Model(BaseModel, ABC):

    def __init__(self, *vertices):
        super().__init__(*vertices)

        self._pivot = vertex()
        self._is_draw_pivot = False

        self._coord_frame = CoordinateFrame()
        self._coord_frame.line_style = "-"
        self._coord_frame.line_width = 1.0
        self._coord_frame.color = ("red", "green")
        self._is_draw_local_frame = False

        self.color = "grey"


    def show_pivot(self, enabled=True):
        self._is_draw_pivot = enabled

    def pivot(self, tx, ty=None, tz=None):
        super().pivot(tx, ty)
        self._coord_frame.pivot(tx, ty)

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
            p = Mat3x3.translation(self._pivot)
            pivot = p * self.transformation * p.inverse() * self._pivot
            draw_point(pivot.xy, color="red")

    def apply_transformation_to_geometry(self):
        super().apply_transformation_to_geometry()

        self._coord_frame.apply_transformation_to_geometry()

    def draw(self):
        self._draw_local_frame()
        self.draw_model()
        self._draw_pivot()
