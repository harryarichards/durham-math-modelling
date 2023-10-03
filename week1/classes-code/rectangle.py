import matplotlib.pyplot as plt

class Rectangle:
    def __init__(self,x,y,Lx,Ly):
        """
        Constructor: initialise a few internal variables
        :param x : left coordinate of rectangle
        :param y : lower coordinate of rectangle
        :param Lx : horizontal size
        :param Ly : vertical size
        """
        self.x = x
        self.y = y
        self.Lx = Lx
        self.Ly = Ly
        
    def move(self,dx,dy):
        """ Translate the rectangle by dx and dy
        :param dx : horizontal displacement
        :param dy : vertical displacement
        """
        self.x += dx
        self.y += dy
        
    def draw(self,format="k-"):
        """Plot the rectangle using the given pyplot format
        :param format : format for plot function
        """
        x_list = [self.x,self.x+self.Lx,self.x+self.Lx,self.x,self.x]
        y_list = [self.y,self.y,self.y+self.Ly,self.y+self.Ly,self.y]
        plt.plot(x_list,y_list,format) 

    def draw_moved(self,dx,dy,format="k-"):
        """ Draw rectangle in position shifted by (dx,dy)
        :param dx : horizontal displacement
        :param dy : vertical displacement
        """
        self.move(dx,dy)   # translate the rectangle
        self.draw(format)  # plot the displaced rectangle
        self.move(-dx,-dy) # translate the rectangle back
        
if __name__ == "__main__": # ONLY EXECUTE WHEN MODULE NOT IMPORTED
    rec1 = Rectangle(0.0,1.0,10,15) # create rectangle: x=0,y=1,Lx=10,Ly=20
    rec1.draw("b-")                 # plot rectangle in blue
    
    rec2 = Rectangle(3.0,4.0,5,5)   # create a square
    rec2.draw("g-")                 # and plot it in green

    rec1.move(2.0,1.0)              # move the rectangle by dx=2 dy=1
    rec1.draw("r-")                 # plot the translated rectangle in red

    rec2.draw_moved(-4,-2.5,"m:")   # plot the moved square in dotted magenta
    
    plt.axis('equal')
    plt.margins(0.1, 0.1)           
    plt.show()
