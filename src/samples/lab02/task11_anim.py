import numpy as np

from src.engine.AnimatedScene import AnimatedScene
from src.engine.Polygon import Polygon
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation


class AnimatedSceneSample(AnimatedScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "my scene"

        polygon = Polygon()
        polygon.set_geometry(
            0, 0,
            0, 0,
            0, 0,
            0, 0
        )
        polygon.show_local_frame()
        # polygon.show_pivot()
        polygon["color"] = "blue"
        polygon["line_style"] = "-"

        self["rect"] = polygon


if __name__ == '__main__':
    scene = AnimatedSceneSample(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-3, -1, 3, 3),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("grey", "grey"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    ).prepare()

    # translation = TranslationAnimation(start=vertex(0, 0),
    #                                    end=vertex(3, 3),
    #                                    channels=("rect",),
    #                                    frames=100,
    #                                    # animation_listener=finish,
    #                                    )
    #


    scale = ScaleAnimation(start=(1, 1),
                           end=(2, 3),
                           frames=180,
                           channels=("rect",),
                           )

    rotation = RotationAnimation(start=0,
                                 end=np.radians(60),
                                 frames=180,
                                 channels=("rect",),
                                 # animation_listener=translation
                                 )

    scene.add_animation(scale)
    scene.add_animation(rotation)
    # scene.add_animation(translation)
    scene.animate()
    # scene.draw_figures()
    # scene.finalize()

