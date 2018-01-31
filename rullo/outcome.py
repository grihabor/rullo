
class Outcome:
    def __init__(self, variants=None):
        self._variants = (
            variants
            if variants
            else []
        )

    @classmethod
    def from_state_set(state_set):
        return Outcome([
            (index,)
            for index
            in range(len(state_set))
        ])
