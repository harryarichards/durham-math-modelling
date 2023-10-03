import matplotlib.pyplot as plt
import numpy as np

# Create 'Figure' and 'Axis' objects for a figure
# with two plots below each other.

f, ax = plt.subplots(2)

# Generate the first plot.
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x ** 2)
ax[0].plot(x,y)
ax[0].set_title('First plot')

# Generate the second plot.
y = np.cos(x ** 2)
ax[1].plot(x,y)
ax[1].set_title('Second plot')

# Show all in one window.
plt.show()

