from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4


class RotationAnimation1(Animation):

    def __init__(self, end, axis, P, **kwargs):
        super().__init__(end, **kwargs)

        self.start_translation, start_angle, self.start_scales = Mat4x4.decompose_affine(self.start)
        self.axis = axis
        self.end_angle = end
        self.start_angle = 0.0

        self.pivot = P

    def current_transformation(self, frame):
        angle = self.start_angle + (self.end_angle - self.start_angle) * (frame / self.frames)

        T = Mat4x4.translation(self.pivot)
        R = Mat4x4.rotation(angle, self.axis)
        # S = Mat4x4.scale(self.start_scales)

        transformation = T * R * T.inverse()
        return transformation
