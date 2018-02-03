import itertools
import numpy as np

from .dependency import Dependency
from .state_set import StateSet
from .checks import is_line_valid
from .outcome import Outcome
from .utils import print_debug_info


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


def calculate_matching_indices(target_state_set, dep_state_set, index_pair):
    
    return [[
        index
        for index, dep_state
        in enumerate(dep_state_set)
        if state[index_pair[0]] == dep_state[index_pair[1]]
    ] for state in target_state_set]
    

class SolveError(Exception):
    pass


@print_debug_info
def calculate_outcome_dependency_intersection(target_state_set, *dependencies):
    if target_state_set.is_empty():
        raise SolveError('Target state set is empty')
    
    if not dependencies:
        return Outcome.from_state_set(target_state_set)

    outcomes = []

    for dep in dependencies:
        indices = calculate_matching_indices(
            target_state_set,
            dep.state_set,
            dep.index_pair,
        )
        outcome = Outcome.from_indices(indices, dep.outcome)
        outcomes.append(outcome)

    return Outcome.from_outcome_intersection(outcomes)


def calculate_next_outcome_pair(content, constraint, pairs, index):
    """
    
    Attributes
    ----------
    content: 1-dim array
    constraint: int
    pairs: list of pairs (state_set, outcome)
    index: int
    """
    target_state_set = StateSet(
        iter_valid_states(content, constraint)
    )
            
    deps = [
        Dependency(state_set, [i, index], outcome)
        for i, (state_set, outcome)
        in enumerate(pairs)
    ]
            
    outcome = calculate_outcome_dependency_intersection(target_state_set, *deps)
    
    return target_state_set, outcome
            

def calculate_final_outcome(rullo):

    row_pairs = []
    column_pairs = []
    
    for i in range(max(rullo.content.shape)):
        print()
        print(
            '+' * 5 + ' ' * 3, 
            i, 
            ' ' * 3 + '+' * 5,
        )
        print()
        if i < rullo.content.shape[0]:
            pair = calculate_next_outcome_pair(
                rullo.content[i, :], 
                rullo.row_constraints[i],
                column_pairs,
                i,
            )
            row_pairs.append(pair)
            
        if i < rullo.content.shape[1]:
            pair = calculate_next_outcome_pair(
                rullo.content[:, i], 
                rullo.column_constraints[i],
                row_pairs,
                i,
            )
            column_pairs.append(pair)
    
    return (
        row_pairs[1]
        if len(row_pairs) > len(column_pairs)
        else column_pairs[1]
    )
        
        
        