from abc import ABC, abstractmethod

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


class Animation(ABC):

    def __init__(self,
                 start,  # Початкове значення трасформації
                 end,  # Кінцеве значення трасформації
                 channels = ("default",),
                 frames=100,  # Кількість кадрів анімації
                 interval=16,  # Час в мілісекундах між кадрами анімації
                 repeat=False,  # Чи циклічна анімація
                 animation_listener=None,  # спостерігач
                 ):
        self.start = start
        self.end = end
        self.channels = channels
        self.frames = frames
        self.interval = interval
        self.repeat = repeat
        self.listener = animation_listener
        self.state = ANIMATION_STOPPED

    def notify(self, frame):
        if frame == 0:
            if self.state == ANIMATION_STOPPED:
                self.state = ANIMATION_PLAYED
                if self.listener is not None:
                    self.listener.on_start()

        if frame == self.frames - 1:
            if self.state == ANIMATION_PLAYED:
                if self.repeat:
                    if self.listener is not None:
                        self.listener.on_repeat()
                else:
                    self.state = ANIMATION_STOPPED
                    if self.listener is not None:
                        self.listener.on_finish()

    @abstractmethod
    def current_transformation(self, frame):
        pass
