import pytest
import numpy as np
import itertools


_states = np.array([
    [1,1,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,1],
])


@pytest.mark.parametrize('states,index,flag,expected', itertools.starmap((
    lambda s,i,f,e: (s,i,f,s[e])
), [
    (_states, 0, 0, [1, 2]),
    (_states, 0, 1, [0]),
    (_states, 1, 0, [2]),
    (_states, 1, 1, [0, 1]),
    (_states, 2, 0, [0, 1]),
    (_states, 2, 1, [2]),
    (_states, 3, 0, [0, 2]),
    (_states, 3, 1, [1]),
    (_states, 4, 0, [1]),
    (_states, 4, 1, [0, 2]),
]))
def test_state_set_filter(states, index, flag, expected):
    from rullo.state_set import StateSet

    states_set = StateSet(states)
    expected_set = StateSet(expected)
    assert expected_set == states_set.filter(index, flag)
