from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4


class RotationAnimation(Animation):

    def __init__(self, end, **kwargs):
        super().__init__(Mat4x4.rotation(end), **kwargs)

    def current_transformation(self, frame):
        start_translation, start_angle, start_scales = Mat4x4.decompose_affine(self.start)
        end_translation, end_angle, end_scales = Mat4x4.decompose_affine(self.end)

        angle = start_angle + (end_angle - start_angle) *  (frame / self.frames)

        T = Mat4x4.translation(start_translation)
        R = Mat4x4.rotation(angle)
        S = Mat4x4.scale(start_scales)

        transformation = T * R * S
        return transformation