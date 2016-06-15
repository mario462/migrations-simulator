__author__ = 'laila'

import numpy
import numpy.random as random
import config
import json


provinces = []
province_names = []
cuban_density = 101.6


class Agent:
    def __init__(self, province):
        self.province = province
        self.peers = []
        self.sociability = define_sociability()
        self.living_place = define_living_place(province)
        self.salary = define_salary(province)
        self.unemployment = define_unemployment(province)
        self.housing = define_housing(province)
        self.update_ratio = 1
        self.satisfaction = -1

    def __str__(self):
        return self.province + " " + self.living_place

    def migration_decision(self):
        should, province, people = self.should_migrate(self.sociable())
        if should:
            old_province = self.living_place
            self.migrate(province, people)
            return True, old_province, province, people
        return False, None, None, None

    def should_migrate(self, sociable):
        if sociable:
            max_sat, province = 0, None
            for p in self.peers:
                if p.living_place != self.living_place:
                    sat = (p.social_satisfaction() - self.social_satisfaction()) * config.social_weight \
                          + (p.economical_satisfaction() - self.economical_satisfaction()) * config.economical_weight \
                          + (p.environmental_satisfaction() - self.environmental_satisfaction()) * config.environmental_weight
                    total_sat = self.update_ratio * self.sociability * sat
                    if total_sat > max_sat:
                        max_sat = total_sat
                        province = p.living_place
        else:
            max_sat, province = 0, None
            for p in provinces:
                if p != self.living_place:
                    sat = (self.hypothetical_social_satisfaction(p) - self.social_satisfaction()) * config.social_weight \
                          + (self.hypothetical_economical_satisfaction(p) - self.economical_satisfaction()) * config.economical_weight \
                          + (self.hypothetical_environmental_satisfaction(p) - self.environmental_satisfaction()) * config.environmental_weight
                    total_sat = self.update_ratio * sat
                    if total_sat > max_sat:
                        max_sat = total_sat
                        province = p

        if max_sat > config.migration_threshold:
            return True, province, config.people_per_agent
        if max_sat > 9/10*(config.migration_threshold):
            return True, province, (3/4)*config.people_per_agent
        if max_sat > 8/10*(config.migration_threshold):
            return True, province, (1/2)*config.people_per_agent
        if max_sat > 7/10*(config.migration_threshold):
            return True, province, (1/4)*config.people_per_agent
        else:
            return False, None, None

    def sociable(self):
        if self.sociability == 1:
            return True
        elif self.sociability == 0:
            return False
        threshold = random.normal(0.5, 0.1)
        return True if self.sociability >= threshold else False

    def migrate(self, province, people):
        old_province = self.living_place
        old_province.population -= people
        old_province.density = old_province.population / old_province.extension

        new_province = province
        new_province.population += people
        new_province.density = new_province.population / new_province.extension

        original_province = self.province
        original_province.living_places[old_province.name] -= people
        original_province.living_places[new_province.name] -= people

        self.living_place = province

        self.salary = define_salary(province)
        self.housing = define_housing(province)
        self.unemployment = define_unemployment(province)

        self.update_ratio = 1

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

    def hypothetical_social_satisfaction(self, province):
        peers_in_province = len(list(filter(lambda x: x.living_place == province.name, self.peers)))
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

    def hypothetical_economical_satisfaction(self, province):
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
        attractiveness = self.living_place.density / cuban_density
        if attractiveness <= config.min_attractiveness:
            return 0
        if attractiveness >= config.max_attractiveness:
            return 5
        return ((attractiveness - config.min_attractiveness) / (
            config.max_attractiveness - config.min_attractiveness)) * 5

    def hypothetical_environmental_satisfaction(self, province):
        # house_price_per_province[self.living_place]
        attractiveness = province.density / cuban_density
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
        return False, None, None, None


class Province:
    def __init__(self, name, salary, unemployment, housing, density, population, extension, living_places):
        self.name = name
        self.salary = salary
        self.unemployment = unemployment
        self.housing = housing
        self.density = density
        self.population = population
        self.extension = extension
        self.living_places = living_places

    def __str__(self):
        return self.name


def initialize_population():
    agents = {}
    for p in provinces:
        agents[p.name] = []
        for i in range(int(numpy.ceil(p.population / config.people_per_agent))):
            agents[p.name].append(Agent(province=p))

    initialize_connections(agents)
    return agents


def initialize_connections(agents):
    for v in agents.values():
        for a in v:
            number_of_peers = max(int(random.normal(config.peers_per_agent, 2)), 1)
            randoms = random.randint(0, len(v), number_of_peers)
            for r in randoms:
                a.peers.append(v[r])


def initialize_provinces():
    living_places_per_province = json.load(open('data/parsed_living_places'))
    salary_per_province = json.load(open('data/parsed_salaries'))
    unemployment_per_province = json.load(open('data/parsed_unemployment'))
    housing_per_province = json.load(open('data/parsed_housing'))
    density_per_province = json.load(open('data/parsed_density'))
    extension_per_province = json.load(open('data/parsed_extension'))
    population_per_province = json.load(open('data/parsed_population'))
    global province_names
    province_names = list(salary_per_province.keys())
    for p in province_names:
        provinces.append(Province(name=p, salary=salary_per_province[p], unemployment=unemployment_per_province[p],
                             housing=housing_per_province[p], density=density_per_province[p],
                             population=population_per_province[p], extension=extension_per_province[p],
                             living_places=living_places_per_province[p]))
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


if __name__ == '__main__':
    pass
