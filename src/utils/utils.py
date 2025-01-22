import numpy as np
from matplotlib import pyplot as plt

def calc_normal(start, end=None):
    if end is None:
        direction = start
        direction = direction / np.linalg.norm(direction)  # Нормалізація вектора

        # Обчислення перпендикулярного вектора
        __perpendicular = np.array([-direction[1], direction[0]])
        return __perpendicular
    else:
        # Вектор напряму лінії
        direction = end - start
        return calc_normal(direction)


def draw_axis(start, end,
              color="black", linewidth=1.0, linestyle="--", ):
    plt.plot(
        [start[0], end[0]], [start[1], end[1]],
        color=color, linestyle=linestyle, linewidth=linewidth
    )


def create_coordinate_system(image_size=(5, 5),
                             coordinate_rect=(-1, -1, 1, 1),
                             title="Picture",
                             base_axis_show=True, axis_show=False, axis_color ="red", axis_line_style ="-.",
                             grid_show=True, grid_line_linestyle="solid", greed_alpha=1.0,
                             keep_aspect_ratio=False,
                             ):
    plt.figure(figsize=image_size)
    plt.xlim(coordinate_rect[0], coordinate_rect[2])
    plt.ylim(coordinate_rect[1], coordinate_rect[3])
    if keep_aspect_ratio:
        plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    if grid_show:
        plt.grid(grid_show, linestyle=grid_line_linestyle, alpha=greed_alpha, )
    else:
        plt.grid(False)

    if axis_show:
        shift_offset = 0.1

        y_len = coordinate_rect[3] - coordinate_rect[1]
        shift = y_len * shift_offset / 2

        start_x = (0.0, coordinate_rect[1] + shift)
        end_x = (0.0, coordinate_rect[3] - shift)
        draw_axis(start_x, end_x, color=axis_color, linestyle=axis_line_style)

        x_len = coordinate_rect[2] - coordinate_rect[0]
        x_shift = x_len * shift_offset / 2

        start_x = (coordinate_rect[0] + x_shift, 0.0)
        end_x = (coordinate_rect[2] - x_shift, 0.0)
        draw_axis(start_x, end_x, color=axis_color, linestyle=axis_line_style)

    # Відключення стандартних осей
    if not base_axis_show:
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)


if __name__ == '__main__':
    create_coordinate_system(
        coordinate_rect=(-5, -3, 4, 4),
        base_axis_show=True,  # set False to hide axis
        axis_show=True,
        grid_show=True,
        grid_line_linestyle='--',
        greed_alpha=0.5,
    )

    ##########################
    # Draw here
    ##########################

    plt.show()
