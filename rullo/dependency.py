from .outcome import Outcome
from .state_set import StateSet


class Dependency:
    def __init__(self, state_set, index_pair, outcome):
        assert isinstance(state_set, StateSet)
        assert isinstance(outcome, Outcome)

        self.state_set = state_set
        self.index_pair = index_pair
        self.outcome = outcome

