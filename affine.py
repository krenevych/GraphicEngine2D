import matplotlib.pyplot as plt

# Coordinates for points
P1 = (0, 0)
P = (1, 2)
v2 = (1, 0)
v3 = (0, 2)

# Create the plot
plt.figure(figsize=(6, 6))

# Plot the points
plt.plot(P1[0], P1[1], 'ko', label='P1')
plt.plot(P[0], P[1], 'ko', label='P')

# Add vectors
plt.arrow(P1[0], P1[1], v2[0], v2[1], color='blue', head_width=0.1, length_includes_head=True, label=r'$\alpha_2 v_2$')
plt.arrow(P1[0], P1[1], v3[0], v3[1], color='brown', head_width=0.1, length_includes_head=True, label=r'$\alpha_3 v_3$')
plt.arrow(v2[0], v2[1], v3[0], v3[1], color='brown', head_width=0.1, length_includes_head=True)
plt.arrow(v3[0], v3[1], v2[0], v2[1], color='blue', head_width=0.1, length_includes_head=True)

# Add labels
plt.text(P1[0] - 0.2, P1[1] - 0.2, r'$P_1$', fontsize=12)
plt.text(P[0] + 0.1, P[1] + 0.1, r'$P$', fontsize=12)
plt.text(v2[0] / 2 - 0.3, v2[1] / 2, r'$\alpha_2 v_2$', fontsize=12, color='blue')
plt.text(v3[0] / 2 - 0.3, v3[1] / 2 + 0.3, r'$\alpha_3 v_3$', fontsize=12, color='brown')

# Formatting the plot
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.xlim(-0.5, 2)
plt.ylim(-0.5, 3)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Visualization of Affine Combination")
plt.legend()

# Show the plot
plt.show()
