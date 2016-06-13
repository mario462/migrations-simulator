__author__ = 'laila'


import numpy.random as random
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

age_group_per_province = {'La Habana': [12,8,13,7,10,11,9,10]}
living_place_per_province = json.load(open('parsed'))
# marital_status = {'La Habana': []}

class Agent:
    def __init__(self, gender, province, living_place, peers=[]):
        # self.age_group = age_group
        self.gender = gender
        self.province = province
        self.peers = peers
        self.living_place = living_place
        # self.marital_status = marital_status

    def __str__(self):
        return self.province + " " + str(self.age_group) + " " + self.gender + " " + self.living_place

    def migrate(self):
        return False


def initialize_population():
    agents = []
    for p in provinces:
        for i in range(population_per_province[p]):
            # a = define_age_group(p)
            g = define_gender(p)
            l = define_living_place(p.capitalize())
            agents.append(Agent(gender=g,province=p, living_place=l))
    return agents


def define_gender(province):
    women_percent = gender_per_province[province]
    r = random.uniform(0, 100)
    return 'female' if r < women_percent else 'male'


def define_age_group(province):
    r = random.uniform(0, 100)
    sum = 0
    j = 0
    for i in age_group_per_province[province]:
        sum += i
        j += 1
        if r <= sum:
            return j*10


def define_living_place(province):
    distribution = living_place_per_province[province]
    r = random.uniform(0, 100)
    sum = 0
    for p in distribution:
        sum += int(distribution[p])
        if r <= sum:
            return p


def define_peers(agents, province):
    agents_from_province = [a for a in agents if a.province == province]


provinces, population_per_province, gender_per_province = import_data()
agents = initialize_population()
for a in agents:
    print(a)

