from matplotlib import pyplot as plt

from src.base.axes import draw_axes


def default_scene():
    ##########################
    # Draw here
    ##########################

    pass

def show_axes(axis_show, coordinate_rect, axis_color, axis_line_style):
    if axis_show:
        draw_axes(coordinate_rect, axis_color, axis_line_style)

    plt.xlim(coordinate_rect[0], coordinate_rect[2])
    plt.ylim(coordinate_rect[1], coordinate_rect[3])



def setup_base_parameters(base_axis_show,
                          keep_aspect_ratio,
                          grid_show, grid_line_linestyle, greed_alpha):
    # Відключення стандартних осей
    if not base_axis_show:
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)

    if keep_aspect_ratio:
        plt.gca().set_aspect('equal', adjustable='box')

    if grid_show:
        plt.grid(grid_show, linestyle=grid_line_linestyle, alpha=greed_alpha, )
    else:
        plt.grid(False)

def set_title(title):
    plt.title(title)

def draw_scene(
        scene=default_scene,
        image_size=(5, 5),
        coordinate_rect=(-1, -1, 1, 1),
        title="Picture",
        base_axis_show=True, axis_show=False, axis_color=("red", "green"), axis_line_style="-.",
        grid_show=True, grid_line_linestyle="solid", greed_alpha=1.0,
        keep_aspect_ratio=True,
):
    plt.figure(figsize=image_size)

    set_title(title)

    setup_base_parameters(base_axis_show, keep_aspect_ratio, grid_show, grid_line_linestyle, greed_alpha)
    show_axes(axis_show, coordinate_rect, axis_color, axis_line_style)

    scene()

    plt.show()


if __name__ == '__main__':
    draw_scene(
        scene=default_scene,
        coordinate_rect=(-3, -3, 4, 4),
        base_axis_show=True,  # set False to hide axis
        axis_show=True,
        # axis_color=("green","red"),
        grid_show=True,
        grid_line_linestyle='--',
        greed_alpha=0.5,
    )
