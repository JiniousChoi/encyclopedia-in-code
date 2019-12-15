'''
17.14 - 구둣점이 없어진 문장을 최대한 복원하라.
'''

WORD_LIST = []
with open('english_dictionary.txt', 'r', encoding="ISO-8859-1") as fp:
    WORD_LIST = fp.read().splitlines()
    WORD_LIST = [word.lower() for word in WORD_LIST]
    WORD_LIST = list(set(WORD_LIST))
    _WORD_LIST = []
    for word in WORD_LIST:
        for ch in word:
            if not ch in 'abcdefghijklmnopqrstuvwxyz':
                continue
        _WORD_LIST.append(word)
    WORD_LIST = _WORD_LIST
    WORD_LIST.sort(key = lambda x: (len(x), x))

print('done sorting word_list')
print('words length ranges from {} to {}'.format(len(WORD_LIST[0]), len(WORD_LIST[-1])))

print('Creating rainbow_table')
rainbow_table = {}
for word in WORD_LIST:
    for i in range(len(word)):
        key = word[:i+1]
        if key not in rainbow_table:
            rainbow_table[key] = True
print('Done!')

def restore_naive(sentence):
    words = []
    i,j = 0,1

    while i<len(sentence):
        i,j = find_word_in_sentence(sentence,i,j,words)
    words = concat_capitals_together(words)
    new_sentence = ' '.join(words)
    return new_sentence

def find_word_in_sentence(sentence, i, j, words):
    assert i < len(sentence)
    while j<=len(sentence) and sentence[i:j] in rainbow_table:
        j+=1
    word = sentence[i:j-1]
    if word in WORD_LIST:
        words.append(word)
    else:
        words.append(word.upper())

    i = j - 1
    #j = j
    return i, j

def concat_capitals_together(words):
    on_capital = False
    range_list = []

    for i, word in enumerate(words):
        if word.isupper() and not on_capital:
            on_capital = True
            start_idx = i
        elif word.isupper() and on_capital:
            if i==(len(words)-1):
                range_list.append(start_idx, len(words))
        elif not word.isupper() and on_capital:
            on_capital=False
            end_idx = i
            range_list.append((start_idx, end_idx))
        elif not word.isupper() and not on_capital:
            pass
        else:
            assert False

    #range_list is prepared
    for i,j in range_list[::-1]:
        words[i:j] = [''.join(words[i:j])]
    return words


#broken_sentence = 'ilovejinsungheleftthismorning'
broken_sentence = 'jesslookedjustliketimherbrother'
print(restore_naive(broken_sentence))
