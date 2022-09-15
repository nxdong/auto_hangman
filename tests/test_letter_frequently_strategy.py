from auto_hangman import LetterFrequentlyStrategy
from auto_hangman import TextLoader


def test_letter_frequently():
    file_path = 'tests/data/top3000.txt'
    loader = TextLoader(file_path)

    strategy = LetterFrequentlyStrategy()
    strategy.start_train(loader)
    
    strategy.print_model()

    top10 = ['e', 'i', 't', 'r', 'a', 'n', 'o', 's', 'l', 'c']

    assert top10 == strategy.get_frequently_letters()[:10]


