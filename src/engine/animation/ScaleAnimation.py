from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4


class ScaleAnimation(Animation):

    def __init__(self, end, **kwargs):
        super().__init__(Mat4x4.scale(end), **kwargs)

    def current_transformation(self, frame):
        start_translation, start_rotation, start_scales, _, _ = Mat4x4.decompose_affine(self.start)
        end_translation, end_rotation, end_scales, _, _ = Mat4x4.decompose_affine(self.end)

        scales = start_scales + (end_scales - start_scales) * (frame / self.frames)

        T = Mat4x4.translation(start_translation)
        R = Mat4x4(start_rotation)
        S = Mat4x4.scale(*scales)

        transformation = T * R * S
        return transformation
