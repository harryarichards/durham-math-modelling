import numpy as np
import matplotlib.pyplot as plt

class RelaxJacobi1D:
  """ A class to solve F(v)=0, where F is a differential
      operator acting on the vector 'v', using Jacobi relaxation."""

  def __init__(self, v0, xmin, xmax, Np):
    """
    :param v0         : initial condition
    :param xmin, xmax : domain boundaries
    :param Np         : number of points 
    """
    self.reset(v0, xmin, xmax, Np)
    

  def reset(self, v0, xmin, xmax, Np):
    """ Set the initial parameters.
    
    :param v0         : initial condition
    :param xmin, xmax : domain boundaries
    :param Np         : number of points 
    """
    self.Np = Np
    self.xmin = xmin        
    self.xmax = xmax
    self.dx = (xmax-xmin)/(Np-1)
    self.n = 0 # time iteration number
    self.v = np.array(v0, dtype='float64') # ensure we use floats!
    self.l_x = []  # list of t values for figures
    self.l_f = []  # list of f values (arrays) for figures
    self.boundary() # make sure the boundary condition is set
    
  def F(self, v, i):
    """ Returns update for v at position i. To be implemented in subclass.
    
    :param v : current function value (a vector).
    :param i : spatial index.
    :return  : update for v at position i.
    """
    pass

  def boundary(self):
    """ Enforce the boundary conditions. To be implemented in subclass."""
    pass
    
  def relax_1_step(self, nu=0.5):
    """ Perform a single Jacobi relaxation iteration.
    
    :param nu : relaxation parameter.
    :return   : the largest update.
    """
    w = np.array(self.v)
    dvmax = 0
    for i in range(1, self.Np-1):
      dv = nu*self.dx**2*self.F(self.v, i)
      if(np.fabs(dv) > dvmax) : dvmax = np.fabs(dv)
      w[i] = self.v[i] + dv
      
    self.v = w
    return(dvmax)
    
  def relax(self, err, nu=0.5):
    """ Relax until largest update is smaller than err.
    
    :param err : target "error".
    :param nu  : relaxation parameter.
    :return    : number of iterations required.
    """
    e = 1e64  # absurdly large
    n = 1
    while(e > err):
      e = self.relax_1_step(nu)
      self.boundary()
      n += 1
      if(n % 1000==0): print("n=",n)
      
    # set plot data
    self.l_x = np.linspace(self.xmin,self.xmax,self.Np)   
    self.l_f = np.array(self.v)
    return(n)
   
  def plot(self, style="k-"):
    """ Plot the vector 'v'.

    :param style: format for the plot function.
    """
    plt.plot(self.l_x, self.l_f, style);


# Tests follow; only run when not importing the module.

if __name__ == "__main__":

  class RelaxDiffusion(RelaxJacobi1D):
    """ A class to relax to static solutions of the diffusion equation. """
    def F(self, v, i):
      return((v[i+1]+v[i-1]-2*v[i])/self.dx**2) 

    def boundary(self):
      self.v[0] = 1
      self.v[self.Np-1] = 0;
      
    
  Np=200
  relax = RelaxDiffusion(np.zeros([Np]), xmin=0, xmax=10, Np=Np)
  n = relax.relax(1e-5)
  print("No of iterations: ",n) 
  relax.plot()             
  plt.show()
