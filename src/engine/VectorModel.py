import numpy as np

from src.base.arrow import draw_segment
from src.engine.Scene import Scene
from src.engine.BaseModel import BaseModel
from src.math.Vec3 import Vec3, vertex


class VectorModel (BaseModel):
    AVAILABLE_PARAMETERS = [
        "color",  # default: , posible values:
        "line_style",  # default: , posible values:
        "linewidth",  # default: , posible values:
        "label",  # default: , posible values:
        "label_color",  # default: , posible values:
        "label_fontsize",  # default: , posible values:
        "label_offset",
    ]

    def __init__(self, *direction):
        super().__init__()
        self._availible_parameters += self.AVAILABLE_PARAMETERS

        self._geometry.append(vertex(0, 0))

        if len(direction) == 1:
            item = direction[0]
            if isinstance(item, Vec3):
                self._geometry.append(direction)
            elif isinstance(item, (np.ndarray, tuple, list)) and len(item) == 2:
                self._geometry.append(vertex(*item))
        elif len(direction)  == 2 and all(isinstance(item, (float, int)) for item in direction):
            self._geometry.append(vertex(*direction))
        else:
            raise ValueError("Data corrupted")

    def draw_model(self):
        transformed_geometry = self.transformed_geometry

        ps = [el.xy for el in transformed_geometry]

        draw_segment(*ps, **self._parameters)

if __name__ == '__main__':
    class SampleScene(Scene):
        def draw_figures(self):

            v = VectorModel(1, 1)
            v["color"] = "blue"
            v["label"] = "v"
            v["label_offset"] = -0.2, 0.1
            v.draw()

            v.translation(1, 2)
            v.rotation(np.radians(20))
            v.draw()



    scene = SampleScene(
        coordinate_rect=(-1, -1, 5, 5),
        grid_show=False,
        axis_show=True
    ).prepare()
    scene.draw_figures()
    scene.finalize()

