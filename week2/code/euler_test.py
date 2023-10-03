from ode_euler import ODE_Euler

class EulerTest(ODE_Euler):
    
    def __init__(self, N, t0, dt, R=-1):
        """ Initialiser: set all the parameter for the integration
        : param N  : initial value of N 
        : param t0 : initial time (usualy 0)
        : param dt : integration time step
        : param R  : equation parameter value (default is -1)
        """
        super().__init__(N, t0, dt)
        self.R = R
          
    def set_R(self, R):
        """ Set the equation parameter value
        """
        self.R = R

    def F(self, t, N):
        """ The right hand side of the equation dN/dt = R*N
        : param t : current value of integration variable t
        : param N : current value of function N
        """
        return self.R*N

if __name__ == "__main__":
    pop = EulerTest(0.01, 0, 0.01) # R takes the default value: -1
    pop.set_R(-0.5) # we change the value of R
    pop.iterate(10) # we perform 10 steps of integration
    pop.plot()      # and display the result

    # Another way to do the same
    pop2 = EulerTest(0.01, 0, 0.01,-0.5) # Set R value using __init__
    pop2.iterate(10) # we perform 10 steps of integration
    pop2.plot("r-")  # and display the result in red this time
    
