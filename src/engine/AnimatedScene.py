from abc import ABC

import matplotlib
from matplotlib.animation import FuncAnimation

from src.engine.animation.Animation import Animation, AnimationFinishedListener
from src.engine.Scene import Scene

matplotlib.use("TkAgg")


class AnimatedScene(Scene, AnimationFinishedListener):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._current_animation = None
        self._animations = []

    def on_finish(self, scene):
        self.__animate_next()

    def add_animation(self, animation: Animation):
        self._animations.append(animation)
        animation.add_animation_listener(self)

    def __animate_next(self):
        if len(self._animations) > 0:
            current = self._animations[0]
            self._animations.pop(0)
            self.animate(current)

    def animate(self, animation: Animation = None):

        if animation is None:
            self.__animate_next()
            return

        self._current_animation = animation
        self._current_animation.initial_transformation = self[animation.channels[0]].transformation

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

        if self._current_animation is not None:

            transformation = self._current_animation.current_transformation(frame)
            for channel in self._current_animation.channels:
                figure = self[channel]
                figure.set_transformation(transformation)

            self._current_animation.notify(self, frame)


    def __update(self, frame):
        # print(f"Frame {frame}")

        self.figure.clear()  # Очищення фігури
        self.prepare()

        self.on_frame(frame)
        self.draw_figures()

        return self.figure,
