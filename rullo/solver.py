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