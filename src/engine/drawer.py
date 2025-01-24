from src.utils.broken_line import draw_broken_line
from src.utils.text import DEFAULT_LABEL_FONT_SIZE
from src.utils.scene import draw_scene


def line2d(*poins,
           color="black", closed=False,
           linewidth=1.0, line_style="solid",
           vertex_color="black", vertex_size=50,
           labels="", labels_color="black", labels_fontsize=DEFAULT_LABEL_FONT_SIZE):
    ps = []
    for el in poins:
        ps.append(el.get2())

    if closed:
        ps.append(poins[0].get2())

    draw_broken_line(ps,
                     color=color,
                     vertex_color=vertex_color,
                     vertex_size=vertex_size,
                     linewidth=linewidth,
                     line_style=line_style,
                     labels=labels,
                     labels_color=labels_color,
                     labels_font_size=labels_fontsize)
    # draw_vector(, color, label, label_color, label_fontsize, label_offset)

def scene():
        pass

if __name__ == '__main__':
    draw_scene(
        scene=scene,
    )
