import numpy as np

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4, vertex

if __name__ == '__main__':
    RECT_KEY = "rect"
    RECT_KEY1 = "rect1"
    ax = Vec4(0.557, 0.500, 0.663).normalize()
    O = vertex(0, 0, 0)
    t = vertex(0, 1, 0)
    angle_rot = np.radians(23)


    class SimplePolygonScene(AnimatedScene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            polygon = SimplePolygon(self.plt_axis,
                                    O,
                                    O + ax,
                                    O + t,
                                    edgecolor="red",
                                    )
            self[RECT_KEY] = polygon
            polygon.show_local_frame()

            polygon = SimplePolygon(self.plt_axis,
                                    O,
                                    O + ax,
                                    O + t,
                                    edgecolor="red",
                                    )
            self[RECT_KEY1] = polygon
            polygon.show_local_frame()


    animated_scene = SimplePolygonScene(
        image_size=(10, 10),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 3, 3, 3),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        # axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    transformation_matrix = (
            Mat4x4.translation(1, 1, 1) *
            Mat4x4.rotation(angle_rot, ax)
        # * Mat4x4.scale(2,
        #                2,
        #                2)
    )
    T, S, R, axis, angle = Mat4x4.decompose_affine(transformation_matrix)

    frames_num = 60
    animation = TrsTransformationAnimation(
        end=transformation_matrix,
        frames=frames_num,
        interval=5,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    animation_ax = RotationAnimation(
        end=angle_rot,
        axis=ax,
        frames=frames_num,
        channel=RECT_KEY1,
        apply_geometry_transformation_on_finish=True,
    )

    animated_scene.add_animation(animation_ax)
    animated_scene.add_animation(animation)
    animated_scene.animate()
