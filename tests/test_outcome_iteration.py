import pytest
import numpy as np


@pytest.mark.parametrize('content,constraint,pairs,index,expected', [
    ([3,3,3], 6, [], 0, (
        [[0,1,1],
         [1,1,0],
         [1,0,1]],
        [(0,), (1,), (2,)]
    )),
])
def test_outcome_iteration(content, constraint, pairs, index, expected):
    from rullo.solver import calculate_next_outcome_pair
    from rullo.outcome import Outcome
    from rullo.state_set import StateSet

    pairs = [
        (StateSet(state_set), Outcome(outcome))
        for state_set, outcome
        in pairs
    ]
    content = np.array(content, dtype=np.int)
    assert (
        StateSet(expected[0]), Outcome(expected[1])
    ) == calculate_next_outcome_pair(content, constraint, pairs, index)


