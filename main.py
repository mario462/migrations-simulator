__author__ = 'mario'

import initial_population
import config


class Simulation:
    def __init__(self):
        self.agents = []
        self.provinces = []
        self.initialize()
        dic = { x:0 for x in self.provinces }
        self.migrations = { y:dic.copy() for y in self.provinces }

    def initialize(self):
        self.provinces = initial_population.initialize_provinces()
        self.agents = initial_population.initialize_population()

    def simulate(self):
        self.reset_migrations()
        for a in self.agents:
            migrate, old, new = a.evolve()
            if migrate:
                self.migrations[old][new] += config.people_per_agent
        yield self.migrations

    def reset_migrations(self):
        self.migrations.values().va


if __name__ == '__main__':
    sim = Simulation()
    sim.initialize()
    sim.simulate()
