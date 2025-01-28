import numpy as np

from src.engine.Scene import Scene
from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Mat3x3 import Mat3x3

if __name__ == '__main__':
    class SampleScene(Scene):
        def draw_scene(self):
            rect = SimplePolygon(
                0, 0,
                1, 0,
                1, 1,
                0, 1,
            )

            rect.color = "grey"  # колір ліній
            rect.line_style = "-."  # стиль ліній
            rect.draw()

            R = Mat3x3.rotation(np.radians(45))
            S = Mat3x3.scale(2, 3)
            T = Mat3x3.translation(0.5, 0.9)

            rect.transformation = S
            rect.color = "red"
            rect.line_style = "--"  # стиль ліній
            # малюємо полігон
            rect.draw()

            rect.line_style = "-"  # стиль ліній
            rect.transformation = (R * S)
            rect.draw()

            rect.transformation = R
            rect.color = "green"
            rect.line_style = "--"  # стиль ліній
            rect.draw()

            rect.transformation = T * R * S
            rect.color = "orange"
            rect.line_style = "-."  # стиль ліній
            rect.draw()


    SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-4, -4, 4, 4),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).draw()
