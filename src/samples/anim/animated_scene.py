from src.engine.AnimatedScene import AnimatedScene, AnimationListener, AnimationFinishedListener
from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex

if __name__ == '__main__':
    class SampleScene(AnimatedScene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self._rect = SimplePolygon(
                0, 0,
                1, 0,
                1, 1,
                0, 1
            )
            self._rect.color = "blue"
            self._rect.line_style = "-"
            self._rect.draw()

        def draw_scene(self):
            self._rect.draw()

        def on_frame(self, frame, start, end):
            vect = start + (end - start) * (frame / 100)
            T = Mat3x3.translation(vect)
            self._rect.transformation = T
            self._rect.draw()


    ######################################################

    scene = SampleScene(
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

        def on_finish(self):
            print("Finished animation")


    class AnimListenerAllEvent(AnimationListener):

        def on_start(self):
            print("Started animation")

        def on_repeat(self):
            print("Animation repeat")

        def on_finish(self):
            print("Finished animation")

    scene.animate(start=vertex(0, 0),
                  end=vertex(2, 2),
                  repeat=True,
                  animation_listener=AnimListenerAllEvent())
