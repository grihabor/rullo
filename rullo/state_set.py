import numpy as np


class StateSet:
    def __init__(self, states):
        self._states = np.asarray(states, dtype=bool)
        
    def __iter__(self):
        yield from self._states

    def __eq__(self, other):
        return np.all(self._states == other._states)

    def filter(self, index, flag):
        self._states = _state_set_filter(self._states, index, flag)
        return self


def _state_set_filter(states, index, flag):
    """

    Attributes
    ----------
    states_set: StateSet
    index: int
    flag: 0 or 1

    Returns
    -------
    Filtered set of states
    """
    return np.extract(states[:, index] == flag, states)