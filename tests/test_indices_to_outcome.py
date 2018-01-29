import pytest
import numpy as np


def test_indices_to_outcome():
    from rullo.solver import _indices_to_outcome

    outcome = [(0,), (1,), (2,),]
    indices = [[0], [1, 2], [1, 2]]
    expected = [
        (0,),
        (1, 1),
        (2, 1),
        (1, 2),
        (2, 2),
    ]

    assert all(expected == _indices_to_outcome(indices, outcome))
