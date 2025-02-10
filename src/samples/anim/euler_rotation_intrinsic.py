import numpy as np

from src.engine.animation.RotationAnimation import RotationAnimation
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
    # p = vertex(1 * 0.5, 0.5, 0 * 0.5)
    # p = vertex(1, 2 * 0.5, 0 * 0.5)
    p = vertex()

    angle_x = 35
    angle_y = 133
    angle_z = 34

    Rx = Mat4x4.rotation_x(angle_x, False)
    Ry = Mat4x4.rotation_y(angle_y, False)
    Rz = Mat4x4.rotation_z(angle_z, False)

    R_final = Rx * Ry * Rz

    X = Vec4(1, 0, 0)
    Y = Vec4(0, 1, 0)
    Z = Vec4(0, 0, 1)

    time = 180
    animation_x = RotationAnimation(
        end=np.radians(angle_x),
        axis=X,
        frames=time,
        interval=3,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    y1 = Rx * Y
    z1 = Rx * Z
    rot_y = Mat4x4.rotation(np.radians(angle_y), y1)

    rot = rot_y * Rx

    z2 = rot_y * z1
    rot_z = Mat4x4.rotation(np.radians(angle_z), z2)

    rot = rot_z * rot

    animation_y = RotationAnimation(
        end=np.radians(angle_y),
        axis=y1,
        frames=time,
        interval=5,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    animation_z = RotationAnimation(
        end=np.radians(angle_z),
        axis=z2,
        frames=time,
        interval=5,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
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
            polygon.pivot(p)
            polygon.show_local_frame()
            polygon.show_pivot()

            polygon0 = SimplePolygon(self.plt_axis,
                                     O,
                                     O + t1,
                                     O + t2,
                                     edgecolor="red",
                                     )
            self[RECT_0_KEY] = polygon0
            polygon0.set_transformation(R_final)
            polygon0.alpha = 0.3
            polygon0.pivot(p)
            polygon0.show_local_frame()


    animated_scene = SimplePolygonScene(
        image_size=(8, 8),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 1, 1, 1),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("#f00000", "#00f000", "#000088"),  # колір осей координат
        axis_line_width=0.5,
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    animated_scene.add_animation(animation_x)
    animated_scene.add_animation(animation_y)
    animated_scene.add_animation(animation_z)
    animated_scene.animate()
