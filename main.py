__author__ = 'mario'

from initial_population import *


def check_affected(agent):
    pass


def measure_push(agent):
    pass


def measure_intervening(agent):
    pass


def measure_pull(agent):
    pass


def migrate(push, intervening, pull):
    pass


def find_best_destination(agent):
    pass


def update_destination(agent):
    pass


def update_attributes(agent):
    pass


def move_to_new_district(agent):
    pass


if __name__ == '__main__':
    agents = initialize_population()
    year = 2016
    while year < 2050:
        for agent in agents:
            if check_affected(agent):
                push = measure_push(agent)
                intervening = measure_intervening(agent)
                pull = measure_pull(agent)
                if migrate(push, intervening, pull):
                    find_best_destination(agent)
                    move_to_new_district(agent)
                    update_attributes(agent)
                    update_destination(agent)