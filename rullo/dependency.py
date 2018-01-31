from .outcome import Outcome
from .state_set import StateSet


class Dependency:
    def __init__(self, state_set, index_pair, outcome):
        assert isinstance(state_set, StateSet)
        assert isinstance(outcome, Outcome)

        self.state_set = state_set
        self.index_pair = index_pair
        self.outcome = outcome

    def __repr__(self):
        return '<Dependency[{}, {}, {}]>'.format(
            self.state_set,
            self.index_pair,
            self.outcome,
        )

