import numpy as np
import matplotlib.pyplot as plt

# Create a grid of (x, y) points
x = np.linspace(-3, 3, 300)
y = np.linspace(-3, 3, 300)
X, Y = np.meshgrid(x, y)

# t = np.linspace(0, 3, 300)
# B_i = 1
# B_j = 2

# X, Y = np.meshgrid(t, t)

# Compute ||x - y||
distance = np.abs(X - Y)
Z = np.where(distance <= 1, 1, 1 / (1 + (np.abs(X - Y) - 1)**2))

# define deadzones
# D1min = -2
# D1max = -1

# D2min = 0
# D2max = 1

# Define the piecewise function
# Z = np.where(~(((D1min <= X) & (X <= D1max)) | ((D1min <= Y) & (Y <= D1max)) | ((D2min <= X) & (X <= D2max)) | ((D2min <= Y) & (Y <= D2max))), np.where(distance <= 1, 1, 1 / (1 + (np.abs(X - Y) - 1)**2)), 0)

# define obstacles
# O1min = -2
# O1max = -1

# O2min = 0
# O2max = 1

# Define the piecewise function
# need to check if the line between the two points x and y intersects with either obstacle.
# in 1D, this only doesn't happen if x and y are both in the same interval excluding the obstacles
# Z = np.where(((X <= O1min) & (Y <= O1min)) | ((X >= O1max) & (Y >= O1max) & (X <= O2min) & (Y <= O2min)) | ((X >= O2max) & (Y >= O2max)), np.where(distance <= 1, 1, 1 / (1 + (np.abs(X - Y) - 1)**2)), 0)




# # define the battery piecewise function
# Z = 1 / (1 + np.maximum(0, X - B_i)**2 + np.maximum(0, Y - B_j)**2)
# # Create the 2D contour plot
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, Z, levels=np.linspace(0, 1, 51), cmap='viridis', vmin=0, vmax=1)
# Correct spatial boundary labeling
plt.contour(X, Y, X - Y, levels=[1], colors='red', linewidths=2, linestyles='--')
plt.contour(X, Y, X - Y, levels=[-1], colors='red', linewidths=2, linestyles='--')

# # correct temporal boundary labeling
# plt.plot([0, B_i], [B_j, B_j], color='red', linestyle='--', linewidth=2)  # top edge
# plt.plot([B_i, B_i], [0, B_j], color='red', linestyle='--', linewidth=2)  # right edge


# Add a colorbar
cbar = plt.colorbar(contour, ticks=np.linspace(0, 1, 11))
cbar.set_label(r'$p$')

# Labels
# plt.xlabel(r'$t_i$')
# plt.ylabel(r'$t_j$')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title(r'$p(x_1, x_2)$ in One Dimension')
# plt.title(r'$p(x_1, x_2)$ in One Dimension with $D=[-2, -1] \cup [0, 1]$')
# plt.title(r'$p(x_1, x_2)$ in One Dimension with $O=[-2, -1] \cup [0, 1]$')
# plt.title(r'$p(t_i, t_j)$ with $B_i = 1$ and $B_j = 2$')

plt.show()


'''
import numpy as np
import matplotlib.pyplot as plt

# Define a range of distances ||x - y||
d = np.linspace(0, 10, 500)

R = 1
# Define z(d) as piecewise
z = np.where(d <= R, 1, 1 / (1 + (d-R)**2))

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(d, z)
plt.axvline(x=1, color='red', linestyle='--', label=r'$d=R$ (boundary)')

# Labels
plt.xlabel(r'$d_{i j}$')
plt.ylabel(r'$p$')
plt.title(r'Probability with respect to distance $(\kappa = 1, R = 1)$')
plt.legend()
plt.grid(True)

plt.show()

'''