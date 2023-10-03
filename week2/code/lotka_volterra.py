import matplotlib.pyplot as plt
from ode_euler_N import ODE_Euler_N


class Lotka_Volterra(ODE_Euler_N):
    def set_K(self, K):
        """
        :param K:  Lotka-Volterra model parameter
        """
        self.K = self.d/self.a

    def F(self, V):
        N = V[0]
        P = V[1]
        ### TO DO


# Only run this when not importing the module.

if __name__ == "__main__":
    lv = Lotka_Volterra()
    lv.set_K(1)
    lv.reset(V0=[0.1, 0.1], dt=0.001)
    lv.iterate(40, 0.01)
    lv.plot(1, 0, "r-")
    lv.plot(2, 0, "b-")
    plt.legend(['Preys', 'Predators'])
    plt.show()
    lv.plot(1, 2, "g-")
    plt.axis('equal')
    plt.margins(0.1, 0.1)
    plt.xlabel('Preys')
    plt.ylabel('Predators')
    plt.show()
