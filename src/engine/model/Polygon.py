import numpy as np

from src.base.broken_line import draw_broken_line
from src.engine.model.BaseModelTRS import BaseModelTRS
from src.engine.scene.Scene import Scene


class Polygon(BaseModelTRS):
    AVAILABLE_PARAMETERS = [
        "color",  # default: , posible values:
        "line_style",  # default: , posible values:
        "linewidth",  # default: , posible values:
        "vertices_show",  # default: , posible values:
        "vertex_color",  # default: , posible values:
        "vertex_size",  # default: , posible values:
        "labels",  # default: , posible values:
        "labels_color",  # default: , posible values:
        "labels_fontsize",  # default: , posible values:
    ]

    def __init__(self, *vertices):
        super().__init__(*vertices)

        self._availible_parameters += Polygon.AVAILABLE_PARAMETERS

    def draw_model(self):
        transformed_geometry = self.transformed_geometry

        ps = [el.xy for el in transformed_geometry]
        ps.append(transformed_geometry[0].xy)  # closed line

        draw_broken_line(ps, **self._parameters)


if __name__ == '__main__':
    scene_figure_key = "polygon"

    class PolygonScene(Scene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            m = Polygon()

            m.set_geometry(
                0, 0,
                1, 0,
                1, 1,
                0, 1
            )
            # m.set_geometry(
            #     0, 0,
            #     2, 0,
            #     2, 1,
            #     1, 2,
            #     0, 1
            # )

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

            self[scene_figure_key] = m

    polygon_scene = PolygonScene(
        coordinate_rect=(-1, -1, 3, 3),
        # grid_show=False,
        base_axis_show=False,
        axis_show=True,
        axis_color="red",
        axis_line_style="-."
    )


    def frame1(scene: Scene):
        m: Polygon = scene[scene_figure_key]

        m.pivot(0.5, 0.5)
        m.show_pivot()
        # m.show_local_frame()

        m["color"] = "green"
        m["line_style"] = "--"
        # m["vertex_color"] = "grey"
        # m["vertices_show"] = True
        # m["labels"] = [
        #     (r'$P_1$', (-0.1, -0.3)),
        #     (r'$P_2$', (-0.15, 0.2)),
        #     (r'$P_3$', (-0.1, 0.1)),
        #     r"$P_4$",
        #     r"$P_5$",
        # ]

    def frame2(scene: Scene):
        m: Polygon = scene[scene_figure_key]
        m["color"] = "blue"
        m["line_style"] = "solid"

        # m.scale(2, 1)
        # m.translation(Vec3.point(2, 2))
        m.rotation(np.radians(45))


    polygon_scene.add_frames(frame1,
                             frame2
                             )

    polygon_scene.show()
