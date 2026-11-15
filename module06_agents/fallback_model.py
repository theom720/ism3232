# fallback_model.py
# Author: Theo Major


class FallbackModel:
    """Try one model, then another if the first has no answer."""

    def __init__(self, first, second):
        """Store the two models to try, in order."""
        self.first = first
        self.second = second

    def decide(self, instructions, history, tools):
        """Ask the first model. If it returns None, ask the second."""
        decision = self.first.decide(instructions, history, tools)
        if decision is None:
            return self.second.decide(instructions, history, tools)
        return decision
