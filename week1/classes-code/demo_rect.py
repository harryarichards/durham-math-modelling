import matplotlib.pyplot as plt

# coordinates of the rectangle
x1 = 0
y1 = 0
x2 = 3
y2 = 2

# list of coordinates. The first point must be repeated at the end
# to draw the last segment.
X = [x1,x2,x2,x1,x1] 
Y = [y1,y1,y2,y2,y1]

plt.plot(X,Y,'b-')    # join the 5 points with lines
plt.axis('equal')     # ensure a square is a square on the screen
plt.margins(0.1, 0.1) # add some space on the edges          
plt.show()            # display on screen
