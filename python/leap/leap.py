"""Function for the leap exercism challange"""

def leap_year(year):
    """Function to check if given year is leap year."""
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0 and year % 100 == 0:
        return True
    return False
