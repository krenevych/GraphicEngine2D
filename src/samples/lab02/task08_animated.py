import numpy as np

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Polygon import Polygon
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"


class AnimatedSceneSample(AnimatedScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "my scene"

        polygon = Polygon()
        polygon.set_geometry(
            0, 0,
            1, 0,
            1, 1,
            0, 1
        )
        polygon.show_local_frame()
        polygon.pivot(0.5, 0.5)
        polygon.show_pivot()
        polygon["color"] = "blue"
        polygon["line_style"] = "-"

        self[FIGURE_KEY] = polygon


if __name__ == '__main__':
    scene = AnimatedSceneSample(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-2, -1, 4, 4),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )

    translation = TranslationAnimation(
        end=vertex(2, 2),
        channel=FIGURE_KEY,
        frames=30,
        # animation_listener=finish,
    )


    def scale_finish_listener(animated_scene):
        print(animated_scene.name)
        print("Animation finished!")


    scale = ScaleAnimation(
        end=(1, 2),
        frames=30,
        channel=FIGURE_KEY,
        animation_listener=scale_finish_listener
    )

    rotation = RotationAnimation(
        end=np.radians(60),
        frames=30,
        channel=FIGURE_KEY,
        # animation_listener=translation
    )

    scene.add_animation(scale)
    scene.add_animation(rotation)
    scene.add_animation(translation)
    scene.show()
