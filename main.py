__author__ = 'mario'

import initial_population
import config


class Simulation:
    def __init__(self):
        self.agents = []
        self.provinces = []
        self.migrations = []
        self.population_per_province = []
        self.living_places_per_province = []
        self.initialize()
        self.reset_migrations()

    def initialize(self):
        self.provinces = initial_population.initialize_provinces()
        self.agents = initial_population.initialize_population()
        self.population_per_province = {x: x.population for x in self.provinces}

    def simulate(self, sim_number=10):
        while sim_number > 0:
            sim_number -= 1
            self.reset_migrations()
            for p in self.agents:
                for a in self.agents[p]:
                    migrate, old, new = a.evolve()
                    if migrate:
                        self.migrations[old.name][new.name] += config.people_per_agent
            self.population_per_province = {x: x.population for x in self.provinces}
            self.living_places_per_province = {x: x.living_places for x in self.provinces}
            yield self.population_per_province, self.migrations, self.living_places_per_province

    def reset_migrations(self):
        dic = {x.name: 0 for x in self.provinces}
        self.migrations = {y.name: dic.copy() for y in self.provinces}

    def population_per_province(self):
        return self.population_per_province


if __name__ == '__main__':
    sim = Simulation()
    sim.initialize()
    result = sim.simulate()
    for r in result:
        print(r)
