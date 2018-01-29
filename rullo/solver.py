import itertools
import functools
import numpy as np
from collections import Counter

from rullo.state_set import StateSet
from .checks import is_line_valid


def iter_states(n_pos):
    it = itertools.product([0, 1], repeat=n_pos)
    yield from map(np.array, it)


def iter_valid_states(content, constraint):
    """

    Attributes
    ----------
    content: 1-dim array
    constraint: int
    """
    for state in iter_states(content.shape[0]):
        if is_line_valid(content, state, constraint):
            yield state


def valid_states_set(content, constraint):
    return set(iter_valid_states(content, constraint))


class Dependency:
    def __init__(self, state_set, index_pair, outcome):
        self.state_set = state_set
        self.index_pair = index_pair
        self.outcome = outcome


def _initialize_outcome(state_set):
    return [
        (index,)
        for index
        in range(len(state_set))
    ]


def _matching_outcome_indices(target_state_set, dependency):
    dep = dependency
    print(target_state_set[0])
    return [[
        index
        for index, dep_state
        in enumerate(dep.state_set)
        if state[dep.index_pair[0]] == dep_state[dep.index_pair[1]]
    ] for state in target_state_set]


def _outcome_intersection(outcomes):
    if len(outcomes) == 1:
        outcome = outcomes[0]
        new_outcomes = [
            outcome + (index,)
            for index, outcome
            in outcome
        ]
    else:
        new_outcomes = [
            
        ]

    return new_outcomes


def _indices_to_outcome(indices, prev_outcome):
    flat = itertools.chain.from_iterable(indices)
    c = Counter(flat)
    nested = [
        [
            (
                prev_outcome[index] + (i,)
                if c[index] > 1
                else prev_outcome[index]
            )
            for index
            in index_list
        ]
        for i, index_list
        in enumerate(indices)
    ]
    return sum(nested, [])


def _calculate_outcomes(target_state_set, *dependencies):
    if not dependencies:
        return _initialize_outcome(target_state_set)

    outcomes = []

    for dep in dependencies:
        indices = _matching_outcome_indices(target_states_set, dep)
        outcomes.append(indices)


