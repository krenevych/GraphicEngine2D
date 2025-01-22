import numpy as np
from matplotlib import pyplot as plt

from Projection import label_size

DEFAULT_LABEL_FONT_SIZE = 20
FONT_SIZE = DEFAULT_LABEL_FONT_SIZE

def print_label(start,
                label="", label_color="black", label_fontsize=DEFAULT_LABEL_FONT_SIZE, label_offset=(0, 0)):

    if label is not None and label != "":
        label_pos = np.array(start) + label_offset
        plt.text(float(label_pos[0]), float(label_pos[1]), label, fontsize=label_fontsize, color=label_color,
                 ha='left')