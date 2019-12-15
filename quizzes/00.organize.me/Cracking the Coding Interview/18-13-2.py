'''
백만 개의 단어 목록이 주어졌을 때, 각 단어의 글자들을 사용하여 만들 수 있는 최대 크기 직사각형을 구하는 알고리즈을 설계하라. 이 정사각형의 각 행은 하나의 단어여야 하고(왼쪽에서 오른쪽 방향). 리스트에서 단어를 선정할 때 연속된 단어를 선정할 필요는 없다. 모든 행의 길이는 서로 같아야 하고, 모든 열의 길이도 서로 같아야 한다.
'''
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
    for words in words_by_same_length[::-1]:
    #오름차순
    #for words in words_by_same_length:
        yield words

def make_words_matrix(words):
    assert len(words) >= len(words[0])*2
    for pivot1 in words:
        for chosens in get_candidates(pivot1, words):
            if is_correct(chosens, words):
                assert pivot1 not in chosens
                return chosens
    else:
        return None

def get_candidates(pivot1, words):
    nested_list = []
    for c1 in pivot1:
        nested_list.append(get_word_list_that_startswith(c1, words, excludes=[pivot1]))

    from itertools import product
    for each_combi in product(*nested_list):
        if are_words_unique(each_combi):
            yield each_combi

def get_word_list_that_startswith(c1, words, excludes=[]):
    assert isinstance(excludes, list)
    result = []
    for word in words:
        if word not in excludes and word.startswith(c1):
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

import datetime
print(datetime.datetime.now())
the_matrix= main(WORD_LIST)
for matrix in the_matrix:
    print('FOUND!')
    for word in matrix:
        print(word)
    print('')
print(datetime.datetime.now())
