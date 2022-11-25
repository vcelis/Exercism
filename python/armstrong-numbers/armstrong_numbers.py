"""Function for the Armstrong number exercism challange"""


def is_armstrong_number(number):
    """Function to check if given number is Armstrong number.

    An Armstrong number is a number that is the sum of its own
    digits each raised to the power of the number of digits.
    """
    nums = [int(n) for n in str(number)]
    result = 0
    for num in nums:
        result += num**len(nums)
    return result == number