import pytest


@pytest.mark.parametrize('content,row_constraints,column_constraints,expected', [
    ([
        [3,3,3,3],
        [3,3,3,3],
        [3,3,3,3],
    ], [
        9,9,6
    ], [
        6,6,6,6
    ], [
    
    ]),
])
def test_get_final_outcomes(content, row_constraints, column_constraints, expected):
    from rullo.rullo import Rullo
    from rullo.solver import calculate_final_outcome

    rullo = Rullo(content, row_constraints, column_constraints)
    assert set(expected) == set(calculate_final_outcome(rullo))


