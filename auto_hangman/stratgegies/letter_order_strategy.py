
from ..strategy_abc import StrategyAbstractClass
from ..data_abc import DataLoaderClassType
from collections import defaultdict


class LetterOrderStrategy(StrategyAbstractClass):

    def __init__(self):
        self.predict_list: list = []   # letter list

    def start_train(self, data: DataLoaderClassType):
        self.predict_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def print_model(self):
        total_count = sum(self.model.values())
        print("=================")
        print("predict_list:", self.predict_list)
        print("=================")

    def get_frequently_letters(self):
        return self.predict_list

    def predict(self, pattern: str, used_letters: list = []):
        if '_' not in pattern:
            return None

        for letter in self.get_frequently_letters():
            if letter in used_letters:
                continue
            return letter

        raise Exception("Invalied letter")
