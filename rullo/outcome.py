import itertools
from collections import Counter

from rullo.intersection import calculate_outcome_intersection


class Outcome:
    def __init__(self, variants=None):
        assert all(
            isinstance(variant, tuple)
            for variant
            in variants
        )

        self._variants = (
            sorted(variants)
            if variants
            else []
        )

    @classmethod
    def from_indices(cls, indices, prev_outcome):
        return _calculate_outcome_from_indices(indices, prev_outcome)

    @classmethod
    def from_state_set(cls, state_set):
        return Outcome({
            (index,)
            for index
            in range(len(state_set))
        })

    @classmethod
    def from_outcome_intersection(cls, outcomes):
        return Outcome(calculate_outcome_intersection(outcomes))

    def __repr__(self):
        return '<Outcome {}>'.format(self._variants)
        
    def __eq__(self, other):
        return self._variants == other._variants

    def __getitem__(self, item):
        return self._variants[item]


def _calculate_outcome_from_indices(indices_list, prev_outcome: Outcome):
    flat = itertools.chain.from_iterable(indices_list)
    c = Counter(flat)
    nested = [
        [
            (
                prev_outcome[index] + (i,)
                if c[index] > 1
                else prev_outcome[index]
            )
            for index
            in indices
        ]
        for i, indices
        in enumerate(indices_list)
    ]
    return Outcome(sum(nested, []))
