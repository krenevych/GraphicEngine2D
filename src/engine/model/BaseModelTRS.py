from src.engine.model.Model import Model
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import Vec3, vertex
from src.math.utils_matrix import decompose_affine3


class BaseModelTRS(Model):

    def __init__(self, *vertices):
        super().__init__(*vertices)
        self.__translation = vertex()
        self.__rotation = 0.0
        self.__scale = Vec3(1, 1, 1)

    def scale(self, sx, sy=None):
        if sy is None and isinstance(sx, Vec3):
            self.__scale = Vec3(*sx)
        else:
            self.__scale = Vec3(sx, sy, 1)

    def translation(self, tx, ty=None):
        if ty is None and isinstance(tx, Vec3):
            self.__translation = Vec3(*tx)
        else:
            self.__translation = Vec3(tx, ty, 1)

    def rotation(self, angle):
        self.__rotation = angle

    @property
    def transformation(self):
        T = Mat3x3.translation(self.__translation)
        R = Mat3x3.rotation(self.__rotation, True)
        S = Mat3x3.scale(self.__scale)

        return T * R * S

    @transformation.setter
    def transformation(self, transformation):
        self.__translation, self.__rotation, self.__scale = decompose_affine3(transformation)
        self._transformation = transformation
