"""
CP1404  Practical

"""

import doctest
from prac_06.car import Car

def repeat_string(s, n):

    return " ".join([s] * n)

def run_tests():
    """Run the tests on the functions."""

    test_car_default_fuel = Car()
    assert test_car_default_fuel._fuel == 0, "Car does not set default fuel correctly"

    test_car_custom_fuel = Car(fuel=10)
    assert test_car_custom_fuel._fuel == 10, "Car does not set custom fuel correctly"
doctest.testmod()

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length
def format_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('test this function')
    'Test this function.'
    """
    return phrase.capitalize() + '.'

doctest.testmod()
