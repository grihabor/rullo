
class Outcome:
    def __init__(self, variants=None):
        self._variants = (
            variants
            if variants
            else []
        )
