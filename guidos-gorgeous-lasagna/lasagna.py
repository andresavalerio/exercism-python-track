'''
This module contains functions based on the preparation time of a lasagna
'''

EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'
    '''

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    '''
    :param layers: int layers in the lasagna
    :return: int time for preparation
    '''
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    :param number_of_layers: int layers in the lasagna
    :param elapsed_bake_time: int baking time already elapsed
    :return: int total elapsed cooking time
    '''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
