import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data/hare_lynx_data.csv')

# To restrict to a subset of years, use e.g.
# data = data[data['Year']>=1919]  

plt.plot(data["Year"], data["Lynx"].values, 'ro-')
plt.plot(data["Year"], data["Hare"].values, 'bo-')
plt.legend(['Lynx', 'Hare'])
plt.show()

plt.plot(data["Hare"].values, data["Lynx"].values, 'bo');
plt.xlabel("hare")
plt.ylabel("lynx")
plt.show()
