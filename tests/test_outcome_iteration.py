import pytest


@pytest.mark.parametrize('content,constraint,pairs,expected', [
    ([3,3,3], 6, [], []),
])
def test_outcome_iteration(content, constraint, pairs, expected):
    from rullo.solver import calculate_next_outcome_pair
    pairs = [
        (StateSet(state_set), Outcome(outcome))
        for state_set, outcome
        in pairs
    ]
    assert expected == calculate_next_outcome_pair(content, constraint, pairs)


