import tkinter as tk
import math

class CoordinateSystem3D:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.scale = 200
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

    def draw_axis(self):
        self.canvas.delete("all")
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

    def rotate_point(self, x, y, z):
        # Rotation around X-axis
        y, z = (
            y * math.cos(self.angle_x) - z * math.sin(self.angle_x),
            y * math.sin(self.angle_x) + z * math.cos(self.angle_x),
        )
        # Rotation around Y-axis
        x, z = (
            x * math.cos(self.angle_y) + z * math.sin(self.angle_y),
            -x * math.sin(self.angle_y) + z * math.cos(self.angle_y),
        )
        # Rotation around Z-axis
        x, y = (
            x * math.cos(self.angle_z) - y * math.sin(self.angle_z),
            x * math.sin(self.angle_z) + y * math.cos(self.angle_z),
        )
        return x, y, z

    def project_point(self, x, y, z):
        # Apply rotation
        x, y, z = self.rotate_point(x, y, z)
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


def main():
    def rotate_x(event):
        coord_system.angle_x += math.radians(5)
        coord_system.draw_axis()

    def rotate_y(event):
        coord_system.angle_y += math.radians(5)
        coord_system.draw_axis()

    def rotate_z(event):
        coord_system.angle_z += math.radians(5)
        coord_system.draw_axis()

    # Window setup
    root = tk.Tk()
    root.title("3D Coordinate System with Rotation")

    # Canvas dimensions
    width = 800
    height = 600

    # Create canvas
    canvas = tk.Canvas(root, width=width, height=height, bg='white')
    canvas.pack()

    # Draw 3D coordinate system
    coord_system = CoordinateSystem3D(canvas, width, height)
    coord_system.draw_axis()

    # Bind keys for rotation
    root.bind("<Left>", lambda e: rotate_y(e))  # Rotate left (Y-axis)
    root.bind("<Right>", lambda e: rotate_y(e))  # Rotate right (Y-axis)
    root.bind("<Up>", lambda e: rotate_x(e))  # Rotate up (X-axis)
    root.bind("<Down>", lambda e: rotate_x(e))  # Rotate down (X-axis)
    root.bind("<z>", lambda e: rotate_z(e))  # Rotate around Z-axis (clockwise)
    root.bind("<x>", lambda e: rotate_z(e))  # Rotate around Z-axis (counterclockwise)

    # Start the Tkinter loop
    root.mainloop()


if __name__ == "__main__":
    main()
