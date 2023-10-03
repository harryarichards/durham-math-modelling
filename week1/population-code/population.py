import matplotlib.pyplot as plt
import numpy as np

class Population:
  """ A class to compute the time evolution of a population. """
  
  def __init__(self, R=0):
    self.R = R  # growth rate
    self.N = 0  # current population
    
  def F(self):
    """ Return the population at the next time. """
    return self.R*self.N
  
  def iterate(self, N0, n1, n2):
    """ Iterate the logistic equation starting at N0 for n1+n2 steps.
    Return the last n2 values of N in a list.
    
    :param N0:    initial population.
    :param n1:    number of iterations to ignore.
    :param n2:    number of iterations to store.
    :return:      the n2 values of N as a list.
    """
    
    N_list = []  # list of populations
    self.N = N0
    for i in range(n1+n2):
      if i>=n1:
        N_list.append(self.N)
      self.N = self.F()

    return N_list
    
  def bifurcation_plot(self, Rmin, Rmax, NR, N0):
    """ Display the bifurcation plot.

    :param Rmin: starting value of growth rate.
    :param Rmax: ending value of growth rate.
    :param NR:   number of steps along R axis.
    :param N0:   initial population.
    """
    
    for R in np.linspace(Rmin, Rmax, NR):
      self.R = R
      N_list = self.iterate(N0, 500, 1500)
      R_list = np.ones(len(N_list))*R
      plt.plot(R_list, N_list, "b.", markersize=1)
    plt.xlabel('$R$')
    plt.ylabel('asymptotic $N$')
    plt.show()

  def transfer_plot(self):
    """ Display the transfer plot of the population. """
    
    for self.N in np.linspace(0, 1, 200):
      plt.plot(self.N, self.F(), "b.")
    plt.xlabel('$N_t$')
    plt.ylabel('$N_{t+1}$')
    plt.show()


# Only run this when not importing the module.

if __name__ == "__main__":
  pop = Population(R=1.5)
  pop.transfer_plot()
  pop.bifurcation_plot(0.2, 1.01, 10, 0.1)


