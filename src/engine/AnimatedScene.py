from abc import abstractmethod, ABC

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from src.engine.Scene import Scene

matplotlib.use("TkAgg")

ANIMATION_STOPPED = "ANIMATION_STOPED"
ANIMATION_PLAYED = "ANIMATION_FINISHED"


class AnimationListener(ABC):
    @abstractmethod
    def on_start(self): pass

    @abstractmethod
    def on_finish(self): pass

    @abstractmethod
    def on_repeat(self): pass


class AnimationFinishedListener(AnimationListener, ABC):
    def on_start(self): pass

    def on_repeat(self): pass


class AnimatedScene(Scene):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._start = None
        self._end = None
        self._frames = 0
        self._repeat = False
        self._animation_state = ANIMATION_STOPPED

        self.__listener = None

    def animate(self,
                start,  # Початкове значення трасформації
                end,  # Кінцеве значення трасформації
                frame=100,  # Кількість кадрів анімації
                interval=16,  # Час в мілісекундах між кадрами анімації
                repeat=False,  # Чи циклічна анімація
                animation_listener=None,  # спостерігач
                ):
        self._start = start
        self._end = end
        self._frames = frame
        self._repeat = repeat
        self.__listener = animation_listener

        global ani
        ani = FuncAnimation(self.figure, self.__update, frames=frame, blit=False, interval=interval, repeat=repeat)

        plt.show()

    @abstractmethod
    def on_frame(self, frame, start, end):
        pass

    def __update(self, frame):
        # print(f"Frame {frame}")

        if frame == 0:
            if self._animation_state == ANIMATION_STOPPED:
                self._animation_state = ANIMATION_PLAYED
                if self.__listener is not None:
                    self.__listener.on_start()

        if frame == self._frames - 1:
            if self._animation_state == ANIMATION_PLAYED:
                if self._repeat:
                    if self.__listener is not None:
                        self.__listener.on_repeat()
                else:
                    self._animation_state = ANIMATION_STOPPED
                    if self.__listener is not None:
                        self.__listener.on_finish()

        self.figure.clear()  # Очищення фігури

        self.set_title()

        self.setup_base_parameters()
        self.show_axes()

        self.on_frame(frame, self._start, self._end)

        return self.figure,
