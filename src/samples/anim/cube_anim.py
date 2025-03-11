import numpy as np

from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.engine.model.Cube import Cube
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Quaternion import Quaternion

if __name__ == '__main__':
    CUBE_KEY = "cube"
    CUBE_TARGET_KEY = "cube_targer"

    angle_x, angle_y, angle_z = np.radians(30), np.radians(45), np.radians(60)

    qx = Quaternion.rotation_x(angle_x)
    qy = Quaternion.rotation_y(angle_y)
    qz = Quaternion.rotation_z(angle_z)
    q_final = qz * qy * qx

    animation = QuaternionAnimation(
        q_final,
        channel=CUBE_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    animation_x = QuaternionAnimation(
        qx,
        channel=CUBE_KEY,
        apply_geometry_transformation_on_finish=True,
    )
    animation_y = QuaternionAnimation(
        qy,
        channel=CUBE_KEY,
        apply_geometry_transformation_on_finish=True,
    )
    animation_z = QuaternionAnimation(
        qz,
        channel=CUBE_KEY,
        apply_geometry_transformation_on_finish=True,
    )


    class CubeScene(AnimatedScene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            cube = Cube(self.plt_axis, alpha=0.1)
            self[CUBE_KEY] = cube
            cube.show_pivot()
            cube.show_local_frame()

            cube_target = Cube(self.plt_axis, alpha=0.1, color="grey", line_width=0.5, line_style="-.")
            self[CUBE_TARGET_KEY] = cube_target
            cube_target.rotation = q_final


    animated_scene = CubeScene().prepare()

    animated_scene.add_animation(animation)
    # animated_scene.add_animation(animation_x)
    # animated_scene.add_animation(animation_y)
    # animated_scene.add_animation(animation_z)
    animated_scene.animate()
