class FiniteStateMachine(object):
    def __init__(self, data):
        self._alphabet = data.alphabet
        self._states = data.states
        self._state = 0
        pass

    def execute(self, word: str) -> bool:
        for symbol in word:
            self._set_state(symbol)

        return self.is_ending_state(self.state)

    def _set_state(self, symbol: str):
        self._state = self._states[self.state]['relations'][symbol]

    @property
    def state(self) -> int:
        return self._state

    def is_ending_state(self, state: int) -> bool:
        return state in self._states.keys() and self._states[state]['ended']



