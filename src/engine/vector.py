from src.base.arrow import draw_vector
from src.base.scene import draw_scene
from src.base.text import DEFAULT_LABEL_FONT_SIZE
from src.math.Mat3x3 import Mat3x3
from src.math.Vec3 import Vec3

def vector(direction: Vec3 = Vec3(1, 0, 0), origin: Vec3 = Vec3(),
           color="black",
           label="", label_color="black", label_fontsize=DEFAULT_LABEL_FONT_SIZE, label_offset=(0, 0)):
    # малювання вектора
    draw_vector(origin.xy, direction.xy,
                color, label, label_color, label_fontsize, label_offset)


def scene():
    o = Vec3.point(1, 1)
    v = Vec3.vect(1, 0)

    vector(direction=v, color="grey")

    T = Mat3x3.translation(1, 1)
    R = Mat3x3.rotation(20, False)
    S = Mat3x3.scale(2, 2)

    v1 = T * v
    vector(v1, color="red")

    v2 = R * v
    vector(v2, color="green")






if __name__ == '__main__':
    draw_scene(
        scene=scene,
        coordinate_rect=(-1, -1, 3, 3),
        # grid_show=False,
        base_axis_show=False,
        # axis_show=True,
        # axis_color="red",
        # axis_line_style="-."
    )
