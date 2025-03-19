import numpy as np

from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Quaternion import Quaternion
from src.math.Vec4 import Vec4, vertex

if __name__ == '__main__':
    RECT_KEY = "rect"
    RECT_0_KEY = "rect_0"
    O = vertex(0, 0, 0)
    t1 = Vec4(1, 0, 0)
    t2 = Vec4(1, 1, 0)

    angle_x = np.radians(30)
    angle_y = np.radians(45)
    angle_z = np.radians(60)

    Rx = Mat4x4.rotation_x(angle_x)
    Ry = Mat4x4.rotation_y(angle_y)
    Rz = Mat4x4.rotation_z(angle_z)
    R_final = Rx * Ry * Rz

    qx = Quaternion.rotation_x(angle_x)
    qy = Quaternion.rotation_y(angle_y)
    qz = Quaternion.rotation_z(angle_z)
    q_final = qx * qy * qz


    OX = Vec4(1, 0, 0)
    OY = Vec4(0, 1, 0)
    OZ = Vec4(0, 0, 1)

    frames_num = 180
    interval = 5

    animation_x = RotationAnimation(  # Rx
        end=angle_x,
        axis=OX,
        frames=frames_num,
        interval=interval,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    OY1 = Rx * OY
    OZ1 = Rx * OZ

    Ry1 = Mat4x4.rotation(angle_y, OY1)

    animation_y = RotationAnimation(  # Ry1
        end=angle_y,
        axis=OY1,
        frames=frames_num,
        interval=interval,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    OZ2 = Mat4x4.rotation(angle_y, OY1) * OZ1

    Rz2 = Mat4x4.rotation(angle_z, OZ2)

    animation_z = RotationAnimation(
        end=angle_z,
        axis=OZ2,
        frames=frames_num,
        interval=interval,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    animation = TrsTransformationAnimation(
        end=R_final,
        frames=frames_num,
        interval=5,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    animation_quat = QuaternionAnimation(
        end_quaternion=q_final,
        frames=frames_num,
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
            polygon.show_local_frame()

            polygon0 = SimplePolygon(self.plt_axis,
                                     O,
                                     O + t1,
                                     O + t2,
                                     edgecolor="red",
                                     alpha=0.2
                                     )
            self[RECT_0_KEY] = polygon0
            polygon0.transformation = R_final
            polygon0.show_local_frame()


    animated_scene = SimplePolygonScene(
        axis_color="grey",  # колір осей координат
    )

    # animated_scene.add_animation(animation_x)
    # animated_scene.add_animation(animation_y)
    # animated_scene.add_animation(animation_z)

    # animated_scene.add_animation(animation)
    animated_scene.add_animation(animation_quat)

    animated_scene.show()