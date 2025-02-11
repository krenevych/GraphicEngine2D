from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4


class TranslationAnimation(Animation):

    def __init__(self, end, **kwargs):
        super().__init__(Mat4x4.translation(end), **kwargs)

    def current_transformation(self, frame):
        start_translation, start_scale, start_rotation, start_axis, start_angle = Mat4x4.decompose_affine(self.start)
        end_translation, end_scales, end_rotation, end_axis, end_angle = Mat4x4.decompose_affine(self.end)

        # start_translation, start_angle, start_scales = Mat4x4.decompose_affine(self.start)
        # end_translation, end_angle, end_scales = Mat4x4.decompose_affine(self.end)

        translation = start_translation + (end_translation - start_translation) *  (frame / self.frames)

        T = Mat4x4.translation(*translation)
        R = Mat4x4(end_rotation)
        S = Mat4x4.scale(end_scales)

        transformation = T * R * S
        # transformation = T
        return transformation