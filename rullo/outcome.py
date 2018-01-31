
class Outcome:
    def __init__(self, variants=None):
        self._variants = (
            set(variants)
            if variants
            else set()
        )

    @classmethod
    def from_state_set(cls, state_set):
        return Outcome({
            (index,)
            for index
            in range(len(state_set))
        })
    
    def __repr__(self):
        return '<Outcome {}>'.format(self._variants)
        
    def __eq__(self, other):
        return self._variants == other._variants
        