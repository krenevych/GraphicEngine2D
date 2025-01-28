from abc import abstractmethod

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from src.base.scene import Scene
from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import vertex


class AnimatedScene(Scene):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._start = None
        self._end = None

    def animate(self, start, end,
                frame=100,
                interval=16):
        self._start = start
        self._end = end

        global ani
        ani = FuncAnimation(self.figure, self.__update, frames=frame, blit=False, interval=interval)

        plt.show()

    @abstractmethod
    def on_frame(self, frame, start, end):
        pass

    def __update(self, frame):
        print(f"Frame {frame}")
        self.figure.clear()  # Очищення фігури

        self.set_title()

        self.setup_base_parameters()
        self.show_axes()

        self.on_frame(frame, self._start, self._end)

        return self.figure,


if __name__ == '__main__':
    matplotlib.use("TkAgg")


    class SampleScene(AnimatedScene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.rect = SimplePolygon(
                0, 0,
                1, 0,
                1, 1,
                0, 1
            )
            self.rect.color = "blue"
            self.rect.line_style = "-"
            self.rect.draw()

        def draw_scene(self):
            self.rect.draw()

        def on_frame(self, frame, start, end):
            vect = start + (end - start) * (frame / 100)
            T = Mat3x3.translation(vect)
            self.rect.transformation = T
            self.rect.draw()


    ######################################################

    scene = SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-3, -1, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )

    # scene.draw()
    scene.animate(start=vertex(0,0), end=vertex(2, 2))
