# Auto Hangman

LetterFrequentlyStrategy average guess times: 16.044  

LetterOrderStrategy average guess times: 20.156

## development

```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
# or use aliyun
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

run test

```bash
make test
```

## run

``` bash
make test 
```

output:

```bash
pytest -s
========================= test session starts ========================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/sss/code/py/auto_hangman
collected 7 items                                                                                                                                                                         

tests/test_autohang.py ...LetterFrequentlyStrategy average times: 16.044666666666668
.LetterOrderStrategy average times: 20.156
.
tests/test_letter_frequently_strategy.py =================
Total Count: 19218
Model: [('e', 2467), ('i', 1558), ('t', 1542), ('r', 1493), ('a', 1491), ('n', 1381), ('o', 1308), ('s', 1123), ('l', 990), ('c', 901), ('p', 614), ('u', 584), ('d', 581), ('m', 529), ('h', 471), ('g', 419), ('y', 393), ('f', 331), ('b', 279), ('v', 268), ('w', 204), ('k', 140), ('x', 64), ('j', 34), ('q', 33), ('z', 20)]
List Model: [('e', 2467), ('i', 1558), ('t', 1542), ('r', 1493), ('a', 1491), ('n', 1381), ('o', 1308), ('s', 1123), ('l', 990), ('c', 901), ('p', 614), ('u', 584), ('d', 581), ('m', 529), ('h', 471), ('g', 419), ('y', 393), ('f', 331), ('b', 279), ('v', 268), ('w', 204), ('k', 140), ('x', 64), ('j', 34), ('q', 33), ('z', 20)]
predict_list: ['e', 'i', 't', 'r', 'a', 'n', 'o', 's', 'l', 'c', 'p', 'u', 'd', 'm', 'h', 'g', 'y', 'f', 'b', 'v', 'w', 'k', 'x', 'j', 'q', 'z']
=================
.
tests/test_loader.py .

================== 7 passed in 0.48s =============
```


## reference

words from:
https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/    

