import numpy as np
import traffic_ode_base
import matplotlib.pyplot as plt


class TrafficODE(traffic_ode_base.TrafficODEBase):
    def vgoal(self, dx):
        """
        Calculate the goal velocity.

        :param dx:    headway.
        """
        #Calculate the goal velocity.
        vgoal = self.v0*(np.tanh(self.m*(dx-self.bf))-np.tanh(self.m*(self.bc-self.bf)))
        # Return the goal velocity
        return vgoal


    def plot_free_flow_density(self):
        """
        Crate plot of free-flow against density
        """
        # Create an empty list for flow and density.
        densities, flows = [], []
        # Sets car_length to 5
        l_c = 5
        # Iterates through numbers 1 to the maximum number of cars which is road length divided by car length.
        for i in range(1, int(self.road_length//(l_c))+1):
            # Calculate the flow for i cars in number of cars per minute
            q = (self.vgoal((self.road_length/i)))*(i/self.road_length) * 60
            # Append the flow (in cars per minute) to the list.
            flows.append(q)
            # Append the density to the list (in cars per km).
            densities.append((i/self.road_length)*1000)
        # Plot flow against density in red.
        plt.plot(densities, flows, 'r')
        # Set the x label to density with unit cars per km.
        plt.xlabel('Density (cars/km)')
        # Set the x label to density with unit cars per km.
        plt.ylabel('Flow (cars/min)')
        # Set the title to free-flow vs density.
        plt.title("Free-flow vs Density")


    def update(self):
        """
        Calculate the headway for all cars.
        Calculate acceleration for all cars
        """
        # Calculate the headway between each car.
        h = np.mod(np.roll(self.x, -1) - self.x, self.road_length)
        # Calculate acceleration.
        a = self.s * (self.vgoal(h) - self.v)
        #Update the position of each car.
        self.x = self.x + self.v * self.dt + 0.5*a*(self.dt**2)
        # Update the speed of each car.
        self.v = self.v + a*self.dt
        # Update the detector, by adding the number of cars with position greater than the length of the road.
        # This accounts for any cars that have drove past the detector.
        self.detector += len(np.where(self.x >= self.road_length)[0])
        # Return any cars that pass the end of the road to the start of the road.
        self.x = np.remainder(self.x, self.road_length)


if __name__ == "__main__":
    tr = TrafficODE(100, s=1, m=1, bc=0, bf=2, vmax=1.964, road_length=200)
    tr.setup_cars(random=True)
    tr.simulate(50, plot=True)
