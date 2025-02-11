from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4


class RotationAnimation(Animation):

    def __init__(self, end, axis, **kwargs):
        super().__init__(end, **kwargs)
        self.start_translation, self.start_scale, start_rotation, start_axis, start_angle = Mat4x4.decompose_affine(self.start)
        self.axis = axis
        self.end_angle = end
        self.start_angle = 0.0

    def current_transformation(self, frame):
        cur = (frame) / self.frames

        angle = self.start_angle + (self.end_angle - self.start_angle) * cur

        T = Mat4x4.translation(self.start_translation)
        R = Mat4x4.rotation(angle, self.axis)
        S = Mat4x4.scale(self.start_scale)

        transformation = T * R * S
        return transformation
