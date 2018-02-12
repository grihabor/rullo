import functools

import numpy as np
import pytest


@pytest.fixture
def sort():
    return _sort


def _sort(x):
    x = [
        tuple(
            tuple(row)
            for row
            in solution
        )
        for solution
        in x
    ]
    return sorted(x)
