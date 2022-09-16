from .data_loaders import TextLoader
from .stratgegies import LetterFrequentlyStrategy
from .stratgegies import LetterOrderStrategy


def guess_next_letter(pattern, used_letters=[], word_list=['about', 'abound', ...]):
    """Returns a letter from the alphabet.
    Input parameters:
            pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """

    strategy = LetterFrequentlyStrategy()
    strategy.start_train(word_list)
    # strategy.print_model()
    return strategy.predict(pattern, used_letters)



def get_word_pattern(word: str, used_letters=[]) -> str:
    '''get word patten'''
    letters = set(used_letters)
    pattern = list(word)
    for idx in range(len(word)):
        # skip no alpha letter
        if not pattern[idx].isalpha():
            continue
        # replace letter not in set
        if pattern[idx].lower() not in letters:
            pattern[idx] = '_'

    return ''.join(pattern)
