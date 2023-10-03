# Import additional modules.
import numpy as np

class Dice:
    # Global variables
    rolls = []

    # Roll the dice once and store the results.
    def roll_once(self):
        result = np.random.randint(1,7)
        self.rolls.append(result)

    def average(self):
        avg = sum(rolls,0.0)/len(rolls)
        return avg


# Unit tests, which each test one isolated bit of functionality.
def test1():
    dice = Dice()
    for i in xrange(10000):
        dice.roll_once()
    assert(min(dice.rolls)>=1)
    assert(max(dice.rolls)<=6)

# Run the unit tests.
if __name__=="__main__":
    test1()

