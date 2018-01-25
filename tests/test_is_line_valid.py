import pytest
import numpy as np


@pytest.mark.parametrize('content,state,constraint,result', [
    (np.array([2, 5, 4, 8, 2]), np.array([1, 0, 0, 1, 0]), 10, True),
    (np.array([2, 5, 4, 8, 2]), np.array([0, 0, 0, 1, 1]), 10, True),
    (np.array([2, 5, 4, 8, 2]), np.array([0, 1, 1, 0, 0]), 10, False),
    (np.array([2, 5, 4, 8, 2]), np.array([1, 1, 1, 1, 1]), 10, False),
    (np.array([2, 5, 4, 8, 2]), np.array([0, 0, 0, 0, 0]), 10, False),
])
def test_is_line_valid(content, state, constraint, result):
    from rullo.rullo import is_line_valid
    
    assert result == is_line_valid(content, state, constraint)