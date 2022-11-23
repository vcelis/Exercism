"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagne has been in the oven as an
    argument and returns how many minutes the lasagna still needs to bake based  
    on the 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time remaining.

    :param number_of_layers: int - number of layers to be added to the lasagna.
    :return: int - additional preparation time (in minutes) required for number_of_layers.

    Function that takes the number of layers to be added to the lasagna as an
    argument and returns how many additional minutes of preparation the lasagna needs
    based on the 'PREPARATION_TIME'.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total number of minutes it has been cooking.

    :param number_of_layers: int - number of layers to be added to the lasagna.
    :param elapsed_bake_time: int - number of minutes the lasagna has been baking in the oven.
    :return: int - total number of minutes you've been cooking so far

    Function takes the bumber of layers to be added to the lasagna and the number of
    minutes the lasagna has been baking so far in the oven and returns the total number of
    minutes you've been cooking.

    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
