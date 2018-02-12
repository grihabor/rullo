import pytest
import numpy as np


@pytest.mark.parametrize('n,expected', [
    (1, np.array([[0], 
                  [1]])),
    (2, np.array([[0, 0], 
                  [0, 1],
                  [1, 0],
                  [1, 1]])),
    (3, np.array([[0, 0, 0], 
                  [0, 0, 1],
                  [0, 1, 0],
                  [0, 1, 1], 
                  [1, 0, 0],
                  [1, 0, 1], 
                  [1, 1, 0],
                  [1, 1, 1]])),
])
def test_iter_states(n, expected):
    from rullo.solver import iter_all_states
    
    assert np.all(
        np.array(list(iter_all_states(n))) == expected
    )
    