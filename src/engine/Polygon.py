import numpy as np

from src.base.broken_line import draw_broken_line
from src.base.scene import draw_scene
from src.engine.BaseModel import BaseModel
from src.math.Vec3 import vertex, Vec3


class Polygon(BaseModel):
    AVAILABLE_PARAMETERS = [
        "color",                 # default: , posible values:
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
        if all(isinstance(item, (float, int)) for item in vertices) and len(vertices) % 2 == 0:
            self._geometry = [vertex(vertices[i], vertices[i + 1]) for i in range(0, len(vertices), 2)]
        elif all(isinstance(item, Vec3) for item in vertices):
            self._geometry = list(vertices)
        elif all(isinstance(item, np.ndarray) and item.shape == (2,) for item in vertices):
            self._geometry = [vertex(*item) for item in vertices]
        elif all(isinstance(item, (tuple, list)) and len(item) == 2 for item in vertices):
            self._geometry = [vertex(*item) for item in vertices]
        else:
            raise ValueError("Data corrupted")

    def draw(self):
        transformed_geometry = self.transformed_geometry

        ps = [el.xy for el in transformed_geometry]
        ps.append(transformed_geometry[0].xy)  # closed line

        draw_broken_line(ps, **self._parameters)


def scene():
    m = Polygon()
    # m.set_geometry(
    #     np.array((0, 0)),
    #     np.array((2, 0)),
    #     np.array((2, 1)),
    #     np.array((1, 2)),
    #     np.array((0, 1))
    # )

    # m.set_geometry(
    #     np.array((0, 0)),
    #     np.array((2, 0)),
    #     np.array((2, 1)),
    #     np.array((1, 2)),
    #     np.array((0, 1))
    # )

    m.set_geometry(
        0, 0,
        2, 0,
        2, 1,
        1, 2,
        0, 1
    )

    # m.set_geometry(
    #     (0, 0),
    #     (2, 0),
    #     (2, 1),
    #     (1, 2),
    #     (0, 1)
    # )

    # m.set_geometry(
    #     vertex(0, 0),
    #     vertex(2, 0),
    #     vertex(2, 1),
    #     vertex(1, 2),
    #     vertex(0, 1)
    # )

    m["color"] = "red"
    m["line_style"] = "--"
    m["vertex_color"] = "grey"
    m["vertices_show"] = True
    m["labels"] = [
        (r'$P_1$', (-0.1, -0.3)),
        (r'$P_2$', (-0.15, 0.2)),
        (r'$P_3$', (-0.1, 0.1)),
        r"$P_4$",
        r"$P_5$",
    ]

    m.draw()

    m["color"] = "blue"
    m["line_style"] = "solid"

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
        coordinate_rect=(-1, -1, 6, 6),
        # grid_show=False,
        base_axis_show=False,
        axis_show=True,
        axis_color="red",
        axis_line_style="-."
    )
