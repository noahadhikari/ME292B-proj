import numpy as np
import matplotlib.pyplot as plt

# Create a grid of (x, y) points (Agent 2's position)
x = np.linspace(-3, 3, 300)
y = np.linspace(-3, 3, 300)
X, Y = np.meshgrid(x, y)

# Agent 1 is fixed at (0, 0)
agent1_pos = np.array([0.0, 0.0])

# Compute distance from Agent 2 (X, Y) to Agent 1 (0, 0)
distance = np.sqrt((X - agent1_pos[0])**2 + (Y - agent1_pos[1])**2)

# Define the communication probability function
R = 1  # Communication radius
Z = np.where(distance <= R, 1, 1 / (1 + (distance - R)**2))

# Create the 2D contour plot
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, levels=np.linspace(0, 1, 51), cmap='viridis', vmin=0, vmax=1)

# Mark agent 1's fixed position
plt.plot(0, 0, 'ro', markersize=8, label="Fixed Agent 1 (0,0)")

# Correct spatial boundary labeling. should be a circle at R=1 centered at (0, 0)

plt.contour(X, Y, distance, levels=[R], colors='red', linewidths=2, linestyles='--')


# Add a colorbar
cbar = plt.colorbar(contour, ticks=np.linspace(0, 1, 11))
cbar.set_label(r'$p$')

# Labels
plt.xlabel(r'$x$ (Agent 2)')
plt.ylabel(r'$y$ (Agent 2)')
plt.title(r'Communication Probability $p(x_1, x_2)$ with $x_1 = (0, 0)$')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Keep aspect ratio correct (circles look like circles)

plt.show()
