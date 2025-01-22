import matplotlib.pyplot as plt

# Coordinates for the points
P1 = (0, 0)
P2 = (-1, 2)
P3 = (2, 3)

# Plotting the points
plt.figure(figsize=(6, 6))
plt.plot(*P1, 'ko', label="P1")
plt.plot(*P2, 'ko', label="P2")
plt.plot(*P3, 'ko', label="P3")

# Adding vectors
plt.arrow(P1[0], P1[1], P2[0] - P1[0], P2[1] - P1[1], color='blue', head_width=0.2, length_includes_head=True)
plt.arrow(P1[0], P1[1], P3[0] - P1[0], P3[1] - P1[1], color='brown', head_width=0.2, length_includes_head=True)

# Adding labels
plt.text(P1[0] - 0.3, P1[1] - 0.3, "$P_1$", fontsize=20, color="black", weight="bold")
plt.text(P2[0] - 0.5, P2[1] + 0.3, "$P_2$", fontsize=20, color="black", weight="bold")
plt.text(P3[0] + 0.3, P3[1] + 0.3, r"$\alpha_3$", fontsize=20, color="black", weight="bold")

# Formatting the plot
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-2, 3)
plt.ylim(-1, 4)
plt.grid(True)
plt.title("Візуалізація точок і векторів")
plt.gca().set_aspect('equal', adjustable='box')

# Save and display the plot
# file_path = "vector_plot_refined.png"
# plt.savefig(file_path)
plt.show()

