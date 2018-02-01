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
        [[0], [1,2], [1,2]],
    ),
    (
        _states,
        [1, 0],
        [[1,2], [0], [1,2]],
    ),
])
def test_matching_outcome_indices(target, indices, expected):
    from rullo.solver import calculate_matching_indices
    from rullo.state_set import StateSet
    from rullo.outcome import Outcome
    
    state_set = StateSet(target)
    outcome = Outcome(outcome)
    
    assert expected == calculate_matching_indices(state_set, state_set, indices)


