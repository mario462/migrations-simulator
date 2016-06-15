__author__ = 'mario'

import initial_population
import config


class Simulation:
    def __init__(self):
        self.agents = []
        self.provinces = []
        self.initialize()
        self.reset_migrations()

    def initialize(self):
        self.provinces = initial_population.initialize_provinces()
        self.agents = initial_population.initialize_population()

    def simulate(self, sim_number=10):
        while sim_number > 0:
            sim_number -= 1
            self.reset_migrations()
            for p in self.agents:
                for a in self.agents[p]:
                    migrate, old, new = a.evolve()
                    if migrate:
                        self.migrations[old.name][new.name] += config.people_per_agent
            yield self.migrations

    def reset_migrations(self):
        dic = { x.name:0 for x in self.provinces }
        self.migrations = { y.name:dic.copy() for y in self.provinces }


if __name__ == '__main__':
    sim = Simulation()
    sim.initialize()
    result = sim.simulate()
    for r in result:
        print(r)
