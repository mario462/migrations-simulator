__author__ = 'mario'

import initial_population
import config
import numpy.random as random

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
        if province.salary > config.max_salary:
            config.max_salary = (config.max_salary+province.salary)/2

    def change_housing(self, province, percent):
        applied = percent / 100
        province.housing = int(province.housing * applied)

    def change_unemployment(self, province, percent):
        applied = percent / 100
        province.unemployment = int(province.unemployment * applied)

    def change_population(self, province, percent):
        change = int(province.population * (percent / 100))
        change = province.population - change
        if change > 0:
            for i in range(int(change / config.people_per_agent)):
                self.add_agent(province)
        else:
            change *= (-1)
            change = int(change / config.people_per_agent)
            self.kill_agents(province, change)

    def kill_agents(self, province, count):
        tokill = []
        for v in self.agents.values():
            for a in v:
                if a.living_place == province:
                    tokill.append(a)
        pos = random.randint(0, len(tokill), count)
        for v in self.agents.values():
            for a in v:
                for p in pos:
                    agent = tokill[p]
                    if agent in a.peers:
                        a.peers.remove(agent)
                    tokill[p].province.living_places[province.name].population -= config.people_per_agent
                    del(tokill[p])

        province.population = province.population - count * config.people_per_agent

    def add_agent(self, province):
        agent = initial_population.Agent(province=province)
        province_agents = self.agents[province.name]
        province_agents.append(agent)
        for a in self.agents[province.name]:
            number_of_peers = max(int(random.normal(config.peers_per_agent, 2)), 1)
            randoms = random.randint(0, len(province_agents), number_of_peers)
            for r in randoms:
                a.peers.append(province_agents[r])
                if random.random() > 0.7:
                    province_agents[r].peers.append(agent)
        province.population += config.people_per_agent


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


