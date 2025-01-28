from abc import abstractmethod

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from src.engine.Scene import Scene

matplotlib.use("TkAgg")


class AnimationListener:

    @abstractmethod
    def on_start(self):
        pass

    @abstractmethod
    def on_finish(self):
        pass

    @abstractmethod
    def on_restart(self):
        pass

ANIMATION_STOPED = "ANIMATION_STOPED"
ANIMATION_PLAYED = "ANIMATION_FINISHED"

class AnimatedScene(Scene):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._start = None
        self._end = None
        self._frames = 0
        self._animation_state = ANIMATION_STOPED

        self.listener = None

    def animate(self, start, end,
                frame=100,
                interval=16,
                animation_listener=None,
                repeat=False):
        self._start = start
        self._end = end
        self._frames = frame
        self._repeat = repeat
        self.listener = animation_listener

        global ani
        ani = FuncAnimation(self.figure, self.__update, frames=frame, blit=False, interval=interval, repeat=repeat)

        plt.show()

    @abstractmethod
    def on_frame(self, frame, start, end):
        pass

    def __update(self, frame):
        # print(f"Frame {frame}")

        if frame == 0:
            if self._animation_state == ANIMATION_STOPED:
                self._animation_state = ANIMATION_PLAYED
                if self.listener is not None:
                    self.listener.on_start()


        if frame == self._frames - 1:
            if self._animation_state == ANIMATION_PLAYED:
                if  self._repeat:
                    if self.listener is not None:
                        self.listener.on_restart()
                else:
                    self._animation_state = ANIMATION_STOPED
                    if self.listener is not None:
                        self.listener.on_finish()

        self.figure.clear()  # Очищення фігури

        self.set_title()

        self.setup_base_parameters()
        self.show_axes()

        self.on_frame(frame, self._start, self._end)

        return self.figure,
