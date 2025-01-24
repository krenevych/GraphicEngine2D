from src.base.scene import draw_scene
from src.engine.drawer import line2d
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import Vec3


class BaseModel:

    def __init__(self, *vertices):
        self.__translation = Vec3.point()
        self.__rotation = 0.0
        self.__scale = Vec3(1, 1, 1)
        self.__pivot = Vec3.point(0, 0)
        self.__data = list(vertices)

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

    def pivot(self, tx, ty):
        if ty is None and isinstance(tx, Vec3):
            self.__pivot = Vec3(tx.xy)
        else:
            self.__pivot = Vec3(tx, ty, 1)


    @property
    def transformation(self):
        T = Mat3x3.translation(self.__translation)
        R = Mat3x3.rotation(self.__rotation, False)
        S = Mat3x3.scale(self.__scale)

        return T * R * S

    def draw(self):
        M = self.transformation
        transformed_data = []
        for point in self.__data:
            _p = M * point
            transformed_data.append(_p)

        line2d(*transformed_data, closed=True)


def scene():
    v0 = Vec3.point(0, 0)
    v1 = Vec3.point(1, 0)
    v2 = Vec3.point(1, 1)
    v3 = Vec3.point(0, 1)
    m = BaseModel(v0, v1, v2, v3)

    m.draw()

    m.scale(2, 1)
    m.translation(Vec3.point(2, 2))
    m.rotation(45)

    m.draw()


if __name__ == '__main__':
    draw_scene(
        scene=scene,
        coordinate_rect=(-1, -1, 5, 5),
        # grid_show=False,
        base_axis_show=False,
        axis_show=True,
        axis_color="red",
        axis_line_style="-."
    )
