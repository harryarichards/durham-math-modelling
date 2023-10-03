import ode_rk4
import numpy as np
import matplotlib.pyplot as plt

class TestRK4(ode_rk4.ODE_RK4):
  """A class derived from the class Ode_rk4.
  """
  def __init__(self, V0=[], dt=0.1, t0=0, a=1):
      """Set the ODE parameters
      : param V0 : initial value of V 
      : param t0 : initial time (usualy 0)
      : param dt : integration time step
      : param a  : equation parameter
      """  
      super().__init__(V0,dt,t0) # we can miss this out
      self.a=a

  def F(self, t, v):
      """ equation to solve: 
          df/dt = a g  
          dg/dt =-a f
          v[0] is f  and v[1] is g
      : param t : current time 
      : param v : current function as a vector 
      """
      eq1 = self.a*v[1]
      eq2 = -self.a*v[0]
      return(np.array([eq1,eq2]))


