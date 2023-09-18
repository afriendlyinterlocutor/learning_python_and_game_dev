import random


def di_roll(di_type):
    """di_type is type: int
    returns type: int"""
    return random.randint(1, di_type)


def sum_multi_di_roll(di_type, amount_of_di):
    """di_type is type: int
    amount_of_di is type: int
    returns sum of amount_of_di of di_type as type: int"""
    amount_of_di = amount_of_di
    counter = 0
    result = int
    while counter < amount_of_di:
        result = result + di_roll(di_type)
        counter += 1
    return result
