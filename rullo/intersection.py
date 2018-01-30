import functools
import itertools
from collections import Counter


def _have_the_same_beginning(x, y):
    return any([
        x == y[:len(x)],
        y == x[:len(y)],
    ])


def _longest(x, y):
    return (
        x
        if len(x) > len(y)
        else y
    )


def _intersect(*outcome_pair):
    assert 2 == len(outcome_pair) 
    
    product = itertools.product(*outcome_pair)
    return [
        _longest(*pair)
        for pair in product
        if _have_the_same_beginning(*pair)
    ]
    

def _outcome_intersection(outcomes):

    result = functools.reduce(
        _intersect,
        outcome[1:],
        outcome[0],
    )
    
    c = Counter(result)
    outcome = [
        (
            item + (index,)
            if c[item] > 1
            else item
        )
        for index, item
        in enumerate(result)
    ]
    
    return outcome
    