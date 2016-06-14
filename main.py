__author__ = 'mario'

import initial_population


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
    agents = initial_population.initialize_population()
    # year = 2016
    # while year < 2050:
    #     year += 1
    #     for agent in agents:
    #         if agent.update_interval_done():
    #             agent.migration_decision()