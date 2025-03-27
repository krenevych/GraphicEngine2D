from src.engine.model.Polygon import Polygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

FIGURE_KEY = "rect"


class SceneSample(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self[FIGURE_KEY] = Polygon(
            0, 0,
            1, 0,
            1, 1,
            0, 1
        )

        self[FIGURE_KEY].color = "blue"
        self[FIGURE_KEY].line_style = ":"


T_P = Mat3x3.translation(-0.5, -0.5)
T_P_inv = T_P.inverse()
S = Mat3x3.scale(2, 3)


def frame1(scene):
    rect = scene[FIGURE_KEY]


def frame2(scene):
    rect = scene[FIGURE_KEY]
    rect.line_style = "solid"
    rect.color = "green"
    rect.transformation = T_P_inv * S * T_P  # повертаємо опорну точку на її місце

    print("зміщення P -> O")
    print(T_P)
    print("розтягу")
    print(S)
    print("повернення опорної точки в початкове положення")
    print(T_P_inv)
    print("загальна трансформація")
    print(rect.transformation)


if __name__ == '__main__':
    scene = SceneSample(
        coordinate_rect=(-1, -2, 4, 4),  # розмірність системи координат
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )

    scene.add_frames(frame1,
                     frame2,
                     )
    scene.show()
