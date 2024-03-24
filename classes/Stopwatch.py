from time import time

class Stopwatch:
    def __init__(self, time=0) -> None:
        self.__time = time

    @property
    def time(self):
        return float(self.__time)

    def start(self):
        self.__time = time()
    
    def finish(self):
        self.__time = time() - self.__time