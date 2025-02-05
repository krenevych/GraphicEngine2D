from abc import abstractmethod, ABCMeta

from src.math.Mat3x3 import Mat3x3


class Base(metaclass=ABCMeta):

    def __init__(self, *vertices):
        self._geometry = []
        self._transformation = Mat3x3()
        self.color = "black"

    def set_transformation(self, transformation):
        self._transformation = transformation

    @property
    def transformation(self):
        return self._transformation

    @property
    def transformed_geometry(self):
        geom = [self.transformation * point for point in self._geometry]
        return geom

    def apply_transformation_to_geometry(self):
        self._geometry = self.transformed_geometry
        self.set_transformation(Mat3x3.identity())


    @abstractmethod
    def draw_model(self):
        pass

    def draw(self):
        self.draw_model()
        # self.__draw_pivot()
        # self.__draw_local_frame()