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
    if word not in rainbow_table:
        rainbow_table[word] = True
print('Done!')
assert 'dog' in rainbow_table


def recursive(broken_sentence):
    if not broken_sentence:
        return [[]]

    result = []
    candidates = get_candidates(broken_sentence)
    for candidate in candidates:
        word, rest = candidate
        for each in recursive(rest):
            tmp = [word]
            tmp.extend(each)
            result.append(tmp)
    return result

def get_candidates(sentence):
    yield (sentence[:1].upper(), sentence[1:])
    for i in range(1, len(sentence)+1):
        word = sentence[:i]
        rest = sentence[i:] #성능상은 if절 안으로 보내는게 남.
        if word in rainbow_table:
            yield (word, rest)

def concat_capitals_together(words):
    on_capital = False
    range_list = []

    for i, word in enumerate(words):
        if word.isupper() and not on_capital:
            on_capital = True
            start_idx = i
        elif word.isupper() and on_capital:
            if i==(len(words)-1):
                range_list.append((start_idx, len(words)))
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


broken_sentence = input('input a broken sentence: ')
#broken_sentence = 'ilovejinsungheleftthismorning'
#broken_sentence = 'jesslookedjustliketimherbrother'
#broken_sentence = 'dog'
result = recursive(broken_sentence)
sentences = []
for each_list in result:
    #assert isinstance(each, list)
    each_list = concat_capitals_together(each_list)
    sentence = ' '.join(each_list)
    sentences.append(sentence)
    
print('numbers of sentences : {}'.format(len(sentences)))
def lesser_capitals(sentence):
    count = 0
    for c in sentence:
        if c.isupper():
            count +=1
    return count, sentence.count(' ')

sentence_in_order = sorted(sentences, key = lesser_capitals)
#print(sentence_in_order)
print('restored sentence :',sentence_in_order[:1])

for stc in sentence_in_order:
    if 'brother' in stc:
        print('found')
        print(stc)
        import sys
        sys.exit(0)
print('not found')
