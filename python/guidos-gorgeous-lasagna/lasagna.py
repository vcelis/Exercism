"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPERATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    return elapsed_bake_time - EXPECTED_BAKE_TIME

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * PREPERATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return bake_time_remaining(elapsed_bake_time) + preparation_time_in_minutes(number_of_layers)
