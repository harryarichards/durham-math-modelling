import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rectangle import Rectangle

class RectangleFilled(Rectangle): # RectangleFilled: a subclass of Rectangle

    def draw(self,format):
        """Plot the rectangle using the given pyplot format
        :param format : format for ploting function
        """

        # translaste "x-" into a colour name
        cols = { "k":"black", "r":"red", "g":"green", "b":"blue",\
                 "c":"cyan","m":"magenta","y":"yellow",} 
        colour = cols[format[0]] # use only the letter
        
        currentAxis = plt.gca()
        currentAxis.add_patch(patches.Rectangle(
                          (self.x, self.y), # (x,y)
                          self.Lx,       # width
                          self.Ly,       # height
                          facecolor=colour # needs a colour name
                          ))


if __name__ == "__main__": # ONLY EXECUTE WHEN MODULE NOT IMPORTED
    rec1 = Rectangle(0.0,1.0,10,15) # create rectangle: x=0,y=1,Lx=10,Ly=20
    rec1.draw("b-")                 # plot rectangle in blue
    
    rec2 = RectangleFilled(3.0,2.0,5,7) # create a red filled rectangle
    rec2.draw("r-")                     # plot red rectangle
    
    rec1.move(2.0,1.5)              # move the 1st rectangle by dx=2 dy=1.5
    rec1.draw("r-")                 # plot the translated rectangle in red

    rec2.move(-2.0,-2.0)            # move the 2nd rectangle by dx=dy=-2
    rec2.draw("g-")                 # plot the translated rectangle 

    rec2.draw_moved(8.0,7.0,"m-")   # draw move in magenta

    plt.axis('equal')
    plt.margins(0.1, 0.1)           
    plt.show()
