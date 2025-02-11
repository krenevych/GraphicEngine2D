from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4


class TranslationAnimation(Animation):

    def __init__(self, end, **kwargs):
        super().__init__(Mat4x4.translation(end), **kwargs)

    def current_transformation(self, frame):
        start_translation, start_rotation, start_scales, _, _ = Mat4x4.decompose_affine(self.start)
        end_translation, end_rotation, end_scales, _, _ = Mat4x4.decompose_affine(self.end)

        translation = start_translation + (end_translation - start_translation) *  (frame / self.frames)
        # print(translation)

        T = Mat4x4.translation(translation)
        R = Mat4x4(start_rotation)
        S = Mat4x4.scale(start_scales)

        transformation = T * R * S

        # print()
        # print(transformation)
        # print("=============")

        return transformation