from src.base.axes import draw_axis
from src.engine.model.BaseModel import BaseModel


class CoordinateFrame(BaseModel):

    def __init__(self, plt_axis):

        super().__init__(plt_axis,
            1,0,0,
            0,1,0,
            0,0,1,
        )

        self.line_style = "-"
        self.line_width = 1.0
        self.color = ("red", "green", "blue")

    def draw_model(self):
        P = self.pivot_transform
        P_inv = P.inverse()

        M = P * self.transformation * P_inv

        origin = M * self._pivot

        transformed_geometry = self.transformed_geometry
        ps = [el.xyz for el in transformed_geometry]

        ox = ps[0]
        oy = ps[1]
        oz = ps[2]

        draw_axis(
            self.plt_axis,
            origin, ox,
            color=self.color[0],
            linewidth=self.line_width,
            linestyle=self.line_style
        )

        draw_axis(
            self.plt_axis,
            origin, oy,
            color=self.color[1],
            linewidth=self.line_width,
            linestyle=self.line_style
        )

        draw_axis(
            self.plt_axis,
            origin, oz,
            color=self.color[2],
            linewidth=self.line_width,
            linestyle=self.line_style
        )

