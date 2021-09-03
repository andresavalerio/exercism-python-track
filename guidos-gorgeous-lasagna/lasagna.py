EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    '''
    :param layers: int layers in the lasagna 
    :return: int time for preparation
    
    Function that takes the number of layers added to 
    the lasagna as an argument and returns how many minutes 
    will be spent making them.
    '''
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    :param number_of_layers: int layers in the lasagna
    :param elapsed_bake_time: int baking time already elapsed
    :return: int total elapsed cooking time
    
    Function that returns the sum of the preperation time and the time that the
    lasanha has already spent baking in the oven.
    '''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time