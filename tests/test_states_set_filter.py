import pytest
import numpy as np

_states = [
    np.array([1,1,0,0,1]),
    np.array([0,1,0,1,0]),
    np.array([0,0,1,0,1]),
]

@pytest.mark.parametrize('states,index,flag,expected', map((
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
def test_states_set_filter(states, index, flag, expected):
    from rullo.solver import states_set_filter
    
    states_set = set(map(
        tuple, states
    ))
    expected_set = set(map(
        tuple, expected
    ))
    assert expected_set == states_set_filter(
        states_set,      
        index,   
        flag,
    )
    