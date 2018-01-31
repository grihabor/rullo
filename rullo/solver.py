import itertools
import functools
import numpy as np
from collections import Counter

from .state_set import StateSet
from .checks import is_line_valid
from .intersection import _outcome_intersection
from .outcome import outcome


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
    assert len(content.shape) == 1
    assert len(content.shape[0]) > 0
    
    for state in iter_states(content.shape[0]):
        if is_line_valid(content, state, constraint):
            yield state


class Dependency:
    def __init__(self, state_set, index_pair, outcome):
        assert isinstance(state_set, StateSet)
        assert isinstance(outcome, Outcome)
        
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
        outcome = _indices_to_outcome(indices, dep.outcome)
        outcomes.append(outcome)

    return _outcome_intersection(outcomes)


def _cycle(content, constraint, pairs):
    target_state_set = StateSet(
        iter_valid_states(content, constraint)
    )
            
    deps = [
        Dependency(state_set, [j, i], outcome)
        for i, (state_set, outcome)
        in enumerate(pairs)
    ]
            
    outcome = _calculate_outcomes(target_state_set, *deps)
    pairs.append(
        (target_state_set, outcome)
    )
            

def get_final_outcomes(rullo):

    row_pairs = []
    column_pairs = []
    
    for i in range(max(rullo.content.shape)):
        if i < rullo.content.shape[0]:
            _cycle(
                rullo.content[i, :], 
                rullo.row_constraints[i],
                row_pairs,
            )
            
        if i < rullo.content.shape[1]:
            _cycle(
                rullo.content[:, i], 
                rullo.column_constraints[i],
                column_pairs,
            )
    
    return (
        row_pairs[1]
        if len(row_pairs) > len(column_pairs)
        else column_pairs[1]
    )
        
        
        