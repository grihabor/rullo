import numpy as np
import pytest


@pytest.mark.parametrize('states,expected', [
    ([[0,1,1,0,0],
      [1,0,1,0,1],
      [1,1,1,0,0]], [3, 2]),
    ([[1,1,0,0,1],
      [1,0,1,0,1],
      [1,1,1,0,0]], [0, 3]),
])
def test_find_indefeasible_indices(states, expected):
    from rullo.solver import find_indefeasible_indices
    
    state_set = set(map(
        tuple, states
    ))
    
    assert set(expected) == set(find_indefeasible_indices(state_set))
    
    