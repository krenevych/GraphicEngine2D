import tkinter as tk
import math

class CoordinateSystem3D:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.scale = 500

    def draw_axis(self):
        # Axis colors
        x_color = 'red'
        y_color = 'green'
        z_color = 'blue'

        # Define axis endpoints in 3D space
        x_axis = [(0, 0, 0), (1, 0, 0)]
        y_axis = [(0, 0, 0), (0, 1, 0)]
        z_axis = [(0, 0, 0), (0, 0, 1)]

        # Draw each axis
        self.draw_line_3d(x_axis, x_color)
        self.draw_line_3d(y_axis, y_color)
        self.draw_line_3d(z_axis, z_color)

    def project_point(self, x, y, z):
        # Simple perspective projection
        factor = self.scale / (z + 3)
        proj_x = self.center_x + int(x * factor)
        proj_y = self.center_y - int(y * factor)
        return proj_x, proj_y

    def draw_line_3d(self, line, color):
        (x1, y1, z1), (x2, y2, z2) = line
        x1_proj, y1_proj = self.project_point(x1, y1, z1)
        x2_proj, y2_proj = self.project_point(x2, y2, z2)
        self.canvas.create_line(x1_proj, y1_proj, x2_proj, y2_proj, fill=color, width=2)


    def increase_scale(self):
        self.scale += 50
        self.canvas.delete("all")  # Очистити canvas
        self.draw_axis()  # Перемалювати осі

    def decrease_scale(self):
        self.scale -= 50
        self.canvas.delete("all")  # Очистити canvas
        self.draw_axis()  # Перемалювати осі



def main():
    # Window setup
    root = tk.Tk()
    root.title("3D Coordinate System")

    # Canvas dimensions
    width = 800
    height = 600

    # Create canvas
    canvas = tk.Canvas(root, width=width, height=height, bg='white')
    canvas.pack()

    # Draw 3D coordinate system
    coord_system = CoordinateSystem3D(canvas, width, height)
    coord_system.draw_axis()

    # Кнопки для масштабування
    btn_increase = tk.Button(root, text="Zoom In", command=lambda : coord_system.increase_scale())
    btn_increase.pack()

    btn_decrease = tk.Button(root, text="Zoom Out", command=lambda : coord_system.decrease_scale())
    btn_decrease.pack()

    # Start the Tkinter loop
    root.mainloop()

if __name__ == "__main__":
    main()
