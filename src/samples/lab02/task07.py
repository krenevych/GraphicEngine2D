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
        rect: (SimplePolygon,) = self["rect"]
        rect.draw()

        T_P = Mat3x3.translation(0.5, 0.5)
        T_P_inv = T_P.inverse()

        R = Mat3x3.rotation(60, False)

        rect.color = "red"
        # rect.transformation = R
        rect.set_transformation(T_P_inv)  # перенесли фігуру, щоб опорна точка потрапила в початок координат
        rect.draw()

        rect.color = "orange"
        rect.set_transformation(
            R * T_P_inv)  # поворот навколо початку координат, з урахуванням перенесення у початок координат оп.точки
        rect.draw()

        rect.line_style = "solid"
        rect.color = "green"
        rect.set_transformation(T_P * R * T_P_inv)  # повертаємо опорну точку на її місце
        rect.draw()


if __name__ == '__main__':
    scene = SceneSample(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, 2, 2),  # розмірність системи координат
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
