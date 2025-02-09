import numpy as np

from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.model.Vector import Vector
from src.engine.scene.Scene import Scene
from src.math.Mat4x4 import Mat4x4

if __name__ == '__main__':
    RECT_KEY = "rect"
    VECT_KEY = "vector"


    class SimplePolygonScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            # polygon = SimplePolygon(self.plt_axis,
            #                         0, 0, 0,
            #                         1, 0, 0,
            #                         1, 1, 0,
            #                         0, 1, 0,
            #                         edgecolor="red",
            #
            #                         )
            polygon = SimplePolygon(self.plt_axis,
                                    0, 0, 0,
                                    0.557, 0.500, 0.663,
                                    # 1, 1, 0,
                                    0, 1, 0,
                                    edgecolor="red",

                                    )
            self[RECT_KEY] = polygon


            vector = Vector(self.plt_axis,
                            0, 0, 0,
                            0.557, 0.500, 0.663
                            )
            self[VECT_KEY] = vector
            vector.color = "brown"


    Rz = Mat4x4.rotation_z(np.radians(45))
    Ry = Mat4x4.rotation_y(np.radians(30))
    Rx = Mat4x4.rotation_x(np.radians(15))
    # T = Mat4x4.translation(1, 0, 0)
    T = Mat4x4.translation(0.557, 0.500, 0.663,)
    T1 = T.inverse()


    ############## Frame 1 ##################
    def frame1(scene: Scene):
        rect: SimplePolygon = scene[RECT_KEY]

        # rect.color = "blue"  # колір ліній
        rect.alpha = 0.2


    ############## Frame 2 ##################
    def frame2(scene: Scene):
        rect: SimplePolygon = scene[RECT_KEY]
        vect: Vector = scene[VECT_KEY]

        u = vect.transformed_geometry[1].xyz
        ux, uy, uz = u
        print(*u)

        R1 = Mat4x4.rotation(np.radians(90), u)
        R = T * R1 * T1

        rect.color = "blue"  # колір ліній
        # rect.set_transformation(T * R * S)
        rect.set_transformation(R)


    simple_scene = SimplePolygonScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 2, 2, 2),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        # axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    simple_scene.add_frames(
        frame1,
        frame2,
    )  # додаємо кадри на сцену

    simple_scene.draw()
    simple_scene.finalize()
