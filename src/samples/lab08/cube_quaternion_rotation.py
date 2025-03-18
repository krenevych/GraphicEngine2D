import numpy as np

from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TrsTransformationAnimation import TrsTransformationAnimation
from src.engine.model.Cube import Cube
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Quaternion import Quaternion
from src.math.Vec4 import Vec4, vertex

CUBE_KEY = "cube"
if __name__ == '__main__':
    RECT_KEY = "rect"


    class AnimScene(AnimatedScene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            cube = Cube(self.plt_axis, alpha=0.1)
            self[CUBE_KEY] = cube
            cube.show_pivot()
            cube.show_local_frame()


    animated_scene = AnimScene(
        coordinate_rect=(-1, -1, -1, 1, 1, 1),  # розмірність системи координатps
    ).prepare()


    def frame1(scene):
        cube: Cube = scene[CUBE_KEY]


    animated_scene.add_frames(
        frame1,
    )  # додаємо кадри на сцену

    animated_scene.draw()
    animated_scene.finalize()