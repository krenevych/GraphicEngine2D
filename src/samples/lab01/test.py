from src.engine.model.Polygon import Polygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

FIGURE_KEY = "rect"

if __name__ == '__main__':
    def frame1(scene):
        rect: Polygon = scene[FIGURE_KEY]
        rect.color = "blue"
        rect.line_style = ":"


    def frame2(scene):
        rect: Polygon = scene[FIGURE_KEY]
        R = Mat3x3.rotation(65, is_radians=False)
        rect.transformation = R


    scene = Scene(
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

    scene[FIGURE_KEY] = Polygon(
        2, 2,
        3, 2,
        3, 3,
        2, 3
    )

    scene.add_frames(
        frame1,
        frame2,
    )
    scene.show()
