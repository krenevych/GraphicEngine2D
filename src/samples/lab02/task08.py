from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3


class SceneSample(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self["rect"] = SimplePolygon(
            0, 0,
            1, 0,
            1, 1,
            0, 1
        )

        self["rect"].color = "blue"
        self["rect"].line_style = ":"

    def draw_figures(self):
        rect = self["rect"]
        rect.draw()

        T_P = Mat3x3.translation(-0.5, -0.5)
        T_P_inv = T_P.inverse()


        S = Mat3x3.scale(2, 3)


        rect.line_style = "solid"
        rect.color = "green"
        rect.set_transformation (T_P_inv * S * T_P ) # повертаємо опорну точку на її місце
        rect.draw()

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
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -2, 4, 4),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )
    scene.prepare()
    scene.draw()

    scene.finalize()


