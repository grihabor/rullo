import pytest
import numpy as np


@pytest.mark.parametrize('content,row_constraints,column_constraints,expected', [
    ([[3,3,3],
      [3,3,3],
      [3,3,3]],
     [6,6,6],
     [6,6,6],
     {
         np.array([
             [0,1,1],
             [1,0,1],
             [1,1,0],
         ]),
         np.array([
             [0,1,1],
             [1,1,0],
             [1,0,1],
         ]),
         np.array([
             [1,0,1],
             [0,1,1],
             [1,1,0],
         ]),
         np.array([
             [1,0,1],
             [1,1,0],
             [0,1,1],
         ]),
         np.array([
             [1,1,0],
             [0,1,1],
             [1,0,1],
         ]),
         np.array([
             [1,1,0],
             [1,0,1],
             [0,1,1],
         ]),
     }),
    
])
def test_solve(content, row_constraints, column_constraints, expected):
    from rullo.rullo import Rullo
    from rullo.solver import solve
    
    assert expected == solve(Rullo(
        content,
        row_constraints,
        column_constraints,
    ))
    