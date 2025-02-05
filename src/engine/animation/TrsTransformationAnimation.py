from src.engine.animation.Animation import Animation
from src.math.Mat3x3 import Mat3x3


class TrsTransformationAnimation(Animation):

    def current_transformation(self, frame):
        start_translation, start_angle, start_scales = Mat3x3.decompose_affine(self.start)
        end_translation, end_angle, end_scales = Mat3x3.decompose_affine(self.end)

        translation = start_translation + (end_translation - start_translation) * (frame / self.frames)
        angle = start_angle + (end_angle - start_angle) * (frame / self.frames)
        scales = start_scales + (end_scales - start_scales) * (frame / self.frames)

        T = Mat3x3.translation(translation)
        R = Mat3x3.rotation(angle)
        S = Mat3x3.scale(scales)

        transformation = T * R * S
        return transformation
