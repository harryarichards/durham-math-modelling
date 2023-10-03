import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rectangle import Rectangle

class RectangleNamed(Rectangle):
    def __init__(self,x,y,Lx,Ly,name):
        """
        Constructor: initialise a few internal variables
        :param x : left coordinate of rectangle
        :param y : lower coordinate of rectangle
        :param Lx : horizontal size
        :param Ly : vertical size
        :param name: rectangle name
        """
        # call __init__() from parent class : Rectangle 
        super(RectangleNamed,self).__init__(x,y,Lx,Ly)
        self.name = name

    def reset_name(self,name):
        """ Modify the rectangle name
        :param name: rectangle new name
        """
        self.name = name
        
    def draw(self,colour):
        """Plot the rectangle using the given colour
        :param colour: drawing colour
        """
        # call draw() from parent class : Rectangle 
        super(RectangleNamed,self).draw(colour)

        # coordinate of middle of rectangle: where to write the name
        x = self.x+self.Lx/2
        y = self.y+self.Ly/2
        
        plt.gca().text(x,y, self.name, fontsize=15)

if __name__ == "__main__": # ONLY EXECUTE WHEN MODULE NOT IMPORTED
    rec1 = Rectangle(0.0,1.0,10,15) # create rectangle: x=0, y=1, Lx=10, Ly=20
    rec1.draw("b-")                 # plot rectangle in blue
    
    rec2 = RectangleNamed(3.0,2.0,5,7,"two") # create named rectangle
    rec2.draw("r-")                     # plot named rectangle
    
    rec3 = RectangleNamed(-3.0,2.0,4,5,"three") # create name rectangle
    rec3.draw("k-")                     # plot named rectangle

    rec2.draw_moved(8.0,7.0,"m-") # draw moved named rectangle

    rec2.reset_name("two B")
    rec2.draw_moved(-4.0,4.0,"c-")
    
    plt.axis('equal')
    plt.margins(0.1, 0.1)           
    plt.show()
