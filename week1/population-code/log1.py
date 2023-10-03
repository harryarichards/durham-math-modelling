import matplotlib.pyplot as plt

t_list = [] # list of t values
N_list = [] # list of N values
R = 3.9       # each couple of rabbits has 4 youngs on average
N = 0.5     # the initial population.

for t in range(101): # compute population for 50 years
  t_list.append(t)
  N_list.append(N)
  N = R*N*(1-N)           # population the next year

plt.plot(t_list, N_list, "b.") # plot the population
plt.savefig("log.pdf")
plt.show()                     # diplay the figure