from abc import ABC

import matplotlib
from matplotlib import pyplot as plt

from src.base.axes import draw_axes
from src.engine.scene.Frame import Frame, FrameCallback

matplotlib.use("TkAgg")


class Scene(ABC):

    def __init__(self,
                 image_size=(5, 5),
                 coordinate_rect=(-1, -1, -1, 1, 1, 1),
                 title="Picture",
                 base_axis_show=False,
                 grid_show=False,
                 axis_show=True,
                 axis_show_from_origin=True,
                 axis_color=("red", "green", "blue"),
                 axis_line_style="-.",
                 axis_line_width=1.0,

                 ):
        self.image_size = image_size
        self.coordinate_rect = coordinate_rect
        self.title = title
        self.base_axis_show = base_axis_show
        self.axis_show = axis_show
        self.axis_show_from_origin = axis_show_from_origin
        self.axis_color = axis_color
        self.axis_line_style = axis_line_style
        self.axis_line_width = axis_line_width
        self.grid_show = grid_show

        self.figure = plt.figure(figsize=self.image_size)
        self.plt_axis = self.figure.add_subplot(111, projection="3d")

        self.figures = {}

        self.frame_sequence: list[Frame] = []

    def add_figure(self, figure, name="default"):
        if name not in self.figures:
            self.figures[name] = figure
        else:
            raise KeyError("Figure name {} already exists".format(name))

    def get_figure(self, name):
        return self.figures[name]

    def __setitem__(self, name, figure):
        self.add_figure(figure, name)

    def __getitem__(self, item):
        return self.figures[item]

    def show_axes(self):
        if self.axis_show:
            draw_axes(
                self.plt_axis,
                self.coordinate_rect,
                self.axis_color,
                self.axis_line_style,
                linewidth=self.axis_line_width,
                axis_show_from_origin=self.axis_show_from_origin,
            )

        self.plt_axis.set_xlim([self.coordinate_rect[0], self.coordinate_rect[3]])
        self.plt_axis.set_ylim([self.coordinate_rect[1], self.coordinate_rect[4]])
        self.plt_axis.set_zlim([self.coordinate_rect[2], self.coordinate_rect[5]])

        # Вирівнювання масштабу осей
        self.plt_axis.set_box_aspect([1, 1, 1])

    def setup_base_parameters(self):

        self.plt_axis.view_init(elev=110,
                                azim=225,
                                roll=-45)

        # self.plt_axis.view_init(elev=110,
        #                         azim=245,
        #                         roll=-25)

        # # Відключення стандартних осей
        if not self.base_axis_show:
            self.plt_axis.axis('off')

        self.plt_axis.grid(self.grid_show)

    def set_title(self):
        # Назва графіка
        self.plt_axis.set_title(self.title)

    def draw(self, name=None):
        if name is None:
            self.draw_frames()
        elif name in self.figures:
            self[name].draw()
        else:
            raise KeyError("Figure {} doesn't exist to draw".format(name))

    def add_frames(self, *frames):
        for frame in frames:
            if isinstance(frame, Frame):
                self.frame_sequence.append(frame)
            elif callable(frame):
                self.frame_sequence.append(FrameCallback(frame))

    def draw_frames(self):
        for frame in self.frame_sequence:
            frame.on_frame(self)

            for name, figure in self.figures.items():
                figure.draw()

    def prepare(self):
        self.set_title()
        self.setup_base_parameters()
        self.show_axes()
        return self

    def finalize(self):
        plt.show()
