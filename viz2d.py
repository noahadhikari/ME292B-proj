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

# define a function to determine if an agent is in a deadzone
def in_deadzones(X, Y):
    # Define deadzones (example)
    D_centers = [(-1, -1), (1, 1), (-1, 2)]
    D_radii = [0.5, 0.5, 1]

    result = np.zeros_like(X, dtype=bool)
    for center, radius in zip(D_centers, D_radii):
        distances_to_center = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
        result |= (distances_to_center <= radius)

    return result

def hits_obstacle(X, Y):
    import numpy as np

    def segments_from_origin_circle_intersect(X2, Y2, cx, cy, R):
        # Vectorized: only X2, Y2 are variable (endpoints)
        dx = X2
        dy = Y2
        fx = -cx
        fy = -cy

        a = dx**2 + dy**2
        b = 2 * (fx * dx + fy * dy)
        c = fx**2 + fy**2 - R**2  # constant

        discriminant = b**2 - 4*a*c

        intersects = np.full_like(X2, False, dtype=bool)

        mask = discriminant >= 0
        valid_a = a[mask]
        valid_b = b[mask]
        valid_discriminant = np.sqrt(discriminant[mask])

        t1 = (-valid_b - valid_discriminant) / (2 * valid_a)
        t2 = (-valid_b + valid_discriminant) / (2 * valid_a)

        intersects_masked = (0 <= t1) & (t1 <= 1) | (0 <= t2) & (t2 <= 1)

        intersects[mask] = intersects_masked

        return intersects

        

    O_centers = [(-1, -1), (1, 1), (-1, 2)]
    O_radii = [0.5, 0.5, 1]

    result = np.zeros_like(X, dtype=bool)

    for center, radius in zip(O_centers, O_radii):
        # Check if the line from (0, 0) to (X, Y) intersects with the circle
        intersects = segments_from_origin_circle_intersect(X, Y, center[0], center[1], radius)
        result |= intersects
    return result


Z = np.where(distance <= R, 1, 1 / (1 + (distance - R)**2))

# # Apply deadzone condition
# Z = np.where(in_deadzones(X, Y), 0, Z)

# Apply obstacle condition
Z = np.where(hits_obstacle(X, Y), 0, Z)

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
# plt.title(r'Communication Probability $p(x_1, x_2)$ with $x_1 = (0, 0)$')
plt.title(r'Obstacles Communication Probability $p(x_1, x_2)$ with $x_1 = (0, 0)$')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Keep aspect ratio correct (circles look like circles)

plt.show()
