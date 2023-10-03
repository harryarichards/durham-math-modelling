import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
from scipy.sparse import lil_matrix
import scipy.sparse.linalg


class RabbitsMatrix:

  def __init__(self):
    self.Ne = 1              # Number of grid points
    self.dx = 0.0            # Distance between grid points
    self.v = np.array([0.0]) # The functions for the equations
    self.Q = []
    
  def reset(self, V0, xmax, Ne, YH, Yn, lambdaY, K=1, D=1, V=0):
    """ Set the initial parameters. """
    self.Ne = Ne
    self.xmin = 0
    self.xmax = xmax
    self.V0 = V0
    self.YH=YH
    self.Yn=Yn
    self.lambdaY=lambdaY
    self.K=K
    self.D=D
    self.dx = (xmax-xmin)/(self.Ne+1)
    self.l_x = np.linspace(xmin,xmax,self.Ne+2)
    
  def Y(self,x):
    TO DO

  def Qmat(self):
    """ Create the Q matrix for the equation."""
    TO DO
    
  def Fmat(self):
    """ Create the F vector for the equation. """
    
  def solve_matrix(self):
    """ Solve the equation Q V = F. """
    print("Solving system...")
    self.V = scipy.sparse.linalg.spsolve(self.Q.tocsc(), self.F)
    
  def plot(self,format="k-"):
    """ plot v(x)
    """
    TO DO

if __name__ == "__main__":
   rabbm = RabbitsMatrix() # create the relaxation object
   rabbm.reset(V0=0.001, xmax=1000, Ne=100, YH=0.0005, \
               Yn=0.001, lambdaY=100, K=0.001, D=1)
   rabbm.Qmat()
   rabbm.Fmat()
   rabbm.solve_matrix()
   print("V[xmax]=",rabbm.V[rabbm.Ne-1])
   rabbm.plot()
   
