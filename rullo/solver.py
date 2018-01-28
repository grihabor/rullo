import itertools
import numpy as np
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
    

def states_set_filter(states_set, index, flag):
    """
    
    Attributes
    ----------
    states_set: set of 1-dim arrays
    index: int
    flag: 0 or 1
    
    Returns
    -------
    Filtered set of states
    """
    return set(
        state
        for state
        in states_set
        if state[index] == flag
    )
    
    
def states_sets_intersection(states_sets, 
                             indices):
    
    outcomes = [(
        states_set_filter(states_sets[0], indices[0], flag),
        states_set_filter(states_sets[1], indices[1], flag),
    ) for flag in [0, 1]]
    
    return outcomes


def find_indefeasible_indices(states_set):
    it = iter(states_set)
    start = next(it)
    result = reduce(lambda: x,y: x*y, it, start=start)
    return [
        i 
        for i, flag 
        in enumerate(result)
        if flag
    ]
    

def solve_board(rullo):
    state_storage = [
        
    ]
    # key - (row, column, flag)
    # value - 
    



