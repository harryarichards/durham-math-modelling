from ode_euler import ODE_Euler
import math

class Schaefer(ODE_Euler):
    def set_V(self, V):
        self.V = V

    def set_Y(self, Y):
        self.Y = Y*(1- math.cos(2*math.pi*self.V*self.t))

    def F(self, t, N):
        return (N*(1-N)-self.Y)

if __name__ == "__main__":
    pop = Schaefer(N =0.25, dt = 0.01, t0 = 0)  # R takes the default value: -1
    pop.set_V(1)
    pop.set_Y(0)  # we change the value of R
    pop.iterate(20)  # we perform 10 steps of integration
    pop.plot()  # and display the result