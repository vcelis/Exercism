""" Functions for the grains exercism challange"""


def square(number):
    """Calculate how many grains were on a given square."""
    if not 0 < number < 65:
        raise ValueError("square must be between 1 and 64")
    result = 1
    for _ in range(1, number):
        result += result
    return result

def total():
    """Calculate the total number of grains on the chessboard."""
    result = 0
    for x in range(1, 65):
        result += square(x)
    return result
