import numpy as np

from src.base.broken_line import draw_broken_line
from src.engine.model.Model import Model
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3


class SimplePolygon(Model):

    def __init__(self, *vertices):
        super().__init__(*vertices)

        self.line_style = "-"

    def draw_model(self):
        transformed_geometry = self.transformed_geometry
        ps = [el.xy for el in transformed_geometry]
        ps.append(transformed_geometry[0].xy)  # closed line

        draw_broken_line(ps, color=self.color, line_style=self.line_style)


if __name__ == '__main__':
    scene_figure_key = "rect"


    class SimplePolygonScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            rect = SimplePolygon(0, 0,
                                 1, 0,
                                 1, 1,
                                 0, 1,
                                 )

            self[scene_figure_key] = rect


    ############## Frame 1 ##################
    def frame1(scene: Scene):
        rect: SimplePolygon = scene[scene_figure_key]

        rect.color = "blue"  # колір ліній
        rect.line_style = "--"  # стиль ліній


    ############## Frame 2 ##################
    def frame2(scene: Scene):
        rect: SimplePolygon = scene[scene_figure_key]

        R = Mat3x3.rotation(np.radians(45))
        S = Mat3x3.scale(2, 3)
        T = Mat3x3.translation(1, 1)

        rect.color = "red"  # колір ліній
        rect.line_style = "-"  # стиль ліній
        rect.transformation = T * R * S


    scene = SimplePolygonScene(
        coordinate_rect=(-2, -2, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    )
    scene.add_frames(frame1,
                     frame2,
                     ) # додаємо кадри на сцену

    scene.show()
