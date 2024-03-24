from classes.Archive import Archive
from classes.Report import Report
from classes.ParalellTest import ParalellTest
from classes.SequencialTest import SequencialTest

class Homework:
    def __init__(self) -> None:
        self.__file = None

    def get_book(self) -> None: # Lê o livro e o armazena em uma lista
        Archive.delete_files_in('./reports')
        self.__file = Archive('./book/Hamlet.txt')
        self.__file.read()

    def run_paralell_test(self, number_of_threads, number_of_executions) -> None:
        self.__file.split(number_of_threads) # Divide o livro em um certo número de partes

        paralell_test = ParalellTest(self.__file.parts)
        paralell_test.run(number_of_executions) # Roda um número de vezes o teste

        paralell_report = Report(paralell_test.times, f'teste_paralelo_{number_of_threads}_threads')
        paralell_report.generate_times_report()

    def run_sequencial_test(self, number_of_executions) -> None:
        sequencial_test = SequencialTest(self.__file.content)
        sequencial_test.run(number_of_executions)

        sequencial_report = Report(sequencial_test.times, 'teste_sequencial')
        sequencial_report.generate_times_report()

    def compare_results(self) -> None:
        Report.generate_speedup_report()