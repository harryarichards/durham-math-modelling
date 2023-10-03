import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
from scipy.sparse import lil_matrix
import scipy.sparse.linalg


class DiffusionMatrix:
  
  def __init__(self):
    self.Ne  = 1             # Number of equations
    self.dx = 0.0            # Distance between grid points
    self.v = np.array([0.0]) # The functions for the equations
    self.Q = []
    
  def reset(self, Ne, xmin, xmax, V0):
    """ Set the initial parameters
    xmax : upper domain boundary (xmin=0)
    Ne : number of grid points 
    V0 : value of V at x=0 (boundary condition)
    """
    self.Ne = Ne
    self.xmin = xmin
    self.xmax = xmax
    self.V0 = V0
    self.dx = (xmax-xmin)/(self.Ne+1)
    self.l_x = np.linspace(xmin,xmax,self.Ne+2)
    
  def Qmat(self):
    """ Create the Q matrix for the equation. """
    self.Q = lil_matrix((self.Ne, self.Ne), dtype=np.float64)
    for i in range(self.Ne):
      self.Q[i,i] = -2.
      if (i > 0) :
        self.Q[i,i-1] = 1.
        self.Q[i-1,i] = 1.
    #print("Q=\n",self.Q.toarray())
 
  def Fmat(self):
    """ Create the F vector for the equation. """
    self.F = np.zeros(self.Ne)
    self.F[0] = -self.V0  # boundary at xmin : V[0] = V0
    self.F[self.Ne-1] = 0  # boundary at xmax : V[xmax] = 0
    #print("F=",self.F)
      
  def solve_matrix(self):
    """ Solve the equation Q V = F. """
    print("Solving system...")
    self.V = scipy.sparse.linalg.spsolve(self.Q.tocsc(), self.F)
    #print("V=",self.V)

  def plot(self, style="k-"):
    """ Plot v(x). """
    V = np.zeros(self.Ne+2)
    V[1:self.Ne+1] = self.V # boundary at xmin
    V[0] = self.V0
    V[self.Ne+1] = 0        # boundary at xmax
    print("Full V=", V)
    #plt.plot(self.l_x, V, style)
    plt.show()
    
if __name__ == "__main__":
  diffm = DiffusionMatrix() 
  diffm.reset(Ne=4, xmin=0, xmax=10, V0=1)
  diffm.Qmat()
  diffm.Fmat()
  diffm.solve_matrix()
  diffm.plot()
  
