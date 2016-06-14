__author__ = 'laila'


import numpy
import numpy.random as random
import config
import json


living_place_per_province = json.load(open('data/parsed_living_places'))
salary_per_province = json.load(open('data/parsed_salaries'))
provinces = list(salary_per_province.keys())
population_per_province = {p: value['Total'] for (p, value) in living_place_per_province.items() if p in provinces}
unemployment_per_province = json.load(open('data/parsed_unemployment'))
housing_per_province = json.load(open('data/parsed_housing'))


class Agent:
    def __init__(self, province, living_place, salary, unemployment, housing, peers=[]):
        self.province = province
        self.peers = peers
        self.living_place = living_place
        self.salary = salary
        self.unemployment = unemployment
        self.housing = housing

    def __str__(self):
        return self.province + " " + self.living_place

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

    def satisfaction(self):
        socw = 0.5
        ecow = 1 - socw
        return socw*self.social_satisfaction() + ecow*self.economic_satisfaction()

    def social_satisfaction(self):
        peers_in_province = len([p for p in self.peers if p.living_place == self.living_place])
        if peers_in_province <= config.min_peers:
            return 0
        if peers_in_province >= config.max_peers:
            return 5
        return ((peers_in_province - config.min_peers) / (config.max_peers - config.min_peers)) * 5

    def economic_satisfaction(self):
        res = random.uniform(0, 0.5) if self.unemployment else random.uniform(0.5, 1)
        res += random.uniform(0, 0.5) if self.housing else random.uniform(0.5, 1)
        if self.salary <= config.min_salary:
            return res
        if self.salary >= config.max_salary:
            return res + 3
        return ((self.salary - config.min_salary) / (config.max_salary - config.min_salary)) * 5


def initialize_connections(agents):
    for v in agents.values():
        for a in v:
            number_of_peers = int(random.normal(config.peers_per_agent, 2))
            a.peers = random.choice(v, max(0, number_of_peers))


def initialize_population():
    agents = {}
    for p in provinces:
        agents[p] = []
        for i in range(int(numpy.ceil(population_per_province[p] / config.people_per_agent))):
            # a = define_age_group(p)
            # g = define_gender(p, gender_per_province)
            l = define_living_place(p)
            s = define_salary(p)
            u = define_unemployment(p)
            h = define_housing(p)
            agents[p].append(Agent(province=p, salary=s, living_place=l, unemployment=u, housing=h))

    initialize_connections(agents)
    return agents


def define_living_place(province):
    distribution = living_place_per_province[province]
    total = distribution['Total']
    probabilities = [distribution[x] / total for x in provinces]
    selection = random.multinomial(1, probabilities)
    for i in range(len(selection)):
        if selection[i]:
            return provinces[i]


def define_salary(province):
    return random.normal(salary_per_province[province], 100)


def define_unemployment(p):
    return random.uniform(0, 100) < unemployment_per_province[p]


def define_housing(p):
    return random.uniform(0, population_per_province[p]) < 2*housing_per_province[p]


# region Comments
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


# def import_data():
#     provinces = []
#     population_per_province = {}
#     gender_per_province = {}
#     f = open('population_per_province.txt')
#     p = f.readline().replace('\n','')
#     while p:
#         provinces.append(p)
#         population = int(f.readline().replace('\n','').replace(' ', ''))
#         population_per_province[p] = population
#         male = int(f.readline().replace('\n','').replace(' ', ''))
#         gender_per_province[p] = (population-male)/population
#         f.readline()
#         p = f.readline().replace('\n','')
#         print(p)
#     return provinces, population_per_province, gender_per_province

# age_group_per_province = {'La Habana': [12,8,13,7,10,11,9,10]}
# marital_status = {'La Habana': []}

#endregion


if __name__ == '__main__':
    pass
