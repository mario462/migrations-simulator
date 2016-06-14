__author__ = 'laila'

import numpy
import numpy.random as random
import config
import json


provinces = []
province_names = []
cuban_density = 101.6


class Agent:
    def __init__(self, sociability, province, living_place, salary, unemployment, housing, peers=[]):
        self.sociability = sociability
        self.province = province
        self.peers = peers
        self.living_place = living_place
        self.salary = salary
        self.unemployment = unemployment
        self.housing = housing
        self.update_ratio = 0.9
        self.satisfaction = -1

    def __str__(self):
        return self.province + " " + self.living_place

    def migration_decision(self):
        if random.random() > 0.5:
            p = self.choose_migration_province()
            self.migrate(p)
            return True
        return False

    def migrate(self, province):
        self.living_place = province

    def choose_migration_province(self):
        return 'La Habana'

    def update_needed(self):
        return random.uniform() < self.update_ratio

    def update_satisfaction(self):
        social_weight = 0.4
        economical_weight = 0.4
        environmental_weight = 1 - social_weight - economical_weight

        self.update_ratio = (social_weight * (5 - self.social_satisfaction()) \
                             + economical_weight * (5 - self.economical_satisfaction()) \
                             + environmental_weight * (5 - self.environmental_satisfaction())) / 5
        if self.update_ratio <= 0.1:
            self.update_ratio = 0.1
        elif self.update_ratio >= 0.9:
            self.update_ratio = 1

        self.satisfaction = social_weight * self.social_satisfaction() \
                            + economical_weight * self.economical_satisfaction() \
                            + environmental_weight * self.environmental_satisfaction()

        return self.satisfaction

    def social_satisfaction(self):
        peers_in_province = len([p for p in self.peers if p.living_place == self.living_place])
        if peers_in_province <= config.min_peers:
            return 0
        if peers_in_province >= config.max_peers:
            return 5
        return ((peers_in_province - config.min_peers) / (config.max_peers - config.min_peers)) * 5

    def economical_satisfaction(self):
        res = random.uniform(0, 0.5) if self.unemployment else random.uniform(0.5, 1)
        res += random.uniform(0, 0.5) if self.housing else random.uniform(0.5, 1)
        if self.salary <= config.min_salary:
            return res
        if self.salary >= config.max_salary:
            return res + 3
        return ((self.salary - config.min_salary) / (config.max_salary - config.min_salary)) * 5

    def environmental_satisfaction(self):
        # house_price_per_province[self.living_place]
        attractiveness = self.living_place.density / cuban_density
        if attractiveness <= config.min_attractiveness:
            return 0
        if attractiveness >= config.max_attractiveness:
            return 5
        return ((attractiveness - config.min_attractiveness) / (
            config.max_attractiveness - config.min_attractiveness)) * 5

    def evolve(self):
        if self.update_needed():
            self.update_satisfaction()
            return self.migration_decision()
        return False


class Province:
    def __init__(self, name, salary, unemployment, housing, density, population, living_places):
        self.name = name
        self.salary = salary
        self.unemployment = unemployment
        self.housing = housing
        self.density = density
        self.population = population
        self.living_places = living_places

    def __str__(self):
        return self.name


def initialize_population():
    agents = {}
    for p in provinces:
        agents[p.name] = []
        for i in range(int(numpy.ceil(p.population / config.people_per_agent))):
            l = define_living_place(p)
            s = define_salary(p)
            u = define_unemployment(p)
            h = define_housing(p)
            b = define_sociability()
            agents[p.name].append(Agent(sociability=b, province=p, salary=s, living_place=l, unemployment=u, housing=h))

    initialize_connections(agents)
    return agents


def initialize_connections(agents):
    for v in agents.values():
        for a in v:
            number_of_peers = int(random.normal(config.peers_per_agent, 2))
            a.peers = random.choice(v, max(0, number_of_peers))


def initialize_provinces():
    living_places_per_province = json.load(open('data/parsed_living_places'))
    salary_per_province = json.load(open('data/parsed_salaries'))
    unemployment_per_province = json.load(open('data/parsed_unemployment'))
    housing_per_province = json.load(open('data/parsed_housing'))
    density_per_province = json.load(open('data/parsed_density'))
    population_per_province = json.load(open('data/parsed_population'))
    global province_names
    province_names = list(salary_per_province.keys())
    for p in province_names:
        provinces.append(Province(name=p, salary=salary_per_province[p], unemployment=unemployment_per_province[p],
                             housing=housing_per_province[p], density=density_per_province[p],
                             population=population_per_province[p], living_places=living_places_per_province[p]))
    return provinces


def define_living_place(province):
    distribution = province.living_places
    total = distribution['Total']
    probabilities = [distribution[x] / total for x in province_names]
    selection = random.multinomial(1, probabilities)
    for i in range(len(selection)):
        if selection[i]:
            return provinces[i]


def define_sociability():
    value = random.uniform(0, 1)
    if value <= 0.2:
        value = 0
    elif value >= 0.8:
        value = 1
    return value


def define_salary(province):
    return random.normal(province.salary, 150)


def define_unemployment(province):
    return random.uniform(0, 100) < province.unemployment


def define_housing(province):
    return random.uniform(0, province.population) < 2 * province.housing


# region Comments
# def define_gender(province, gender_per_province):
# women_percent = gender_per_province[province]
# r = random.uniform(0, 100)
# return 'female' if r < women_percent else 'male'


# def define_age_group(province):
# r = random.uniform(0, 100)
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
#     f = open('population.txt')
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
