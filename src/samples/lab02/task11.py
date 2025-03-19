import numpy as np

from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

FIGURE_KEY = "rect"


class SceneSample(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self[FIGURE_KEY] = SimplePolygon(
            2, 3.4,
            4.9, 4,
            4.5, 6,
            1.6, 5.4
        )

        self[FIGURE_KEY].color = "blue"
        self[FIGURE_KEY].line_style = ":"

transformation = Mat3x3(2.934, -0.416, 2.000,
                        0.624, 1.956, 3.400,
                        0, 0, 1)

print(transformation)

transformation_inv = transformation.inverse()
#     0.326    0.069   -0.888
#    -0.104    0.489   -1.455
#     0.000    0.000    1.000

print(transformation_inv)


def frame1(scene):
    pass

def frame2(scene):
    rect = scene[FIGURE_KEY]
    rect.transformation = transformation_inv
    rect.color = "red"
    rect.line_style = "-"

    translation = transformation[:2, 2]
    print(f"{translation=}")

    i = transformation[:2, 0]
    j = transformation[:2, 1]
    print(f"{i=}")
    print(f"{j=}")

    s_x = np.linalg.norm(i)
    s_y = np.linalg.norm(j)

    print(f"{s_x=}")
    print(f"{s_y=}")

    scale_x = (2.934 ** 2 + 0.624 ** 2) ** 0.5
    scale_y = ((-0.416) ** 2 + 1.956 ** 2) ** 0.5
    print(f"{scale_x=}", f"{scale_y=}")

    transformation_1 = transformation * Mat3x3.scale(1 / scale_x, 1 / scale_y)
    print(transformation_1)

    print(np.linalg.norm(transformation_1[:2, 0]))
    print(np.linalg.norm(transformation_1[:2, 1]))

    print(np.linalg.norm(transformation_1[0, :2]))
    print(np.linalg.norm(transformation_1[0, :2]))

    cos_t = transformation_1[0, 0]
    sin_t = transformation_1[1, 0]
    angle = np.arctan2(sin_t, cos_t)
    print(angle, np.degrees(angle))

    print(Mat3x3.decompose_affine(transformation), sep="\n")  # checking


if __name__ == '__main__':
    scene = SceneSample(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -2, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )

    scene.add_frames(frame1, frame2)

    scene.show()
