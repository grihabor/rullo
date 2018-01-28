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
    from rullo.state_set import StateSet
    
    state_set = StateSet(states)

    assert set(expected) == state_set.indefeasible_indices()
    
    