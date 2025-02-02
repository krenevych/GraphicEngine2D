from src.engine.animation.Animation import Animation
from src.math.Mat3x3 import Mat3x3


class TranslationAnimation(Animation):

    def current_transformation(self, frame):
        vect = self.start + (self.end - self.start) * (frame / self.frames)
        transformation = Mat3x3.translation(vect)
        transformation = transformation * self.initial_transformation
        return transformation
