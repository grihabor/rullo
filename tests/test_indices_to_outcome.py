import pytest


@pytest.mark.parametrize('outcome,indices,expected', [
    (
        [((0,),), ((1,),), ((2,),),],
        [[0], [1, 2], [1, 2]],
        [
            ((0,),),
            ((1, 1), (2, 1),),
            ((1, 2), (2, 2),),
        ],
    ),
])
def test_indices_to_outcome(outcome, indices, expected):
    from rullo.outcome import Outcome
    
    outcome = Outcome(outcome)
    expected = Outcome(expected)

    assert expected == Outcome.from_indices(indices, outcome)
