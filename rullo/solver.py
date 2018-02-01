import itertools
import numpy as np

from .dependency import Dependency
from .state_set import StateSet
from .checks import is_line_valid
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


def calculate_matching_indices(target_state_set, dependency: Dependency):
    dep = dependency
    print()
    print('Calculate matching indices')
    print('--------------------------')
    print(target_state_set)
    print(dependency)
    print()
    
    result = [[
        index
        for index, dep_state
        in enumerate(dep.state_set)
        if state[dep.index_pair[0]] == dep_state[dep.index_pair[1]]
    ] for state in target_state_set]
    
    print('Result')
    print('------')
    print(result)
    print()
    
    return result

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
        Dependency(state_set, [index, i], outcome)
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
                i,
            )
            row_pairs.append(pair)
            
        if i < rullo.content.shape[1]:
            pair = calculate_next_outcome_pair(
                rullo.content[:, i], 
                rullo.column_constraints[i],
                column_pairs,
                i,
            )
            column_pairs.append(pair)
    
    return (
        row_pairs[1]
        if len(row_pairs) > len(column_pairs)
        else column_pairs[1]
    )
        
        
        