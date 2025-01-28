import numpy as np

from src.base.broken_line import draw_broken_line
from src.engine.Scene import Scene
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex


class SimplePolygon:

    def __init__(self, *vertices):
        assert all(isinstance(item, (float, int)) for item in vertices) and len(vertices) % 2 == 0

        self.__geometry = [vertex(vertices[i], vertices[i + 1]) for i in range(0, len(vertices), 2)]
        self.transformation = Mat3x3()
        self.color = "black"
        self.line_style = "-"

    @property
    def transformed_geometry(self):
        return [self.transformation * point for point in self.__geometry]

    def draw(self):
        transformed_geometry = self.transformed_geometry
        ps = [el.xy for el in transformed_geometry]
        ps.append(transformed_geometry[0].xy)  # closed line

        draw_broken_line(ps, color=self.color, line_style=self.line_style)





if __name__ == '__main__':
    class SimplePolygonScene(Scene):

        def draw_scene(self):
            rect = SimplePolygon(0, 0,
                                 1, 0,
                                 1, 1,
                                 0, 1,
                                 )

            rect.color = "blue"  # колір ліній
            rect.line_style = "--"  # стиль ліній
            rect.draw()

            R = Mat3x3.rotation(np.radians(45))
            S = Mat3x3.scale(2, 3)
            T = Mat3x3.translation(1, 1)

            rect.color = "red"  # колір ліній
            rect.line_style = "-"  # стиль ліній
            rect.transformation = T * R * S
            rect.draw()


    SimplePolygonScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-2, -2, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).draw()