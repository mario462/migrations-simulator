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
        self.population_per_province = {x.name: x.population for x in self.provinces}

    def simulate(self, sim_number=10):
        while sim_number > 0:
            print('Simulation ' + str(sim_number))
            sim_number -= 1
            self.reset_migrations()
            for p in self.agents:
                for a in self.agents[p]:
                    migrate, old, new, people = a.evolve()
                    if migrate:
                         self.migrations[old.name][new.name] += int(people)
            self.population_per_province = {x.name: x.population for x in self.provinces}
            self.living_places_per_province = {x.name: x.living_places for x in self.provinces}
            config.migration_threshold -= config.migration_threshold*0.1
            yield self.population_per_province, self.migrations, self.living_places_per_province

    def reset_migrations(self):
        dic = {x.name: 0 for x in self.provinces}
        self.migrations = {y.name: dic.copy() for y in self.provinces}

    def population(self):
        return self.population_per_province

    def change_salary(self, province, percent):
        applied = percent / 100
        province.salary *= applied

    def change_housing(self, province, percent):
        applied = percent / 100
        province.housing = int(province.housing, applied)



if __name__ == '__main__':
    import time
    p = initial_population.initialize_provinces()
    a = initial_population.Agent(p[0])
    a.peers.append(initial_population.Agent(p[0]))
    a.peers.append(initial_population.Agent(p[0]))
    a.peers.append(initial_population.Agent(p[0]))
    a.peers.append(initial_population.Agent(p[0]))
    a.peers.append(initial_population.Agent(p[0]))
    a.peers.append(initial_population.Agent(p[0]))

    ag = initial_population.Agent(p[0])
    ag.living_place = p[1]
    a.peers.append(ag)

    print(a.province.name)
    print(a.economical_satisfaction())
    print(a.social_satisfaction())
    print(a.environmental_satisfaction())

    for i in range(1,len(p)):
        print(p[i].name)
        print(a.hypothetical_economical_satisfaction(p[i]))
        print(a.hypothetical_social_satisfaction(p[i]))
        print(a.hypothetical_environmental_satisfaction(p[i]))

    # start = time.time()
    # sim = Simulation()
    # result = sim.simulate(sim_number=1)
    # for r in result:
    #     print(r)
    # end = time.time()
    # print(end-start)
    # print('Simulation ended')


