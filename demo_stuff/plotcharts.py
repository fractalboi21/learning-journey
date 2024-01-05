import matplotlib.pyplot as plt

import numpy as np
 
# Generate random data for the histogram

data = np.random.randn(1000)
 
# Plotting a basic histogram

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
 
# Adding labels and title

plt.xlabel('Values')

plt.ylabel('Frequency')

plt.title('Basic Histogram')
 
# Display the plot
plt.show()