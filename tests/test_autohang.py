from auto_hangman import get_word_patten


def help_get_predict_times(word, words_data):
    guess_next_letter()


def test_get_word_patten():
    word = 'apple'
    used_letters = ['m']
    patten = get_word_patten(word, used_letters)
    assert '_____' == patten

    used_letters = ['a']
    patten = get_word_patten(word, used_letters)
    assert 'a____' == patten

    used_letters = ['p']
    patten = get_word_patten(word, used_letters)
    assert '_pp__' == patten

    used_letters = ['a', 'p']
    patten = get_word_patten(word, used_letters)
    assert 'app__' == patten

    used_letters = ['a', 'p', 'l']
    patten = get_word_patten(word, used_letters)
    assert 'appl_' == patten

    used_letters = ['a', 'p', 'l', 'e']
    patten = get_word_patten(word, used_letters)
    assert 'apple' == patten

    used_letters = ['a', 'b', 'p', 'l', 'e']
    patten = get_word_patten(word, used_letters)
    assert 'apple' == patten


def test_auto_hangman():
    word = 'apple'