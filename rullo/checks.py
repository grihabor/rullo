import numpy as np
import csv


def is_line_valid(content,
                  state,
                  constraint):
    """Checks if line is valid

    Attributes
    ----------
    content: 1-dim array
        Line content
    state: 1-dim array
        Line state

        state.shape == content.shape
    constraint: int
    """
    return np.sum(content * state) == constraint


def is_board_valid(content,
                   state,
                   row_constraints,
                   column_constraints):
    """Checks if board is valid

    Attributes
    ----------
    content: 2-dim array
        Line content
    state: 2-dim array
        Line state

        state.shape == content.shape
    row_constraints: 1-dim array
        Array of constraints on rows

        row_constraints.shape[0] == content.shape[0]
    column_constraints: 1-dim array
        Array of constraints on columns

        column_constraints.shape[0] == content.shape[1]
    """
    assert content.shape == state.shape
    assert row_constraints.shape[0] == content.shape[0]
    assert column_constraints.shape[0] == content.shape[1]

    values = content * state
    return all([
        np.all(np.sum(values, axis=1) == row_constraints),
        np.all(np.sum(values, axis=0) == column_constraints),
    ])


