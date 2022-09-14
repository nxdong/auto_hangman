from abc import ABC
from .data_abc import DataLoaderClassType

class StrategyAbstractClass(ABC):
    '''Model train interface'''
    
    def __init__(self) -> None:
        pass
    
    def start_train(self, data: DataLoaderClassType):
        pass
    
    def save_model(self, model_path):
        pass
    
    def load_model(self, model_path):
        pass
    
    def predict(self, input, used):
        pass