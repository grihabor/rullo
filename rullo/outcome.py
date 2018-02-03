import itertools
from collections import Counter

from .intersection import calculate_outcome_intersection
from .utils import print_debug_info


class Outcome:
    def __init__(self, variants=None):
        assert all(
            isinstance(variant, tuple)
            for variant
            in variants
        )

        self._variants = (
            variants
            if variants
            else []
        )

    @classmethod
    def from_indices(cls, indices, prev_outcome):
        return _calculate_outcome_from_indices(indices, prev_outcome)

    @classmethod
    def from_state_set(cls, state_set):
        return Outcome([
            ((index,),)
            for index
            in range(len(state_set))
        ])

    @classmethod
    def from_outcome_intersection(cls, outcomes):
        return Outcome(calculate_outcome_intersection(outcomes))

    def __repr__(self):
        if not self._variants:
            return '<Outcome {}>'
            
        return '\n'.join([
            '<Outcome {',
        ] + [
            '    ' + str(list(section))
            for section
            in self._variants
        ] + [
            '}>'
        ])
        
    def __eq__(self, other):
        return sorted(self._variants) == sorted(other._variants)

    def __getitem__(self, item):
        try:
            return self._variants[item]
        except IndexError:
            return tuple()


@print_debug_info
def _calculate_outcome_from_indices(indices_list, prev_outcome: Outcome):

    flat = itertools.chain.from_iterable(indices_list)
    c = Counter(flat)
    nested = [
        tuple(
            (
                out_tuple + (i,)
                if c[index] > 1
                else out_tuple
            )
            for index
            in indices
            for out_tuple
            in prev_outcome[index]
        )
        for i, indices
        in enumerate(indices_list)
    ]
    return Outcome(nested)
   
