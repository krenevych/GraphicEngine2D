import numpy as np

from src.engine.model.Polygon import Polygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

FIGURE_KEY = "rect"

if __name__ == '__main__':
    class SampleScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            rect = Polygon(
                0, 0,
                1, 0,
                1, 1,
                0, 1
            )
            self[FIGURE_KEY] = rect


    S_2 = Mat3x3(
        2, 0, 0,
        0, 1, 0,
        0, 0, 1,
    )
    print("=== Scale (manual) ====")
    print(S_2)

    S_2 = Mat3x3.scale(2, 1)
    print("=== Scale (from Mat3x3) ====")
    print(S_2)

    R_45 = Mat3x3(
        np.cos(np.radians(45)), -np.sin(np.radians(45)), 0,
        np.sin(np.radians(45)), np.cos(np.radians(45)), 0,
        0, 0, 1
    )
    print("=== Rotation ====")
    print(R_45)


    def frame1(scene):
        rect: Polygon = scene[FIGURE_KEY]
        rect.color = "blue"
        rect.line_style = ":"


    def frame2(scene):
        rect: Polygon = scene[FIGURE_KEY]
        rect.transformation = S_2
        rect.color = "red"
        rect.line_style = ":"


    def frame3(scene):
        rect: Polygon = scene[FIGURE_KEY]
        rect.transformation = R_45 * S_2
        rect.color = "blue"
        rect.line_style = "-"


    scene = SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-3, -1, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )
    scene.add_frames(
        frame1,
        frame2,
        frame3,
    )
    scene.show()
