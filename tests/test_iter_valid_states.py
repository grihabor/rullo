import pytest
import numpy as np


@pytest.mark.parametrize('content,constraint,valid,expected', [
    (np.array([3,2,5,6,4]), 8, True, [np.array([1,0,1,0,0]),
                                      np.array([0,1,0,1,0])]),
    (np.array([3,3,2,3]), 6, True, [np.array([1,1,0,0]),
                                    np.array([1,0,0,1]),
                                    np.array([0,1,0,1])]),
])
def test_iter_valid_states(content, constraint, valid, expected):
    from rullo.solver import iter_valid_states
    
    expected_set = set(map(
        tuple, expected
    )) 
    result_set = set(map(
        tuple, iter_valid_states(content, constraint)
    ))
    
    if valid:
        assert expected_set == result_set
    else:
        assert expected_set != result_set