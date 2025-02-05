import numpy as np

from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

if __name__ == '__main__':
    class SampleScene(Scene):
        def draw_figures(self):
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

            rect.set_transformation(S)
            rect.color = "red"
            rect.line_style = "--"  # стиль ліній
            # малюємо полігон
            rect.draw()

            rect.line_style = "-"  # стиль ліній
            rect.set_transformation(R * S)
            rect.draw()

            rect.set_transformation(R)
            rect.color = "green"
            rect.line_style = "--"  # стиль ліній
            rect.draw()

            rect.set_transformation(T * R * S)
            rect.color = "orange"
            rect.line_style = "-."  # стиль ліній
            rect.draw()


    scene = SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-4, -4, 4, 4),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()
    scene.draw()
    scene.finalize()
