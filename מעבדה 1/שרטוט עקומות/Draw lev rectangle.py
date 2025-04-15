import numpy as np
import matplotlib.pyplot as plt


#draw lev
# Create a grid of x and y values
x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)
X, Y = np.meshgrid(x, y)

# Apply the equation to each point in the grid
# The equation x^2 + (y - cbrt(x^2))^2 = 1 becomes F(X, Y) = 0 where F(X, Y) = X**2 + (Y - cbrt(X**2))^2 - 1
F = X**2 + (Y - X**(2/3))**2 - 1

# Plot the contour where F(X, Y) equals 0 (which represents the original equation = 1)
plt.figure(figsize=(6,6))
plt.contour(X, Y, F, levels=[0], colors='blue')

# Set the aspect of the plot to be equal
#plt.gca().set_aspect('equal', adjustable='box')

# Add labels and title


# Show the plot
plt.show()
