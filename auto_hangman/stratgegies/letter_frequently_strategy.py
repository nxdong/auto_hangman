
from ..strategy_abc import StrategyAbstractClass
from ..data_abc import DataLoaderClassType

class LetterFrequentlyStrategy(StrategyAbstractClass):
    
    def __init__(self):
        self.model = {}
    
    def start_train(self, data: DataLoaderClassType):
        for word in data:
            print(word)
            
    