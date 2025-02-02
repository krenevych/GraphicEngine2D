from abc import ABC

import matplotlib
from matplotlib.animation import FuncAnimation

from src.engine.Animation import Animation
from src.engine.Scene import Scene

matplotlib.use("TkAgg")


class AnimatedScene(Scene, ABC):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._animation = None


    def animate(self, animation: Animation):

        self._animation = animation

        global ani
        ani = FuncAnimation(self.figure,
                            self.__update,
                            frames=animation.frames,
                            interval=animation.interval,
                            repeat=animation.repeat,
                            blit=False,
                            )

        #       ani.save("animation.gif", writer="pillow", fps=20)
        self.finalize()

    def on_frame(self, frame):

        if self._animation is not None:

            transformation = self._animation.current_transformation(frame)
            for channel in self._animation.channels:
                figure = self[channel]
                figure.transformation = transformation

            self._animation.notify(frame)


    def __update(self, frame):
        # print(f"Frame {frame}")

        self.figure.clear()  # Очищення фігури
        self.prepare()

        self.on_frame(frame)
        self.draw_figures()

        return self.figure,
