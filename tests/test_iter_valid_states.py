import pytest
import numpy as np


@pytest.mark.parametrize('content,constraint,valid,expected', [(
    [3,2,5,6,4],
    8,
    True,
    [[1,0,1,0,0],
     [0,1,0,1,0]],
), (
    [3,2,5,6,4],
    5,
    False,
    [[1,0,1,0,0],
     [0,1,0,1,0]],
), (
    [3,2,5,6,4],
    8,
    False,
    [[1,0,1,0,0]],
), (
    [3,3,2,3],
    6,
    True,
    [[1,1,0,0],
     [1,0,0,1],
     [0,1,0,1]],
), (
    [3,3,2,3],
    6,
    False,
    [[1,0,0,1],
     [0,1,0,1]],
), (
    [3,7,2,3],
    6,
    False,
    [[1,1,0,0],
     [1,0,0,1],
     [0,1,0,1]],
)])
def test_iter_valid_states(content, constraint, valid, expected):
    from rullo.solver import iter_valid_states
    
    content = np.array(content)

    expected_set = expected
    result_set = iter_valid_states(content, constraint)
    
    if valid:
        assert expected_set == result_set
    else:
        assert expected_set != result_set