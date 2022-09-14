
from ..strategy_abc import StrategyAbstractClass
from ..data_abc import DataLoaderClassType
from collections import defaultdict


class LetterFrequentlyStrategy(StrategyAbstractClass):

    def __init__(self):
        self.model = defaultdict(int)  # letter count
        self.list_model: list = []     # model sort by value
        self.predict_list: list = []   # letter list

    def start_train(self, data: DataLoaderClassType):
        for word in data:
            for letter in word:
                if letter.isalpha():
                    self.model[letter.lower()] += 1
        print(self.model)
        self.list_model = sorted(self.model.items(),
                                 key=lambda x: x[1], reverse=True)
        self.predict_list = list(map(lambda x: x[0], self.list_model))
        self.print_model()

    def print_model(self):
        total_count = sum(self.model.values())
        print("=================")
        print("Total Count:", total_count)
        print("Model:", self.list_model)
        print("List Model:", self.list_model)
        # new_percent_list = list(
        #     map(lambda x: (x[0], x[1]/total_count), self.list_model))
        # print("letter percent:", new_percent_list)
        print("predict_list:", self.predict_list)
        print("=================")

    def get_frequently_letter(self):
        return self.predict_list
