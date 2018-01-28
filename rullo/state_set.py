import numpy as np


class StateSet:
    def __init__(self, states):
        self._states = np.asarray(states, dtype=bool)
        
    def __iter__(self):
        yield from self._states

    def __eq__(self, other):
        return np.all(self._states == other._states)
