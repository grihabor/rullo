import pytest
import numpy as np


_content = np.array([
    [6,4,1,2,9],
    [3,1,4,1,4],
    [3,3,3,9,3],
    [8,2,5,9,8],
], dtype=np.int)

_state = np.array([
    [0,1,0,0,1],
    [1,0,1,1,1],
    [1,1,0,0,1],
    [0,0,1,0,0],
])

@pytest.mark.parametrize('content,state,row_constraints,column_constraints,result', [
    (_content, _state, np.array([13, 12, 9, 5]), np.array([6, 7, 9, 1, 16]), True),
    (_content, _state, np.array([3, 21, 9, 5]), np.array([6, 17, 2, 1, 16]), False),
    (_content, _state, np.array([3, 2, 6, 6]), np.array([6, 17, 11, 13, 1]), False),
])
def test_is_line_valid(content, state, row_constraints, column_constraints, result):
    from rullo.checks import is_board_valid

    assert result == is_board_valid(content,
                                    state,
                                    row_constraints,
                                    column_constraints)
