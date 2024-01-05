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



import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.bar(langs,students)

plt.show()

# Import libraries

from matplotlib import pyplot as plt

import numpy as np
 
 
# Creating dataset

cars = ['AUDI', 'BMW', 'FORD',

        'TESLA', 'JAGUAR', 'MERCEDES']
 

data = [23, 17, 35, 29, 12, 41]
 
# Creating plot

fig = plt.figure(figsize =(10, 7))

plt.pie(data, labels = cars)
 
# show plot
plt.show()