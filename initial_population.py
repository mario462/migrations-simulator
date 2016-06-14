__author__ = 'laila'


import numpy.random as random
from . import config
import json


def import_data():
    provinces = []
    population_per_province = {}
    gender_per_province = {}
    f = open('population_per_province.txt')
    p = f.readline().replace('\n','')
    while p:
        provinces.append(p)
        population = int(f.readline().replace('\n','').replace(' ', ''))
        population_per_province[p] = population
        male = int(f.readline().replace('\n','').replace(' ', ''))
        gender_per_province[p] = (population-male)/population
        f.readline()
        p = f.readline().replace('\n','')
        print(p)
    return provinces, population_per_province, gender_per_province

# age_group_per_province = {'La Habana': [12,8,13,7,10,11,9,10]}
# marital_status = {'La Habana': []}
living_place_per_province = json.load(open('parsed_migrations'))
salary_per_province = json.load(open('parsed_salaries'))


class Agent:
    def __init__(self, province, living_place, salary, peers=[]):
        # self.age_group = age_group
        # self.gender = gender
        self.province = province
        self.peers = peers
        self.living_place = living_place
        # self.marital_status = marital_status

    def __str__(self):
        return self.province + " " + str(self.age_group) + " " + self.gender + " " + self.living_place

    def migration_decision(self):
        if random.random() > 0.5:
            p = self.choose_migration_province()
            self.migrate(p)
            return True
        return False

    def update_interval_done(self):
        return False

    def migrate(self, province):
        self.living_place = province

    def choose_migration_province(self):
        return 'La Habana'


def initialize_connections(agents):
    for i in range(len(agents)):
        number_of_peers = random.uniform(config.peers_per_agent, 3)
        agents[i].append(random.choice(agents, number_of_peers))


def initialize_population():
    provinces, population_per_province, gender_per_province = import_data()
    agents = {}
    for p in provinces:
        agents[p] = []
        for i in range(population_per_province[p] / config.people_per_agent):
            # a = define_age_group(p)
            # g = define_gender(p, gender_per_province)
            l = define_living_place(p.capitalize())
            s = salary_per_province(p)
            agents[p].append(Agent(province=p, salary=s, living_place=l))

    initialize_connections(agents)
    return agents


def define_living_place(province):
    distribution = living_place_per_province[province]
    r = random.uniform(0, sum(distribution.values))
    total = 0
    for p in distribution:
        total += int(distribution[p])
        if r <= total:
            return p


def define_salary(province):
    return random.normal(salary_per_province[province], 80)


def simulate(years):
    agents = initialize_population()
    while years > 0:
        for a in agents:
            if a.update_interval_done():
                a.migration_decision()
        years -= 1


# def define_gender(province, gender_per_province):
#     women_percent = gender_per_province[province]
#     r = random.uniform(0, 100)
#     return 'female' if r < women_percent else 'male'


# def define_age_group(province):
#     r = random.uniform(0, 100)
#     sum = 0
#     j = 0
#     for i in age_group_per_province[province]:
#         sum += i
#         j += 1
#         if r <= sum:
#             return j*10