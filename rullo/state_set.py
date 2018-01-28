
class StateSet:
    def __init__(self, states):
        self._states = np.asarray(states, dtype=bool)
        
        