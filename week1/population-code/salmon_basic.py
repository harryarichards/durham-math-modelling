import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('data/LakeTroutMI.csv')

filtered = data[data['area'] == 'MI5'].sort_values(by='stocked')

recruits = filtered['recruits'].values
stocked  = filtered['stocked'].values

plt.plot(stocked, recruits, 'o')
plt.xlabel('stock')
plt.ylabel('recruits')
plt.show()


