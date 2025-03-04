from src.engine.animation.Animation import Animation
from src.math.Mat4x4 import Mat4x4
from src.math.utils_matrix import decompose_translation_scale_quaternion
from src.math.utils_quat import slerp


class QuaternionAnimation(Animation):

    def __init__(self, end, **kwargs):  # end - Quaternion
        super().__init__(end, **kwargs)
        self.start_translation, self.start_rotation, self.start_scale = decompose_translation_scale_quaternion(self.start)
        self.end_rotation = end

    def current_transformation(self, frame):
        t = frame / self.frames

        interpolated = slerp(self.start_rotation, self.end_rotation, t)

        T = Mat4x4.translation(self.start_translation)
        R = interpolated.toRotationMatrix()
        S = Mat4x4.scale(self.start_scale)

        transformation = T * R * S
        return transformation
