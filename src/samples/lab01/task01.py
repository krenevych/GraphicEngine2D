from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

FIGURE_KEY = "rect"

if __name__ == '__main__':
    class SampleScene(Scene):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            rect = SimplePolygon(
                0, 0,
                1, 0,
                1, 1,
                0, 1
            )
            self[FIGURE_KEY] = rect


    R_30 = Mat3x3.rotation(45, is_radians=False)
    T_2_3 = Mat3x3.translation(2, 3)


    def frame1(scene):
        rect: SimplePolygon = scene[FIGURE_KEY]
        rect.color = "blue"
        rect.line_style = ":"


    def frame2(scene):
        rect: SimplePolygon = scene[FIGURE_KEY]
        rect.transformation= R_30
        rect.color = "orange"
        rect.line_style = ":"


    def frame3(scene):
        rect: SimplePolygon = scene[FIGURE_KEY]
        rect.transformation = T_2_3
        rect.color = "orange"
        rect.line_style = ":"


    def frame4(scene):
        rect: SimplePolygon = scene[FIGURE_KEY]
        rect.color = "red"
        rect.line_style = "-"
        rect.transformation = T_2_3 * R_30


    def frame5(scene):
        rect: SimplePolygon = scene[FIGURE_KEY]
        rect.transformation = R_30 * T_2_3


    scene = SampleScene(
        coordinate_rect=(-3, -1, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
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
                     frame5
                     )

    scene.show()
