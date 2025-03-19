from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

FIGURE_KEY = "rect"


class SceneSample(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self[FIGURE_KEY] = SimplePolygon(
            0, 0,
            1, 0,
            1, 1,
            0, 1
        )

        self[FIGURE_KEY].color = "blue"
        self[FIGURE_KEY].line_style = ":"


T_P = Mat3x3.translation(0.5, 0.5)
T_P_inv = T_P.inverse()

R = Mat3x3.rotation(60, False)

def frame1(scene: Scene):
    pass

def frame2(scene: Scene):
    rect: (SimplePolygon,) = scene[FIGURE_KEY]
    rect.color = "red"
    rect.transformation = T_P_inv  # перенесли фігуру, щоб опорна точка потрапила в початок координат


def frame3(scene: Scene):
    rect: (SimplePolygon,) = scene[FIGURE_KEY]
    rect.color = "orange"
    rect.transformation = R * T_P_inv  # поворот навколо початку координат, з урахуванням перенесення у початок координат оп.точки


def frame4(scene: Scene):
    rect: (SimplePolygon,) = scene[FIGURE_KEY]
    rect.line_style = "solid"
    rect.color = "green"
    rect.transformation = T_P * R * T_P_inv  # повертаємо опорну точку на її місце


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

    scene.add_frames(frame1,
                     frame2,
                     frame3,
                     frame4,
                     )


    scene.show()
