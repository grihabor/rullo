import itertools
import numpy as np

from .checks import is_line_valid, is_board_valid



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


def possible_states(rullo):
    row_states = [
        list(iter_valid_states(row, constraint))
        for row, constraint
        in zip(rullo.content, rullo.row_constraints)
    ]
    rullo_states = list(itertools.product(*row_states))
    
    return np.asarray(rullo_states)
        
        
def solve(rullo):
    states = possible_states(rullo)
    
    result = set()
    for state in states:
        if is_board_valid(rullo.content,
                          state,
                          rullo.row_constraints,
                          rullo.column_constraints):
            result.add(state)
    
    return result
    
    