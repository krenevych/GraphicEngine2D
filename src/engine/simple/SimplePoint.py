import numpy as np

from src.base.points import draw_point
from src.engine.Scene import Scene
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex


class SimplePoint:

    def __init__(self, x=0, y=0):
        self.vertex = vertex(x, y)
        self.transformation = Mat3x3()
        self.color = "black"

    def draw(self):
        ps = self.transformation * self.vertex
        draw_point(ps.xy, color=self.color)


if __name__ == '__main__':
    class SimplePointScene(Scene):
        def draw_scene(self):
            point = SimplePoint(1, 1)

            point.color = "blue"  # колір ліній
            point.draw()

            R = Mat3x3.rotation(np.radians(45))
            S = Mat3x3.scale(2, 3)
            T = Mat3x3.translation(1, 1)

            point.color = "red"  # колір ліній
            point.transformation = T * R * S
            point.draw()


    scene = SimplePointScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-2, -2, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()
    scene.draw_figures()
    scene.finalize()
