import numpy as np

from src.engine.model.CoordinateFrame import CoordinateFrame
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3

if __name__ == '__main__':
    RECT_KEY = "rect"


    class CoordinateFrameScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            coord_frame = CoordinateFrame()
            self[RECT_KEY] = coord_frame


    ############## Frame 1 ##################
    def frame1(scene: Scene):
        rect: CoordinateFrame = scene[RECT_KEY]
        rect.line_style = "--"  # стиль ліній


    ##############################################
    ##############################################

    Rz = Mat3x3.rotationZ(np.radians(45))
    Rx = Mat3x3.rotationX(np.radians(15))
    S = Mat3x3.scale(1)
    T = Mat3x3.translation(0, 0)


    ############## Frame 2 ##################
    def frame2(scene: Scene):
        rect: CoordinateFrame = scene[RECT_KEY]

        # rect.show_local_frame()

        R = Rz

        rect.alpha = 1.0
        rect.set_transformation(T * R * S)


    ############## Frame 3 ##################
    def frame3(scene: Scene):
        rect: CoordinateFrame = scene[RECT_KEY]

        R = Rx * Rz

        rect.set_transformation(T * R * S)


    simple_scene = CoordinateFrameScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, 2, 2),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=False,  # чи показувати осі координат
        axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    simple_scene.add_frames(
        frame1,
        frame2,
        frame3,
    )  # додаємо кадри на сцену

    simple_scene.draw()
    simple_scene.finalize()
