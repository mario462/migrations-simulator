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
density_per_province = json.load(open('data/parsed_density'))


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
        should, province = self.should_migrate(self.sociable())
        if should:
            self.migrate(province)
            return True
        return False

    def should_migrate(self, sociable):
        if sociable:
            max_sat, province = 0, None
            for p in self.peers:
                sat = (p.social_satisfaction() - self.social_satisfaction()) * config.social_weight \
                      + (p.economical_satisfaction() - self.economical_satisfaction()) * config.economical_weight \
                      + (p.environmental_satisfaction() - self.environmental_satisfaction()) * config.environmental_weight
                total_sat = self.update_ratio * self.sociability * sat
                if total_sat > max_sat:
                    max_sat = total_sat
                    province = p.living_place
            if max_sat > config.migration_treshold:
                return True, province
            else:
                return False, None
        else:
            return True, 'La Habana'

    def sociable(self):
        if self.sociability == 1:
            return True
        elif self.sociability == 0:
            return False
        treshold = random.normal(0.5, 0.2)
        return True if self.sociability >= treshold else False

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

    def hipothetical_social_satisfaction(self, province):
        peers_in_province = len(list(filter(lambda x: x.living_place == province, self.peers)))
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
        return ((self.salary - config.min_salary) / (config.max_salary - config.min_salary)) * 3 + res

    def hipothetical_economical_satisfaction(self, province):
        res = random.uniform(0, 0.5) if define_unemployment(province) else random.uniform(0.5, 1)
        res += random.uniform(0, 0.5) if define_housing(province) else random.uniform(0.5, 1)
        salary = define_salary(province)
        if salary <= config.min_salary:
            return res
        if salary >= config.max_salary:
            return res + 3
        return ((salary - config.min_salary) / (config.max_salary - config.min_salary)) * 3 + res

    def environmental_satisfaction(self):
        # house_price_per_province[self.living_place]
        attractiveness = density_per_province[self.living_place] / density_per_province['Total']
        if attractiveness <= config.min_attractiveness:
            return 0
        if attractiveness >= config.max_attractiveness:
            return 5
        return ((attractiveness - config.min_attractiveness) / (
            config.max_attractiveness - config.min_attractiveness)) * 5

    def hipothetical_environmental_satisfaction(self, province):
        # house_price_per_province[self.living_place]
        attractiveness = density_per_province[province] / density_per_province['Total']
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
            l = define_living_place(p)
            s = define_salary(p)
            u = define_unemployment(p)
            h = define_housing(p)
            b = define_sociability()
            agents[p].append(Agent(sociability=b, province=p, salary=s, living_place=l, unemployment=u, housing=h))

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


def define_sociability():
    value = random.uniform(0, 1)
    if value <= 0.2:
        value = 0
    elif value >= 0.8:
        value = 1
    return value


def define_salary(province):
    return random.normal(salary_per_province[province], 100)


def define_unemployment(p):
    return random.uniform(0, 100) < unemployment_per_province[p]


def define_housing(p):
    return random.uniform(0, population_per_province[p]) < 2 * housing_per_province[p]


# region Comments
# def define_gender(province, gender_per_province):
# women_percent = gender_per_province[province]
# r = random.uniform(0, 100)
# return 'female' if r < women_percent else 'male'


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
