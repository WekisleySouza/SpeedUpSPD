from classes.Stopwatch import Stopwatch

class Test:
    def __init__(self, list) -> None:
        self._times = []
        self._list = list

    @property
    def times(self) -> list: # Retorna lista com os tempos no tipo float
        return [timer.time for timer in self._times]

    def _count_positions(self, list) -> None:
            stopwatch = Stopwatch()
            stopwatch.start()
            len(list)
            stopwatch.finish()
            self._times.append(stopwatch)