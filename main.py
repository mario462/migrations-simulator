__author__ = 'mario'

import initial_population


class Simulation:
    def __init__(self):
        self.agents = []

    def initialize(self):
        initial_population.initialize_provinces()
        self.agents = initial_population.initialize_population()

    def simulate(self):
        for a in self.agents:
            a.evolve()

if __name__ == '__main__':
    sim = Simulation()
    sim.initialize()
    sim.simulate()