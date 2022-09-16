from auto_hangman import get_word_pattern
from auto_hangman import guess_next_letter
from auto_hangman import TextLoader
from auto_hangman import LetterFrequentlyStrategy
from auto_hangman import LetterOrderStrategy


def help_get_predict_times(word, words_data):
    used_letters = []
    pattern = get_word_pattern(word, used_letters)
    guess_time = 0
    while '_' in pattern:
        guess_time += 1

        new_letter = guess_next_letter(pattern, used_letters, words_data)
        if new_letter == None:
            print("Word is already guessed or something wrong.")
            break

        used_letters.append(new_letter)
        pattern = get_word_pattern(word, used_letters)

    # print("Word: {} guess {} times.".format(word, guess_time))
    return guess_time


def help_get_predict_times_by_strategy(word, strategy):
    used_letters = []
    pattern = get_word_pattern(word, used_letters)
    guess_time = 0
    while '_' in pattern:
        guess_time += 1
        new_letter = strategy.predict(pattern, used_letters)
        if new_letter == None:
            print("Word is already guessed or something wrong.")
            break

        used_letters.append(new_letter)
        pattern = get_word_pattern(word, used_letters)

    # print("Word: {} guess {} times.".format(word, guess_time))
    return guess_time


def test_get_word_pattern():
    word = 'apple'
    used_letters = ['m']
    pattern = get_word_pattern(word, used_letters)
    assert '_____' == pattern

    used_letters = ['a']
    pattern = get_word_pattern(word, used_letters)
    assert 'a____' == pattern

    used_letters = ['p']
    pattern = get_word_pattern(word, used_letters)
    assert '_pp__' == pattern

    used_letters = ['a', 'p']
    pattern = get_word_pattern(word, used_letters)
    assert 'app__' == pattern

    used_letters = ['a', 'p', 'l']
    pattern = get_word_pattern(word, used_letters)
    assert 'appl_' == pattern

    used_letters = ['a', 'p', 'l', 'e']
    pattern = get_word_pattern(word, used_letters)
    assert 'apple' == pattern

    used_letters = ['a', 'b', 'p', 'l', 'e']
    pattern = get_word_pattern(word, used_letters)
    assert 'apple' == pattern


def test_guess_next_letter():
    file_path = 'tests/data/top3000.txt'
    loader = TextLoader(file_path)
    assert 3000 == len(loader)

    pattern = "a__le"
    used_letters = ['a', 'l', 'e']
    next_letter = guess_next_letter(pattern, used_letters, loader)
    assert 'i' == next_letter

    pattern = "apple"
    used_letters = []
    next_letter = guess_next_letter(pattern, used_letters, loader)
    assert None == next_letter

    pattern = "_"
    used_letters = []
    next_letter = guess_next_letter(pattern, used_letters, loader)
    assert 'e' == next_letter

    pattern = "_"
    used_letters = ['e']
    next_letter = guess_next_letter(pattern, used_letters, loader)
    assert 'i' == next_letter


def test_auto_hangman():
    file_path = 'tests/data/top3000.txt'
    loader = TextLoader(file_path)
    assert 3000 == len(loader)

    word = 'eit'
    guess_times = help_get_predict_times(word, loader)
    assert 3 == guess_times

    word = 'apple'
    guess_times = help_get_predict_times(word, loader)
    assert 11 == guess_times

    word = 'a'
    guess_times = help_get_predict_times(word, loader)
    assert 5 == guess_times

    word = 'z'
    guess_times = help_get_predict_times(word, loader)
    assert 26 == guess_times


def test_LetterFrequentlyStrategy_average_times():
    file_path = 'tests/data/top3000.txt'
    loader = TextLoader(file_path)
    assert 3000 == len(loader)
    strategy = LetterFrequentlyStrategy()
    strategy.start_train(loader)
    # strategy.print_model()
    total_times = 0

    for word in loader:
        total_times += help_get_predict_times_by_strategy(word, strategy)

    average_times = total_times / len(loader)
    print("LetterFrequentlyStrategy average times:", average_times)
    assert 16 == int(average_times)


def test_LetterOrderStrategy_average_times():
    file_path = 'tests/data/top3000.txt'
    loader = TextLoader(file_path)
    assert 3000 == len(loader)
    strategy = LetterOrderStrategy()
    strategy.start_train(loader)
    # strategy.print_model()
    total_times = 0

    for word in loader:
        total_times += help_get_predict_times_by_strategy(word, strategy)

    average_times = total_times / len(loader)
    print("LetterOrderStrategy average times:", average_times)
    assert 20 == int(average_times)
