import pytest
import numpy as np


@pytest.mark.parametrize('content,constraint,expected', [
    (np.array([3,2,5,6,4]), 8, [np.array([1,0,1,0,0]),
                                np.array([0,1,0,1,0])]),
    (np.array([3,3,2,3]), 6, [np.array([1,1,0,0]),
                              np.array([1,0,0,1]),
                              np.array([0,1,0,1])]),
])
def test_iter_valid_states(content, constraint, expected):
    from rullo.solver import iter_valid_states
    
    assert set(map(
        tuple, expected
    )) == set(map(
        tuple, iter_valid_states(content, constraint)
    ))
    