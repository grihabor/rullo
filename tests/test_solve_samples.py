import os

import itertools
import numpy as np
import pytest


SAMPLES_PATH = os.path.join('tests', 'samples')
SOLUTIONS_PATH = os.path.join('tests', 'solutions')


def _sample_path(filename):
    return os.path.join(SAMPLES_PATH, filename)


def _solution_paths(sample_filename):
    name, _ = os.path.splitext(sample_filename)
    path = os.path.join(SOLUTIONS_PATH, name)
    return [
        os.path.join(path, filename)
        for filename
        in os.listdir(path)
    ]


def load_solutions(paths):
    return [
        np.loadtxt(path, delimiter=',')
        for path
        in paths
    ]


@pytest.mark.parametrize('path,solution_paths', [
    (_sample_path(filename), _solution_paths(filename))
    for filename
    in os.listdir(SAMPLES_PATH)
])
def test_solve_samples(path, solution_paths, sort):
    from rullo import solve, Rullo

    with open(path, 'r') as f:
        rullo = Rullo.from_csv(f)

    assert np.all(sort(solve(rullo)) == sort(load_solutions(solution_paths)))


