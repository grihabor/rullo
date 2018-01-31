import functools
import numpy as np


class StateSet:
    def __init__(self, states):
        self._states = np.asarray(states, dtype=bool)

    def __iter__(self):
        yield from self._states

    def __getitem__(self, index):
        return self._states[index]

    def __eq__(self, other):
        return np.all(self._states == other._states)

    def filter(self, index, flag):
        self._states = _state_set_filter(self._states, index, flag)
        return self

    def __repr__(self):
        return repr(self._states)

    def indefeasible_indices(self):
        return _indefeasible_indices(self._states)

    def __len__(self):
        return len(self._states)
        
        
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
    return states[states[:, index] == flag]


def _indefeasible_indices(states):
    """

    Attributes
    ----------
    states: 2-dim array

    """
    zeros = np.logical_and.reduce(states, axis=0)
    ones = np.logical_and.reduce(np.logical_not(states), axis=0)
    return set(
        np.where(ones)[0].tolist() + np.where(zeros)[0].tolist()
    )
