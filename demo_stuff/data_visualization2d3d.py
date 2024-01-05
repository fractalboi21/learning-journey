import matplotlib.pyplot as plt
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y, label='sin(x)')
plt.title('2D Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create sample 3D data
theta = np.linspace(0, 10 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
z = theta

# Plot the 3D data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='3D Spiral')
ax.set_title('3D Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
plt.show()