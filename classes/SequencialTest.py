from classes.Test import Test
from time import sleep

class SequencialTest(Test):
    def __init__(self, list_of_words) -> None:
        super().__init__(list_of_words)

    def run(self, number_of_tests=1) -> None:
        for _ in range(number_of_tests):
            super()._count_positions(self._list)
            sleep(1) # Resolve problema dos tempos zerados