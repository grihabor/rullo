import itertools
import functools
import numpy as np
from collections import Counter

from .state_set import StateSet
from .checks import is_line_valid
from .intersection import _outcome_intersection
from .outcome import Outcome


def iter_all_states(n_pos):
    it = itertools.product([0, 1], repeat=n_pos)
    yield from map(np.array, it)


def iter_valid_states(content, constraint):
    """

    Attributes
    ----------
    content: 1-dim array
    constraint: int
    """
    assert len(content.shape) == 1
    assert content.shape[0] > 0
    
    for state in iter_all_states(content.shape[0]):
        if is_line_valid(content, state, constraint):
            yield state


class Dependency:
    def __init__(self, state_set, index_pair, outcome):
        assert isinstance(state_set, StateSet)
        assert isinstance(outcome, Outcome)
        
        self.state_set = state_set
        self.index_pair = index_pair
        self.outcome = outcome


def calculate_matching_indices(target_state_set, dependency):
    dep = dependency
    print(target_state_set[0])
    return [[
        index
        for index, dep_state
        in enumerate(dep.state_set)
        if state[dep.index_pair[0]] == dep_state[dep.index_pair[1]]
    ] for state in target_state_set]


def calculate_outcome_from_indices(indices, prev_outcome):
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
    return Outcome(sum(nested, []))


class SolveError(Exception):
    pass


def calculate_outcome_dependency_intersection(target_state_set, *dependencies):
    if target_state_set.is_empty():
        raise SolveError('Target state set is empty')
    
    if not dependencies:
        return Outcome.from_state_set(target_state_set)

    outcomes = []

    for dep in dependencies:
        indices = calculate_matching_indices(target_state_set, dep)
        outcome = calculate_outcome_from_indices(indices, dep.outcome)
        outcomes.append(outcome)

    return _outcome_intersection(outcomes)


def calculate_next_outcome_pair(content, constraint, pairs):
    """
    
    Attributes
    ----------
    content: 1-dim array
    constraint: int
    pairs: list of pairs (state_set, outcome)
    """
    target_state_set = StateSet(
        iter_valid_states(content, constraint)
    )
            
    deps = [
        Dependency(state_set, [j, i], outcome)
        for i, (state_set, outcome)
        in enumerate(pairs)
    ]
            
    outcome = calculate_outcome_dependency_intersection(target_state_set, *deps)
    
    return target_state_set, outcome
            

def calculate_final_outcome(rullo):

    row_pairs = []
    column_pairs = []
    
    for i in range(max(rullo.content.shape)):
        if i < rullo.content.shape[0]:
            pair = calculate_next_outcome_pair(
                rullo.content[i, :], 
                rullo.row_constraints[i],
                row_pairs,
            )
            row_pairs.append(pair)
            
        if i < rullo.content.shape[1]:
            pair = calculate_next_outcome_pair(
                rullo.content[:, i], 
                rullo.column_constraints[i],
                column_pairs,
            )
            column_pairs.append(pair)
    
    return (
        row_pairs[1]
        if len(row_pairs) > len(column_pairs)
        else column_pairs[1]
    )
        
        
        