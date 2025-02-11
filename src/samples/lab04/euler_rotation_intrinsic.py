import numpy as np

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4, vertex

if __name__ == '__main__':
    RECT_KEY = "rect"
    RECT_0_KEY = "rect_0"
    O = vertex(0, 0, 0)
    t1 = Vec4(1, 0, 0)
    t2 = Vec4(1, 1, 0)

    angle_x = 30
    angle_y = 45
    angle_z = 60

    Rx = Mat4x4.rotation_x(angle_x, False)
    Ry = Mat4x4.rotation_y(angle_y, False)
    Rz = Mat4x4.rotation_z(angle_z, False)

    # R_final = (
    #         Rz *
    #         Ry *
    #         Rx
    # )

    R_final = (
            Rx *
            Ry *
            Rz
    )


    class SimplePolygonScene(AnimatedScene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            polygon = SimplePolygon(self.plt_axis,
                                    O,
                                    O + t1,
                                    O + t2,
                                    edgecolor="red",
                                    )
            self[RECT_KEY] = polygon
            polygon.show_local_frame()

            polygon0 = SimplePolygon(self.plt_axis,
                                     O,
                                     O + t1,
                                     O + t2,
                                     edgecolor="red",
                                     )
            self[RECT_0_KEY] = polygon0
            polygon0.set_transformation(R_final)
            polygon0.alpha = 0.2
            polygon0.show_local_frame()




    OX = Vec4(1, 0, 0)
    OY = Vec4(0, 1, 0)
    OZ = Vec4(0, 0, 1)

    frames_num = 180
    interval = 5

    animation_x = RotationAnimation(   # Rx
        end=np.radians(angle_x),
        axis=OX,
        frames=frames_num,
        interval=interval,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    OY1 = Rx * OY
    OZ1 = Rx * OZ

    Ry1 = Mat4x4.rotation(angle_y, OY1, False)

    animation_y = RotationAnimation(  # Ry1
        end=np.radians(angle_y),
        axis=OY1,
        frames=frames_num,
        interval=interval,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    OZ2 = Mat4x4.rotation(angle_z, OY1, False) * OZ1

    Rz2 = Mat4x4.rotation(angle_z, OZ2)

    # R_final = {
    #     Rz2 * Ry1 * Rx
    # }

    animation_z = RotationAnimation(
        end=np.radians(angle_z),
        axis=OZ2,
        frames=frames_num,
        interval=interval,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    animated_scene = SimplePolygonScene(
        image_size=(7, 7),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 1, 1, 1),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    animated_scene.add_animation(animation_x)
    animated_scene.add_animation(animation_y)
    animated_scene.add_animation(animation_z)

    # animated_scene.add_animation(animation)

    animated_scene.animate()

    # def frame1(scene):
    #     pass
    #
    #
    # #
    # # def frame2(scene):
    # #     pass
    #
    # animated_scene.add_frames(
    #     frame1,
    #     # frame2
    # )
    # animated_scene.draw()
    # animated_scene.finalize()
