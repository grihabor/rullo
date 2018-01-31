import pytest
import numpy as np


def test_indices_to_outcome():
    from rullo.solver import _indices_to_outcome
    from rullo.outcome import Outcome
    
    outcome = [(0,), (1,), (2,),]
    indices = [[0], [1, 2], [1, 2]]
    expected = Outcome([
        (0,),
        (1, 1),
        (2, 1),
        (1, 2),
        (2, 2),
    ])

    assert expected == _indices_to_outcome(indices, outcome)
