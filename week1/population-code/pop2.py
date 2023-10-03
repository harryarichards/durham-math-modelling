import matplotlib.pyplot as plt

t_list = [] # list of t values
N_list = [] # list of N values
R = 3       # each couple of rabbits has 4 youngs on average
N = 2       # the initial population.

for t in range(51): # compute population for 50 years
  t_list.append(t)
  N_list.append(N)
  N = R*N           # population the next year

plt.plot(t_list, N_list, "b-") # plot the population
plt.show()                     # display the figure 
