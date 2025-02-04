import numpy as np

from src.engine.animation.Animation import Animation
from src.math.Mat3x3 import Mat3x3


class ScaleAnimation(Animation):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.start = np.array(self.start)
        self.end = np.array(self.end)

    def current_transformation(self, frame):
        scale = self.start + (self.end - self.start) * (frame / self.frames)
        transformation = Mat3x3.scale(scale)
        transformation = transformation * self.initial_transformation
        return transformation