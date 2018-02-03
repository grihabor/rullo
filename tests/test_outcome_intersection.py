import pytest


@pytest.mark.parametrize('outcomes,expected', [
    ((
        [
            ((2,),),
            ((0,), (1,),),
            ((0,), (1,),),
        ],
        [
            ((1,2,0), (2,2,0), (0,1,0), (1,1,1,0), (2,1,1,0)),
            ((0,2), (1,1,2), (2,1,2),),
            ((1,2,2), (2,2,2), (0,1,2), (1,1,1,2), (2,1,1,2)),
        ],
    ), 
    [
        ((2,2,0), (2,1,1,0)),
        ((0,2), (1,1,2)),
        ((1,2,2), (0,1,2), (1,1,1,2),),
    ],),
])
def test_outcome_intersection(outcomes, expected):
    from rullo.outcome import Outcome

    outcomes = list(map(Outcome, outcomes))
    assert Outcome(expected) == Outcome.from_outcome_intersection(outcomes)


