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
def test_outcome_intersection(content, row_constraints, column_constraints, expected):
    from rullo.rullo import Rullo
    from rullo.solver import get_final_outcomes

    rullo = Rullo(content, row_constraints, column_constraints)
    assert set(expected) == set(get_final_outcomes(rullo))


