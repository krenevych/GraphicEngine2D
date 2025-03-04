from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4
from src.math.utils_matrix import decompose_affine


class TrsTransformationAnimation(Animation):

    # def __init__(self, end, **kwargs):
    #     super().__init__(end, **kwargs)
    #
    #     end_translation, end_scale, end_rotation, end_axis, end_angle = Mat4x4.decompose_affine(self.end)
    #     print(end_axis, np.degrees(end_angle))

    def current_transformation(self, frame):
        start_translation, start_rotation, start_scale, start_axis, start_angle = decompose_affine(self.start)
        end_translation, end_rotation, end_scale, end_axis, end_angle = decompose_affine(self.end_rotation)

        translation = start_translation + (end_translation - start_translation) * (frame / self.frames)
        angle = start_angle + (end_angle - start_angle) * (frame / self.frames)
        scales = start_scale + (end_scale - start_scale) * (frame / self.frames)

        T = Mat4x4.translation(translation)
        R = Mat4x4.rotation(angle, end_axis)
        S = Mat4x4.scale(scales)

        transformation = T * R * S
        return transformation
