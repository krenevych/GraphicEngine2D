import numpy as np

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.model.Vector import Vector
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Vec4 import Vec4, vertex

if __name__ == '__main__':
    RECT_KEY = "rect"
    VECT_KEY = "vector"
    ax = Vec4(0.557, 0.500, 0.663)
    O = vertex(0, 0, 0)
    t = vertex(0, 1, 0)


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
            # polygon.show_local_frame()

            vector = Vector(
                self.plt_axis,
                O,
                O + ax,
            )
            self[VECT_KEY] = vector
            vector.color = "brown"


    def frame1(scene):
        pass


    animated_scene = SimplePolygonScene(
        image_size=(10, 10),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 2, 2, 2),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        # axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    frames_num = 180
    animation = RotationAnimation(
        end=np.radians(90),
        axis=ax,
        frames=frames_num,
        channel=RECT_KEY,
        apply_geometry_transformation_on_finish=True,
    )

    animated_scene.add_animation(animation)
    animated_scene.animate()

    # animated_scene.add_frames(frame1)
    # animated_scene.draw()
    # animated_scene.finalize()
