import numpy as np
import traffic_discrete_base

class TrafficDiscrete(traffic_discrete_base.TrafficDiscreteBase):
    def step(self):
        """
        Perform one update cycle of the system using the rules highlighted below:

        1. Each car accelerates by 1 providing it has not reached the maximal legal speed.
        2. If a car is getting too close to the next car, it decelerates.
        3. Each car slows down randomly, with probability p_slowdown
        4. The car moves the number of positions defined by the velocity.

        It also updates the car counter in self.detector when a car moves past the detector at the 'end' of the road.
        """
        # Determines all the road positions where a car exists
        cars = np.where(self.v != -1)[0]
        # Determines the distance between the car and the car in front
        headway = np.mod(np.roll(cars,-1)-cars, len(self.v))
        # Generates an array of each of the cars velocities
        velocities = np.array(self.v[cars])
        # This sets each velocity to the minimum of itself or vmax (the maximum legal speed).
        # This increases each velocity by 1 unless this exceeds the maximum legal speed.
        velocities = np.minimum(velocities + 1, self.vmax)
        # This sets each velocity to the minimum of itself or the headway - 1.
        # This aids in ensuring the car never hits the car infront.
        velocities = np.minimum(velocities, headway-1)
        # Generate an array with a random number 0-1 for each segment.
        rnd = np.random.rand(len(velocities))
        # Generates an array of truth values dependent.
        # Each element in the array is:
        # True if the random number is less than the probability of slowing down that was passed into the function,
        # set to False otherwise.
        rnd_tf = rnd < self.p_slowdown
        # Set choices equal to 0 or -1.
        # 0 if the element in rnd_tf is false, -1 if it is true.
        choices = np.choose(rnd_tf, [0, -1])
        # This sets each velocity to the maximum of 0 and the velocity plus the choices variable.
        # This equates to subtracting 1 from each of the elements where the random number
        # was less than probability of slowing down that was passed into the function.
        # However making sure the velocity does not go less than 0.
        velocities = np.maximum(velocities+choices, 0)
        # For each position of the car add the new velocity to the position,
        # as this corresponds to the new position of cars.
        cars = cars + velocities
        # Update the detector, by adding the number of cars with position greater than the length of the road.
        # This accounts for any cars that have drove past the detector.
        self.detector += len(np.where(cars >= self.road_len)[0])
        # Put any cars that have drove past the end of the road back at the beginning mimicking a circular road).
        cars = np.remainder(cars, self.road_len)
        # Fill an array with -1s, which models an empty road.
        new_v = -np.ones(self.road_len)
        # This places the velocities we calculated in the new road.
        np.put(new_v, cars.astype(int), velocities)
        # Set v equal to the updated road.
        self.v = new_v

    def flow_density(self, density, steps):
        """
        Calculates the flow.

        :param density:    traffic density.
        :param steps:      number of steps to iterate.
        :return:           tuple of (density, flow).
        """
        # Set density to be as in the parameter
        self.density = density
        # Fill the road randomly based on the density set above.
        self.fill_road_randomly(self)
        # Set the the detector to 0.
        self.detector = 0
        # Evolve the system for  steps//10 steps - this will aid the system in settling down.
        self.evolve(steps//10, False)
        # Set the the detector to 0.
        self.detector = 0
        # Evolve the system for the number of steps provided as a parameter.
        self.evolve(steps, False)
        # Calculates flow.
        flow = self.detector / steps
        # Returns a tuple of density and flow.
        return (self.density, flow)

if __name__=="__main__":
    # Totally deterministic behaviour (which reduces the model to
    # something known as 'Rule 184').
    tr=TrafficDiscrete(density=0.5, p_slowdown=0, vmax=1)
    tr.evolve(200)
    tr.make_plot()
    # More complicated case with random behaviour.
    tr=TrafficDiscrete(density=0.2, p_slowdown=0.2, vmax=4)
    tr.evolve(200)
    tr.make_plot()