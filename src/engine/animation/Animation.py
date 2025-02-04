from abc import ABC, abstractmethod

from src.engine.animation.AnimationListener import AnimationListener, FinishCallback
from src.math.Mat3x3 import Mat3x3

ANIMATION_STOPPED = "ANIMATION_STOPED"
ANIMATION_PLAYED = "ANIMATION_FINISHED"



class Animation(ABC):

    def __init__(self,
                 start,  # Початкове значення трасформації
                 end,  # Кінцеве значення трасформації
                 channels=("default",),
                 frames=60,  # Кількість кадрів анімації 60 (при інтервалі 16 мілісекунд буде 1 секунда)
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
        self.__animation_listeners = []

        self.add_animation_listener(animation_listener)

    def add_animation_listener(self, animation_listener):
        if animation_listener is not None:
            if isinstance(animation_listener, AnimationListener):
                self.__animation_listeners.append(animation_listener)
            elif callable(animation_listener):
                self.__animation_listeners.append(FinishCallback(animation_listener))

    def notify(self, scene, frame):
        if frame == 0:
            if self.state == ANIMATION_STOPPED:
                self.state = ANIMATION_PLAYED
                for listener in self.__animation_listeners:
                    listener.on_start(scene)

        if frame == self.frames - 1:
            if self.state == ANIMATION_PLAYED:
                if self.repeat:
                    for listener in self.__animation_listeners:
                        listener.on_repeat(scene)
                else:
                    self.state = ANIMATION_STOPPED
                    for listener in self.__animation_listeners:
                        listener.on_finish(scene)

    @abstractmethod
    def current_transformation(self, frame):
        pass
