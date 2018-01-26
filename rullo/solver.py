import itertools
import numpy as np


def iter_states(n_pos):
    it = itertools.product([0, 1], repeat=n_pos)
    yield from map(np.array, it)
    

def find_valid_states(content, constraint):
    pass