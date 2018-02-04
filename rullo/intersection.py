import functools
import itertools
from collections import Counter
from .utils import print_debug_info


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


def _intersect_sections(*outcome_pair):
    assert 2 == len(outcome_pair) 
    
    product = itertools.product(*outcome_pair)
    return tuple(
        _longest(*pair)
        for pair in product
        if _have_the_same_beginning(*pair)
    )


def _intersect(*outcome_pair):
    return [
        _intersect_sections(*section_pair)
        for section_pair
        in zip(*outcome_pair)
    ]


@print_debug_info
def calculate_outcome_intersection(outcomes):
    
    intersection = functools.reduce(
        _intersect,
        outcomes[1:],
        outcomes[0],
    )
    result = intersection
    '''
    c = Counter(intersection)
    result = [
        (
            item + (index,)
            if c[item] > 1
            else item
        )
        for index, item
        in enumerate(intersection)
    ]
    '''
    
    return result
    