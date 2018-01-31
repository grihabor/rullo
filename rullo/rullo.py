import numpy as np
import csv

from rullo.solver import iter_valid_states
from rullo.state_set import StateSet


class Rullo:
    def __init__(self,
                 content,
                 row_constraints,
                 column_constraints,
                 state=None):
        """Creates a rullo board

        Attributes
        ----------
        content: 2-dim array
            Values on the board
        row_constraints: 1-dim array
            Array of constraints on rows

            row_constraints.shape[0] == content.shape[0]
        column_constraints: 1-dim array
            Array of constraints on columns

            column_constraints.shape[0] == content.shape[1]
        """
        self.content = np.asarray(content, dtype=np.int)
        self.row_constraints = np.asarray(row_constraints, dtype=np.int)
        self.column_constraints = np.asarray(column_constraints, dtype=np.int)
        self.state = (
            np.zeros(content.shape, dtype=np.bool)
            if not state
            else np.asarray(state, dtype=np.bool)
        )

    @classmethod
    def from_csv(cls, f):
        reader = csv.reader(f)
        column_constraints = np.array(next(reader), dtype=np.int)
        row_constraints = np.array(next(reader), dtype=np.int)

        content_shape = row_constraints.shape + column_constraints.shape
        content = np.zeros(content_shape, dtype=np.int)
        for i, line in enumerate(reader):
            row = np.array(line, dtype=np.int)
            content[i, :] = row

        return cls(content,
                   row_constraints,
                   column_constraints)
    
    def solve(self):
        self.state = _solve_board(self)
        return self


def _all_state_sets(content, constraints):
    return [
        StateSet(iter_valid_states(row, constraint))
        for row, constraint
        in zip(content, constraints)
    ]


def _solve_board(rullo: Rullo):
    state_storage = [
        _all_state_sets(rullo.content, rullo.row_constraints),
        _all_state_sets(np.transpose(rullo.content), rullo.column_constraints)
    ]

