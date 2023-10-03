import numpy as np
import matplotlib.pyplot as plt
import relax_GS_1d

class RelaxRabbits(relax_GS_1d.RelaxGaussSeidel1D):
  def __init__(self, v0, xmax, Np, YH, Yn, lambdaY, Rmin, Rmax, K=1, D=1, V=0):
      """ Set the initial parameters

      :param v0  : initial condition
      :param xmax: upper domain boundary
      :param Np  : number of points 
      :param YH, Yn, lambdaY: Hunting rate parameters
      :param Rmin, Rmax     : rabbit population threshold parameters 
      :param K   : rabbit birth rate 
      :param D   : rabbit diffusion 
      :param V   : rabbit drifting speed
      """
      self.reset(v0, xmax, Np, YH, Yn, lambdaY, Rmin, Rmax, K, D, V)

  def reset(self, v0, xmax, Np, YH, Yn, lambdaY, Rmin, Rmax, K=1, D=1, V=0):
      """ Set the initial parameters. See __init__ for more info."""
      super().reset(v0, 0, xmax, Np)
      self.YH=YH
      self.Yn=Yn
      self.lambdaY=lambdaY
      self.Rmin=Rmin
      self.Rmax=Rmax
      self.K=K
      self.D=D
      self.V=V
     
  def Y(self,x):
      TO DO
    
  def R(self,x):
      TO DO
    
  def F(self,v,i):
      """ 
      Describes the model of rabbits on a hill slope.

      :param v : current function value (a vector).
      :param i : index of array element.
      """
      x = self.xmin+i*self.dx 
      dv = TO DO
      return(dv/self.D) 

  def boundary(self):
      """ Set the bounary condition: dN/dx = 0 at the top/bottom. """
      self.v[0] = self.v[1]
      self.v[self.Np-1] = self.v[self.Np-2];


# Tests follow; only run when not importing the module.

if __name__ == "__main__":
   Np = 100                # number of points to use
   rel = RelaxRabbits(v0=np.ones([Np]), xmax=1000, Np=Np, YH=0.05, \
                      Yn=0.005, lambdaY=100, Rmin=0.001, Rmax=1, \
                      K=0.1, D=1, V=0)
   
   n=rel.relax(1e-6,0.2)   # relax until err < 1e-5
   print("No of iterations: ",n) 
   rel.plot()
   plt.savefig("relax_rabbit.pdf")
   plt.show()
