from classes.Test import Test
from classes.MyThread import MyThread
from classes.Stopwatch import Stopwatch

from time import sleep

class ParalellTest(Test):
    def __init__(self, list_of_parts) -> None:
        super().__init__(list_of_parts)

    def organize_times(self) -> None:
        new_times = []
        current_time = 0
        for i, timer in enumerate(self._times):
            if timer.time > current_time: 
                current_time = timer.time
         
            if (i + 1) % len(self._list) == 0:
                new_times.append(Stopwatch(current_time))
                current_time = 0

        self._times = new_times

    def run(self, number_of_tests=1) -> None:
        for i in range(number_of_tests): # Para cada um dos 30 testes
            for part in self._list: # Para cada parte do livro
                thread = MyThread(i, super()._count_positions, part) # Params = (nome_da_thread, função_a_ser_executada, parâmetros_da_função)
                thread.start()
            sleep(1) # Para separar as threads das 30 execuções
        self.organize_times() # Vai fazer a soma dos tempos de cada thread em uma contagem
