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

        polygon = Polygon()
        polygon.set_geometry(
            0, 0,
            1, 0,
            1, 1,
            0, 1
        )
        polygon.show_local_frame()
        polygon.pivot(2, 2.)
        polygon.show_pivot()
        polygon["color"] = "blue"
        polygon["line_style"] = "-"

        self[FIGURE_KEY] = polygon


if __name__ == '__main__':
    scene = AnimatedSceneSample(
        coordinate_rect=(-1, -1, 4, 4),  # розмірність системи координат
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )

    translation = TranslationAnimation(
        end=vertex(3, 3),
        channel=FIGURE_KEY,
        frames=100,
        # animation_listener=finish,
    )

    scale = ScaleAnimation(
        end=(2, 2),
        frames=100,
        channel=FIGURE_KEY,
        # animation_listener=rotation
    )

    rotation = RotationAnimation(
        end=np.radians(60),
        frames=180,
        channel=FIGURE_KEY,
        # animation_listener=translation
    )

    scene.add_animation(rotation)
    scene.add_animation(scale)
    scene.add_animation(translation)
    scene.show()
