import numpy as np

from src.engine.animation.RotationAnimation1 import RotationAnimation1
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.model.Vector import Vector
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Vec4 import Vec4, vertex

if __name__ == '__main__':
    RECT_KEY = "rect"
    VECT_KEY = "vector"
    ax = Vec4(0.557, 0.500, 0.663)
    O = vertex(0, 0, 0)
    pass



    class SimplePolygonScene(AnimatedScene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            polygon = SimplePolygon(self.plt_axis,
                                    O[0], O[1], O[2],
                                    O[0] + ax[0], O[1] + ax[1], O[2] + ax[2],
                                    # O[0], O[1] + 1, O[2],
                                    0, 1, 0,
                                    edgecolor="red",
                                    )
            self[RECT_KEY] = polygon
            # polygon.show_local_frame()

            vector = Vector(
                self.plt_axis,
                O[0], O[1], O[2],
                O[0] + ax[0], O[1] + ax[1], O[2] + ax[2],
            )
            self[VECT_KEY] = vector
            vector.color = "brown"


    animated_scene = SimplePolygonScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 2, 2, 2),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        # axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    animation = RotationAnimation1(
        end=np.radians(90),
        axis=ax,
        P=O,

        frames=180,
        channel=RECT_KEY,
        # apply_geometry_transformation_on_finish=True,
    )

    animated_scene.add_animation(animation)
    animated_scene.animate()
