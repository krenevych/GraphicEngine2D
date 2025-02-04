from src.engine.AnimatedScene import AnimatedScene
from src.engine.animation.Animation import AnimationFinishedListener
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Vec3 import vertex


class AnimatedSceneSample(AnimatedScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self["rect"] = SimplePolygon(
            0, 0,
            1, 0,
            1, 1,
            0, 1
        )

        self["rect"].color = "blue"
        self["rect"].line_style = "-"


if __name__ == '__main__':
    scene = AnimatedSceneSample(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-3, -1, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )


    class AnimListener(AnimationFinishedListener):
        def on_finish(self, scene):
            print("Finished animation")


    animation = TranslationAnimation(start=vertex(0, 0),
                                     end=vertex(2, 2),
                                     channels=("rect",),
                                     animation_listener=AnimListener())

    scene.animate(animation)
