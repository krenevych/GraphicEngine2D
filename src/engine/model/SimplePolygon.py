import numpy as np

from src.base.broken_line import draw_broken_line
from src.base.poligon import draw_poly
from src.engine.model.Model import Model
from src.engine.scene.Scene import Scene
from src.math.Mat4x4 import Mat4x4


class SimplePolygon(Model):

    def __init__(self, plt_axis, *vertices,
                 color="grey",
                 edgecolor="black",
                 line_style="-",
                 line_width=1.0,
                 alpha=1.0
                 ):
        super().__init__(plt_axis, *vertices, color=color)

        self.edgecolor = edgecolor
        self.line_style = line_style
        self.line_width = line_width
        self.alpha = alpha

    def draw_model(self):
        transformed_geometry = self.transformed_geometry
        ps = [el.xyz for el in transformed_geometry]

        draw_poly(
            self.plt_axis,
            ps,
            alpha=self.alpha,
            edgecolor=self.edgecolor,
            facecolor=self.color
        )

        draw_broken_line(
            self.plt_axis,
            ps,
            color=self.edgecolor,
            linewidth=self.line_width,
            linestyle=self.line_style,
        )


if __name__ == '__main__':
    RECT_KEY = "rect"


    class SimplePolygonScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            polygon = SimplePolygon(self.plt_axis,
                                    0, 0, 0,
                                    0.5, 0, 0,
                                    0.5, 0.5, 0,
                                    0, 0.5, 0,
                                    edgecolor="red",

                                    )
            self[RECT_KEY] = polygon
            polygon.show_pivot()
            polygon.show_local_frame()


    ############## Frame 1 ##################
    def frame1(scene: Scene):
        rect: SimplePolygon = scene[RECT_KEY]

        rect.color = "blue"  # колір ліній
        rect.line_style = "--"  # стиль ліній
        rect.alpha = 0.3

        # T = Mat4x4.translation(1, 1, 1)
        # rect.set_transformation(T)
        rect.show_local_frame()


    ##############################################
    ##############################################

    Rz = Mat4x4.rotation_z(np.radians(45))
    Rx = Mat4x4.rotation_x(np.radians(15))
    S = Mat4x4.scale(2)
    T = Mat4x4.translation(1, 0, 0)


    ############## Frame 2 ##################
    def frame2(scene: Scene):
        rect: SimplePolygon = scene[RECT_KEY]

        rect.show_local_frame()

        R = Rz
        # R = Rx * Rz
        S = Mat4x4.scale(2)

        rect.color = "yellow"  # колір ліній
        rect.alpha = 1.0
        rect.transformation = (T * R * S)


    ############## Frame 3 ##################
    def frame3(scene: Scene):
        rect: SimplePolygon = scene[RECT_KEY]

        R = Rx * Rz

        rect.set_transformation(T * R * S)


    simple_scene = SimplePolygonScene(
        coordinate_rect=(-1, -1, -1, 2, 2, 2),  # розмірність системи координатps
        axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    )

    simple_scene.add_frames(
        frame1,
        frame2,
        frame3,
    )  # додаємо кадри на сцену

    simple_scene.show()
