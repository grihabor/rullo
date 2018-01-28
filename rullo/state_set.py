import numpy as np


class StateSet:
    def __init__(self, states):
        self._states = np.asarray(states, dtype=bool)
        
    def __iter__(self):
        yield from self._states
