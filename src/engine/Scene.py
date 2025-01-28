from abc import abstractmethod, ABC

from matplotlib import pyplot as plt

from src.base.axes import draw_axes


class Scene(ABC):

    def __init__(self,
                 image_size=(5, 5),
                 coordinate_rect=(-1, -1, 1, 1),
                 title="Picture",
                 base_axis_show=True,
                 axis_show=False, axis_color=("red", "green"), axis_line_style="-.",
                 grid_show=True, grid_line_linestyle="solid", greed_alpha=1.0,
                 keep_aspect_ratio=True, ):
        self.image_size = image_size
        self.coordinate_rect = coordinate_rect
        self.title = title
        self.base_axis_show = base_axis_show
        self.axis_show = axis_show
        self.axis_color = axis_color
        self.axis_line_style = axis_line_style
        self.grid_show = grid_show
        self.grid_line_linestyle = grid_line_linestyle
        self.greed_alpha = greed_alpha
        self.keep_aspect_ratio = keep_aspect_ratio

        self.figure = plt.figure(figsize=self.image_size)

    def show_axes(self):
        if self.axis_show:
            draw_axes(self.coordinate_rect, self.axis_color, self.axis_line_style)

        plt.xlim(self.coordinate_rect[0], self.coordinate_rect[2])
        plt.ylim(self.coordinate_rect[1], self.coordinate_rect[3])

    def setup_base_parameters(self):
        # Відключення стандартних осей
        if not self.base_axis_show:
            plt.gca().spines['bottom'].set_visible(False)
            plt.gca().spines['left'].set_visible(False)
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)

        if self.keep_aspect_ratio:
            plt.gca().set_aspect('equal', adjustable='box')

        if self.grid_show:
            plt.grid(self.grid_show, linestyle=self.grid_line_linestyle, alpha=self.greed_alpha, )
        else:
            plt.grid(False)

    def set_title(self):
        plt.title(self.title)

    def draw(self):
        self.set_title()

        self.setup_base_parameters()
        self.show_axes()

        self.draw_scene()

        plt.show()

    @abstractmethod
    def draw_scene(self):
        pass


