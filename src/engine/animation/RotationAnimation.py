from src.engine.animation.Animation import Animation
from src.math.Mat3x3 import Mat3x3


class RotationAnimation(Animation):

    def current_transformation(self, frame):
        angle = self.start + (self.end - self.start) * (frame / self.frames)
        transformation = Mat3x3.rotation(angle)
        transformation = transformation * self.initial_transformation
        return transformation