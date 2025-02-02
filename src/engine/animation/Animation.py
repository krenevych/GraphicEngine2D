from abc import ABC, abstractmethod

from src.math.Mat3x3 import Mat3x3

ANIMATION_STOPPED = "ANIMATION_STOPED"
ANIMATION_PLAYED = "ANIMATION_FINISHED"


class AnimationListener(ABC):
    @abstractmethod
    def on_start(self, scene): pass

    @abstractmethod
    def on_finish(self, scene): pass

    @abstractmethod
    def on_repeat(self, scene): pass


class AnimationFinishedListener(AnimationListener, ABC):
    def on_start(self, scene): pass

    def on_repeat(self, scene): pass

class FinishCallback(AnimationFinishedListener):
    def __init__(self, callback):
        if callable(callback):
            self.callback = callback

    def on_finish(self, scene):
        self.callback(scene)


class Animation(ABC):

    def __init__(self,
                 start,  # Початкове значення трасформації
                 end,  # Кінцеве значення трасформації
                 channels=("default",),
                 frames=100,  # Кількість кадрів анімації
                 interval=16,  # Час в мілісекундах між кадрами анімації
                 repeat=False,  # Чи циклічна анімація
                 animation_listener=None,  # спостерігач
                 ):
        self.initial_transformation = Mat3x3.identity()
        self.start = start
        self.end = end
        self.channels = channels
        self.frames = frames
        self.interval = interval
        self.repeat = repeat
        self.state = ANIMATION_STOPPED

        if isinstance(animation_listener, AnimationListener):
            self.listener = animation_listener
        elif callable(animation_listener):
            self.listener = FinishCallback(animation_listener)
        else:
            self.listener = None

    def notify(self, scene, frame):
        if frame == 0:
            if self.state == ANIMATION_STOPPED:
                self.state = ANIMATION_PLAYED
                if self.listener is not None:
                    self.listener.on_start(scene)

        if frame == self.frames - 1:
            if self.state == ANIMATION_PLAYED:
                if self.repeat:
                    if self.listener is not None:
                        self.listener.on_repeat(scene)
                else:
                    self.state = ANIMATION_STOPPED
                    if self.listener is not None:
                        self.listener.on_finish(scene)

    @abstractmethod
    def current_transformation(self, frame):
        pass
