from auto_hangman import TextLoader

def test_text_loader():
    file_path = 'tests/data/top3000.txt'
    loader = TextLoader(file_path)
    assert 3000 == len(loader)
    
    # test iterator
    target = []
    for w in loader[:10]:
        target.append(w)
    
    assert target == loader[:10]
    
    # test get
    assert 'happy' == loader[1230]
    
