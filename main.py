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
            print('Simulation ' + str(sim_number))
            sim_number -= 1
            self.reset_migrations()
            for p in self.agents:
                for a in self.agents[p]:
                    migrate, old, new, people = a.evolve()
                    if migrate:
                        self.migrations[old.name][new.name] += people
            self.population_per_province = {x: x.population for x in self.provinces}
            self.living_places_per_province = {x: x.living_places for x in self.provinces}
            yield self.population_per_province, self.migrations, self.living_places_per_province

    def reset_migrations(self):
        dic = {x.name: 0 for x in self.provinces}
        self.migrations = {y.name: dic.copy() for y in self.provinces}

    def population_per_province(self):
        return self.population_per_province


if __name__ == '__main__':
    import time
    start = time.time()
    sim = Simulation()
    result = sim.simulate(sim_number=1)
    next(result)
    end = time.time()
    print(end-start)
    print('Simulation ended')
