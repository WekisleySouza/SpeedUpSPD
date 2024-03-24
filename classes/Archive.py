from math import ceil
import os

class Archive:
    def __init__(self, name) -> None:
        self.__name = name
        self.__content = None
        self.__parts = []

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def content(self) -> str:
        return self.__content
    
    @property
    def parts(self) -> str:
        return self.__parts

    def read(self) -> None: # Define vetor em que cada posição é uma palavra
        with open(self.__name, 'r') as file:
            self.__content = file.read().split()

    def split(self, parts_number) -> None: # Divide o livro em um número de partes
        if (self.__content): # Vê se já leu o livro
            self.__parts = []
            parts_length = ceil(len(self.__content) / parts_number)
            start = 0

            for i in range(parts_number):
                if i < parts_number:
                    self.__parts.append(self.__content[start:start + parts_length])
                else:
                    self.__parts.append(self.__content[start:])
                start += parts_length
        else:
            print('Você deve chamar o read antes!')

    def delete_files_in(path) -> None:
        files = os.listdir(path) # Lista os arquivos em um caminho
        
        for file in files:
            file_path = os.path.join(path, file) # Junta o caminho com o nome do arquivo

            if os.path.isfile(file_path):
                os.remove(file_path) # Revove o arquivo