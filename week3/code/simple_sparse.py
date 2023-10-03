import numpy as np
import scipy.sparse
import scipy.sparse.linalg
  
Ne=100                                              # number of equations
Q=scipy.sparse.lil_matrix((Ne,Ne),dtype=np.float64) # create sparse matrix
for i in range(Ne):                                 # populate Q
   Q[i,i] = -2
   if (i > 0) :
       Q[i,i-1] = 1.
       Q[i-1,i] = 1.
   Q[Ne-1,Ne-1] += 1.

F = np.zeros(Ne)                                   # create F
F[0] = -1                                          # V0=1 nonzero element
W = scipy.sparse.linalg.spsolve(Q.tocsc(), F)      # solve

print(W)
