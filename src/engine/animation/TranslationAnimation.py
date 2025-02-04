from src.engine.animation.Animation import Animation
from src.math.Mat3x3 import Mat3x3


class TranslationAnimation(Animation):

    def __init__(self, end, **kwargs):
        super().__init__(Mat3x3.translation(end), **kwargs)

    def current_transformation(self, frame):
        start_translation, start_angle, start_scales = Mat3x3.decompose_affine(self.start)
        end_translation, end_angle, end_scales = Mat3x3.decompose_affine(self.end)

        translation = start_translation + (end_translation - start_translation) *  (frame / self.frames)

        T = Mat3x3.translation(*translation)
        R = Mat3x3.rotation(start_angle)
        S = Mat3x3.scale(start_scales)

        transformation = T * R * S
        return transformation