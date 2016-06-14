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
    sim.print_satisfactions()
    # year = 2016
    # while year < 2050:
    #     year += 1
    #     for agent in agents:
    #         if agent.update_interval_done():
    #             agent.migration_decision()