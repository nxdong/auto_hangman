from auto_hangman import LetterFrequentlyStrategy
from auto_hangman import TextLoader


def test_letter_frequently():
    file_path = 'tests/data/top3000.txt'
    loader = TextLoader(file_path)
    
    strategy = LetterFrequentlyStrategy()
    strategy.start_train(loader)