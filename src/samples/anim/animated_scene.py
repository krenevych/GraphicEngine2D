from src.engine.AnimatedScene import AnimatedScene, Animation
from src.engine.Animation import AnimationFinishedListener
from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex


class TranslationAnimation(Animation):

    def current_transformation(self, frame):
        vect = self.start + (self.end - self.start) * (frame / self.frames)
        transformation = Mat3x3.translation(vect)
        return transformation


if __name__ == '__main__':
    scene = AnimatedScene(
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

    scene["rect"] = SimplePolygon(
        0, 0,
        1, 0,
        1, 1,
        0, 1
    )

    scene["rect"].color = "blue"
    scene["rect"].line_style = "-"


    class AnimListener(AnimationFinishedListener):
        def __init__(self, scene):
            self.scene = scene

        def on_finish(self):
            animation = TranslationAnimation(start=vertex(2, 2),
                                             end=vertex(4, 0),
                                             channels=("rect",),
                                             # animation_listener=AnimListener()
                                             )
            scene.animate(animation)
            print("Finished animation")


    animation = TranslationAnimation(start=vertex(0, 0),
                                     end=vertex(2, 2),
                                     channels=("rect",),
                                     animation_listener=AnimListener(scene))

    scene.animate(animation)
