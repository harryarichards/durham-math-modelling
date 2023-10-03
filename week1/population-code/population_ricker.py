from population import Population
import math



class PopulationRicker(Population):
    """ A class to compute the time evoluation of a logistic population. """

    def __init__(self,Q=0):
        super().__init__()
        self.Q = Q

    # The only function we need to describe a population.
    def F(self):
        return ((self.N * math.exp(self.R*(1 - self.N))) + self.Q)


# Only run this when not importing the module
if __name__ == "__main__":
    pop = PopulationRicker(0.06)
    print(pop.R)
    pop.transfer_plot()
    pop.bifurcation_plot(0.2, 4, 500, 0.1)

