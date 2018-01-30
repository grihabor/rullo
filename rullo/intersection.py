import functools
import itertools
from collections import Counter


def _have_the_same_beginning(x, y):
    return any([
        x == y[:len(x)],
        y == x[:len(y)],
    )


def _longest(x, y):
    return (
        x
        if len(x) > len(y)
        else y
    )


def _intersect(outcome_1, outcome_2):
    product = itertools.product(outcome_1, outcome_2)
    result = []
    for item_1, item_2 in product:
        if _have_the_same_beginning(item_1, item_2):
            result.append(_longest(*pair))


def _outcome_intersection(outcomes):

    result = functools.reduce(
        _intersect,
        outcome[1:],
        outcome[0],
    )
    
    
    

    if len(outcomes) == 1:
        outcome = outcomes[0]
        c = Counter(outcome)
        new_outcomes = [
            (
                outcome_tuple + (index,)
                if c[outcome
            )
            for index, outcome_tuple
            in outcome
        ]
    else:
        new_outcomes = [
            
        ]

    return new_outcomes