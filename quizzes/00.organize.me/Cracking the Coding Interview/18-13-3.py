'''
백만 개의 단어 목록이 주어졌을 때, 각 단어의 글자들을 사용하여 만들 수 있는 최대 크기 직사각형을 구하는 알고리즈을 설계하라. 이 정사각형의 각 행은 하나의 단어여야 하고(왼쪽에서 오른쪽 방향). 리스트에서 단어를 선정할 때 연속된 단어를 선정할 필요는 없다. 모든 행의 길이는 서로 같아야 하고, 모든 열의 길이도 서로 같아야 한다.
'''
import datetime

perm_dict = {}

WORD_LIST = []
with open('english_dictionary.txt', 'r', encoding="ISO-8859-1") as fp:
    WORD_LIST = fp.read().splitlines()
    WORD_LIST = [word.lower() for word in WORD_LIST]
    WORD_LIST = list(set(WORD_LIST))
    WORD_LIST.sort(key = lambda x: (len(x), x))

print('done sorting word_list')
print('words length ranges from {} to {}'.format(len(WORD_LIST[0]), len(WORD_LIST[-1])))

def main(word_list):
    for words in get_words_by_same_length(word_list):
        if len(words[0]) in [30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15]:
        #if len(words[0]) in range(14):
            continue
        #print('words', words)
        print('starting time', datetime.datetime.now())
        print('trying words of length, {}({})'.format(len(words[0]), len(words)))
        if not is_satisfied_requirement(words):
            continue
        matrix = make_words_matrix(words)
        if matrix:
            yield matrix

def is_satisfied_requirement(words):
    word_length = len(words[0])
    count = len(words)
    if word_length * 2 <= count:
        return True
    else:
        return False
    
def get_words_by_same_length(word_list):
    words_by_same_length = []

    first_word = word_list[0]
    word_length = len(first_word)
    words = [first_word]
    for word in word_list[1:]:
        if len(word) == word_length:
            words.append(word)
        else:
            words_by_same_length.append(words)
            word_length = len(word)
            words = [word]
    words_by_same_length.append(words)
    
    #내림차순
    for words in words_by_same_length[:0:-1]:
    #오름차순
    #for words in words_by_same_length[1:]:
        #[' ']가 존재해 에러나므로.
        yield words

def make_words_matrix(words):
    #print('words', words)
    assert len(words) >= len(words[0])*2
    from itertools import permutations
    from math import floor, log
    pivot_len = floor(log(len(words[0])))
    if pivot_len == 0:
        pivot_len = 1
    total_try_count = get_permutations_count(len(words), pivot_len)
    trial = 0
    for pivot_tuple in permutations(words, pivot_len):
        trial += 1
        proceed = 100 * trial / total_try_count
        print("%0.5f" % proceed, '%', end='\r')

        #print('pivot_tuple', pivot_tuple)
        for chosens in get_candidates(pivot_tuple, words, proceed):
            #print('chosens:', chosens)
            if is_correct(chosens, words):
                return chosens
    else:
        return None

def get_permutations_count(n, r):
    assert n>=r
    if (n,r) in perm_dict:
        return perm_dict[(n,r)]
    else:
        result = 1
        for i in range(r):
            result *= (n-i)
        perm_dict[(n,r)] = result
        return result

def get_candidates(pivot_tuple, words, outer_progress):
    nested_list = []
    for c_tuple in zip(*pivot_tuple):
        nested_list.append(get_word_list_that_startswith(c_tuple, words, excludes=pivot_tuple))

    from itertools import product
    from functools import reduce
    total_try_count = reduce(lambda x,y: x*y, [len(each) for each in nested_list])
    trial = 0
    for each_combi in product(*nested_list):
        if are_words_unique(each_combi):
            yield each_combi
        trial += 1
        proceed = 100 * trial / total_try_count
        print('%0.5f' % outer_progress, '%', '-', "%0.5f" % proceed, '%', end='\r')

def get_word_list_that_startswith(c_tuple, words, excludes=()):
    assert isinstance(excludes, tuple)
    result = []
    for word in words:
        if word in excludes:
            continue
        starting_word = ''.join(c_tuple)
        if word.startswith(starting_word):
            result.append(word)
    return result

def are_words_unique(words):
    assert isinstance(words, tuple)
    from collections import Counter
    for word, cnt in Counter(words).items():
        if cnt > 1:
            return False
    return True


def is_correct(word_list, words):
    #print(word_list, words)
    assert len(word_list) == len(word_list[0])
    first_word = word_list[0]
    
    col_words = []
    for col in range(len(first_word)):
        col_word = ''
        for word in word_list:
            col_word += word[col]
        if col_word not in words:
            return False
    return True

print('START TIME', datetime.datetime.now())
the_matrix= main(WORD_LIST)
for matrix in the_matrix:
    print('FOUND!')
    for word in matrix:
        print(word)
    print('')
print('END TIME', datetime.datetime.now())
