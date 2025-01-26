import numpy as np

from src.base.scene import draw_scene
from src.engine.BaseModel import BaseModel
from src.engine.drawer import line2d
from src.math.Vec3 import vertex, Vec3


class Polygon(BaseModel):
    AVAILABLE_PARAMETERS = [
        "color",                 # default: , posible values:
        "closed",                # default: , posible values:
        "line_style",            # default: , posible values:
        "linewidth",             # default: , posible values:
        "vertices_show",         # default: , posible values:
        "vertex_color",          # default: , posible values:
        "vertex_size",           # default: , posible values:
        "labels",                # default: , posible values:
        "labels_color",          # default: , posible values:
        "labels_fontsize",       # default: , posible values:
    ]

    def __init__(self):
        super().__init__()
        self._availible_parameters += Polygon.AVAILABLE_PARAMETERS

    def set_geometry(self, *vertices):
        self._geometry = list(vertices)

    def draw(self):
        transformed_data = self.transformed_geometry
        line2d(*transformed_data, **self._parameters)


def scene():
    m = Polygon()
    m.set_geometry(
        vertex(0, 0),
        vertex(2, 0),
        vertex(2, 1),
        vertex(1, 2),
        vertex(0, 1)
    )

    m["closed"] = True
    m["color"] = "red"
    m["line_style"] = "--"
    m["vertex_color"] = "grey"
    m["vertices_show"] = True
    m["labels"] = [
        ('P1', (-0.1, -0.3)),
        ('P2', (-0.15, 0.2)),
        ('P3', (-0.1, 0.1)),
    ]


    m.draw()

    m.scale(2, 1)
    m.translation(Vec3.point(2, 2))
    m.rotation(np.radians(45))

    # S = Mat3x3.scale(2, 1)
    # T = Mat3x3.translation(Vec3.point(2, 2))
    # R = Mat3x3.rotation(np.radians(45))

    # transform = T * R * S
    # m.set_transformation(transform)

    m.draw()


if __name__ == '__main__':
    draw_scene(
        scene=scene,
        coordinate_rect=(-1, -1, 5, 5),
        # grid_show=False,
        base_axis_show=False,
        axis_show=True,
        axis_color="red",
        axis_line_style="-."
    )
