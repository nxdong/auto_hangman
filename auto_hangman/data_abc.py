from abc import ABC
import typing


class DataLoaderAbstractClass(ABC):
    def __init__(self):
        self.words: typing.List[str] = []

    def __len__(self):
        return len(self.words)

    def __iter__(self):
        return self.DataIterator(self)

    def __getitem__(self, item) -> str:
        return self.words[item]

    class DataIterator:
        def __init__(self, words):
            self.__words = words
            self.__index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index >= len(self.__words):
                raise StopIteration

            # return the next word
            word = self.__words.words[self.__index]
            self.__index += 1
            return word


DataLoaderClassType = typing.TypeVar(
    'DataLoaderClassType', bound='DataLoaderAbstractClass')
