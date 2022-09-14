from ..data_abc import DataLoaderAbstractClass

class TextLoader(DataLoaderAbstractClass):
    
    def __init__(self, file_path: str):
        with open(file_path, 'r') as f:
            lines = f.read()
        self.words = lines.split()
    
