from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4
from src.math.utils_matrix import decompose_affine


class RotationAnimation1(Animation):

    def __init__(self, end, axis, P, **kwargs):
        super().__init__(end, **kwargs)

        self.start_translation, start_angle, self.start_scales = decompose_affine(self.start)
        self.axis = axis
        self.end_angle = end
        self.start_angle = 0.0

        self.pivot = P

    def current_transformation(self, frame):
        t = frame / self.frames
        angle = self.start_angle + (self.end_angle - self.start_angle) * t

        T = Mat4x4.translation(self.pivot)
        R = Mat4x4.rotation(angle, self.axis)
        # S = Mat4x4.scale(self.start_scales)

        transformation = T * R * T.inverse()
        return transformation
