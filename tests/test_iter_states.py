import pytest
import numpy as np


@pytest.mark.parametrize('n,expected', [
    (1, [np.array([0]), 
         np.array([1])]),
    (2, [np.array([0, 0]), 
         np.array([0, 1]),
         np.array([1, 0]),
         np.array([1, 1])]),
    (3, [np.array([0, 0, 0]), 
         np.array([0, 0, 1]), 
         np.array([0, 1, 0]),
         np.array([0, 1, 1]), 
         np.array([1, 0, 0]),
         np.array([1, 0, 1]), 
         np.array([1, 1, 0]),
         np.array([1, 1, 1])]),
])
def test_iter_states(n, expected):
    from rullo.solver import iter_states
    
    assert all(list(iter_states(n)) == expected)
    