import matplotlib.pyplot as pyplot
import math

# Turn on interactive mode and show the plot window. We do
# this only once.
pyplot.ion()
pyplot.show()

t=0
while True:
    # Tell pyplot what we want to plot: two data sets, which both depend
    # on the value of the 't' parameter.
    pyplot.plot([0, 1, 2],   [0,  math.sin(t), 0], '-o')
    pyplot.plot([0, 1.5, 2], [0, -math.sin(t), 0], '-o')
    # Set the range of y-values.
    pyplot.ylim([-1,1])
    # Draw everything.
    pyplot.draw()
    # Remove the two drawing commands from the stack.
    pyplot.cla()
    # Update time.
    t+=0.1
