from src.engine.model.BaseModel import BaseModel
from src.math.Mat4x4 import Mat4x4
from src.math.Vec3 import Vec3
from src.math.Vec4 import Vec4


class BaseModelTRS(BaseModel):

    def __init__(self, *vertices):
        super().__init__(*vertices)
        self.__translation = Vec4.point()
        self.__rotation = 0.0
        self.__scale = Vec3(1, 1, 1)

    def scale(self, sx, sy=None, sz=None):
        if sy is None and isinstance(sx, (Vec3, Vec4)):
            self.__scale = Vec3(*sx.xyz)
        else:
            self.__scale = Vec3(sx, sy, sz)

    def translation(self, tx, ty=None, tz=None):
        if ty is None and isinstance(tx, (Vec3, Vec4)):
            self.__translation = Vec4(*tx.xyz)
        else:
            self.__translation = Vec4(tx, ty, tz, 1)

    def rotation(self, angle):
        self.__rotation = angle

    def set_transformation(self, transformation):
        self.__translation, self.__rotation, self.__scale = Mat4x4.decompose_affine(transformation)
        self._transformation = transformation

    @property
    def transformation(self):
        T = Mat4x4.translation(self.__translation)
        R = Mat4x4.rotation(self.__rotation, True)
        S = Mat4x4.scale(self.__scale)

        return T * R * S
