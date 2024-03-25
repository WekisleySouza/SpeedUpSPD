from threading import Thread

class MyThread(Thread):
    def __init__(self, name, func, *kw_args) -> None:
        super().__init__()
        self.__name = name
        self.__func = func
        self.__kw_args = kw_args

    def run(self) -> None:
        print(f"Thread: {self.__name} começou!")
        self.__func(*self.__kw_args)
        print(f"Thread: {self.__name} acabou!")
