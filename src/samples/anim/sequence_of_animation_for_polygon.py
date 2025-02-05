import numpy as np

from src.engine.model.Polygon import Polygon
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Vec3 import vertex


class AnimatedSceneSample(AnimatedScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        polygon = Polygon()
        polygon.set_geometry(
            0, 1,
            1, 0,
            2, 1,
            1, 2
        )
        polygon.show_local_frame()
        polygon.pivot(1, 1)
        polygon.show_pivot()
        polygon["color"] = "blue"
        polygon["line_style"] = ":"

        self["rect"] = polygon


if __name__ == '__main__':
    scene = AnimatedSceneSample(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, 5, 5),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    ).prepare()

    translation = TranslationAnimation(
        end=vertex(1, 1),
        channel="rect",
        frames=20,
        # animation_listener=finish,
        # apply_geometry_transformation_on_finish=True,
    )

    translation2 = TranslationAnimation(
        end=vertex(-1, -1),
        channel="rect",
        frames=20,
        # animation_listener=finish,
        # apply_geometry_transformation_on_finish=True,
    )

    scale_before = ScaleAnimation(
        end=(1.2, 1.2),
        frames=20,
        channel="rect",
        # animation_listener=rotation
        # apply_geometry_transformation_on_finish=True,
    )

    scale_before2 = ScaleAnimation(
        end=(1, 1),
        frames=20,
        channel="rect",
        # animation_listener=rotation
        # apply_geometry_transformation_on_finish=True,
    )

    scale = ScaleAnimation(
        end=(2, 2),
        frames=20,
        channel="rect",
        # animation_listener=rotation
        # apply_geometry_transformation_on_finish=True,
    )

    scale2 = ScaleAnimation(
        end=(0.5, 0.5),
        frames=20,
        channel="rect",
        # animation_listener=rotation
        # apply_geometry_transformation_on_finish=True,
    )

    rotation = RotationAnimation(
        end=np.radians(30),
        frames=20,
        channel="rect",
        # animation_listener=translation
        # apply_geometry_transformation_on_finish=True,
    )

    rotation2 = RotationAnimation(
        end=np.radians(-30),
        frames=20,
        channel="rect",
        # animation_listener=translation
        # apply_geometry_transformation_on_finish=True,
    )

    scene.add_animation(scale_before)
    scene.add_animation(scale_before2)
    scene.add_animation(scale)
    scene.add_animation(rotation)
    scene.add_animation(translation)
    scene.add_animation(scale2)
    scene.add_animation(translation2)
    scene.add_animation(rotation2)
    scene.animate()
