import pytest



@pytest.mark.parametrize('content,row_constraints,column_constraints,expected', [
    ([[3,3,3],
      [3,3,3],
      [3,3,3]],
     [6,6,6],
     [6,6,6],
     []),
    
])
def test_solve(content, row_constraints, column_constraints, expected):
    from rullo.rullo import Rullo
    from rullo.solver import solve
    
    assert expected == solve(Rullo(
        content,
        row_constraints,
        column_constraints,
    ))
    