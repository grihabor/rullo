import numpy as np


def is_line_valid(content, state, constraint):
    """Checks if line is valid
    
    Attributes
    ----------
    line: 1-dim array
        Line content
    state: 1-dim array
        Line state
    constraint: int
    """
    return np.sum(content * state) == constraint


class Rullo:
    def __init__(self, content, constraints):
        """Creates a rullo board
        
        Attributes
        ----------
        content: 2-dim array
            Values on the board
        constraints: 2 stacked 1-dim arrays
            Constraints on rows and columns
            constraints[0] is the rows constraints
            constraints[1] is the columns constraints
 
        """
        self.content = content
        self.constraints = constraints
        
        