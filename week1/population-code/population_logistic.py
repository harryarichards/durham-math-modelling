from population import Population

class PopulationLogistic(Population):
  """ A class to compute the time evoluation of a logistic population. """

  # The only function we need to describe a population.
  def F(self):
      return(self.R*self.N*(1-self.N))
       

# Only run this when not importing the module
if __name__ == "__main__":
  pop = PopulationLogistic(2.5)
  print(pop.R)
  pop.transfer_plot()
  pop.bifurcation_plot(0.2, 4, 500, 0.1)


