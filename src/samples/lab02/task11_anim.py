import numpy as np

from src.engine.scene.AnimatedScene import AnimatedScene
from src.engine.model.Polygon import Polygon
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec3 import vertex


class AnimatedSceneSample(AnimatedScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "my scene"

        polygon = Polygon()
        polygon.set_geometry(
            0.5, 0.5,
            1.5, 0.5,
            1.5, 1.5,
            0.5, 1.5
        )
        polygon.show_local_frame()
        # polygon.show_pivot()
        polygon["color"] = "blue"
        polygon["line_style"] = "-"

        self["rect"] = polygon


if __name__ == '__main__':
    scene = AnimatedSceneSample(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-3, -1, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("grey", "grey"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    ).prepare()

    translation = TranslationAnimation(
        end=vertex(2, 2),
        channel="rect",
        frames=60,
        # animation_listener=finish,
    )

    scale = ScaleAnimation(
        end=(2, 3),
        frames=60,
        channel="rect",
    )

    rotation = RotationAnimation(
        end=np.radians(60),
        frames=60,
        channel="rect",
    )

    scene.add_animation(scale)
    scene.add_animation(rotation)
    scene.add_animation(translation)
    scene.animate()
