m = {
    "alphabet": [
        '0',
        '1'
    ],
    "states": {
        0: {
            "ended": False,
            "relations": {
                '0': 1,
                '1': 0
            }
        },
        1: {
            "ended": True,
            "relations": {
                '0': 1,
                '1': -1
            }
        }
    }
}


class FiniteStateMachine(object):
    def __init__(self, data):
        self._alphabet = data['alphabet']
        self._states = data['states']
        self._state = 0

    def execute(self, word: str) -> bool:
        for symbol in word:
            self._set_state(symbol)

            if self.state < 0:
                break

        return self.is_ending_state(self.state)

    def _set_state(self, symbol: str):
        self._state = self._states[self.state]['relations'][symbol]

    @property
    def state(self) -> int:
        return self._state

    def is_ending_state(self, state: int) -> bool:
        return state in self._states.keys() and self._states[state]['ended']


a = FiniteStateMachine(m)

print(a.execute('11100000001'))
