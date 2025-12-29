"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME= 40
PREPARATION_TIME = 60

print (EXPECTED_BAKE_TIME)

def bake_time_remaining(elapsed_bake_time):
    ""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    ""
    return layers * 2

def elapsed_time_in_minutes(layers, time):
    ""
    return preparation_time_in_minutes(layers) + time
                                        

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
