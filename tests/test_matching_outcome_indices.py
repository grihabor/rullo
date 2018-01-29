import pytest
import numpy as np


_states = np.array([
    [0,1,1],
    [1,0,1],
    [1,1,0],
])



@pytest.mark.parametrize('target,indices,outcome,expected', [
    (
        _states,
        [0, 0],
        [(0,), (1,), (2,)],
        [[0], [1,2], [1,2]],
    ),
    (
        _states,
        [1, 0],
        [(0,), (1,), (2,)],
        [[1,2], [0], [1,2]],
    ),
])
def test_matching_outcome_indices(target, indices, outcome, expected):
    from rullo.solver import _matching_outcome_indices, Dependency
    from rullo.state_set import StateSet

    state_set = StateSet(target)
    dependency = Dependency(state_set, indices, outcome)

    assert _matching_outcome_indices(state_set, dependency) == expected

