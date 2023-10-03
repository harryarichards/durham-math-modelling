import numpy as np
import matplotlib.pyplot as plt
import relax_jacobi_1d

class RelaxGaussSeidel1D(relax_jacobi_1d.RelaxJacobi1D):
  def relax_1_step(self, nu=0.9):
      """ Perform a single Gauss Seidel relaxation iteration 
         Return: the largest update

      :param nu : relaxation parameter
      """
     TO COMPLETE

     
# Tests follow; only run when not importing the module.

if __name__ == "__main__":
   class RelaxGSDiffusion(RelaxGaussSeidel1D):
      """ A class to relax to static solutions of the diffusion equation. """
      def F(self, v, i):
        return((v[i+1]+v[i-1]-2*v[i])/self.dx**2) 

      def boundary(self):
        self.v[0] = 1
        self.v[self.Np-1] = 0


   Np  = 100                # number of grid points to use
   v0  = np.zeros([Np])     # initial value : 0 everywhere
   rel = RelaxGSDiffusion(v0, xmin=0, xmax=10, Np=Np)
   n   =rel.relax(1e-5,0.9)   # relax until err < 1e-5
   print("No of iterations: ",n) 
   rel.plot()      
   plt.show()
