import matplotlib.pyplot as plt
import numpy as np

def iterate(N0, R, n1, n2):
    N_list = []
    N = N0
    for i in range(n1 + 1):  # compute population for n1 + n2 years
        N = R * N * (1 - N)
    for i in range(n2 + 1):
        N = R * N * (1 - N)
        N_list.append(N)
    return N_list

for R in np.linspace(0.2, 4, 500):
    N_list = iterate(0.5, R, 500, 1500)
    R_list = np.ones(len(N_list))*R
    plt.plot (R_list, N_list, "b.", markersize = 1)
plt.savefig("bifurcation_plot.pdf")
plt.show()