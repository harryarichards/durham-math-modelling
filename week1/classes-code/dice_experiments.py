from dice import *
import matplotlib.pyplot as plt

dice = Dice()
for i in xrange(1000):
    dice.roll_once()

plt.hist(dice.rolls,6,range=(0.5,6.5))
plt.show()
