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
        key = (len(word), word[:i+1])
        if key in rainbow_table:
            rainbow_table[key].append(word)
        else:
            rainbow_table[key] = [word]
print('Done!')

from collections import Counter
def main(word_list):
    for words in get_words_by_same_length(word_list):
        #if len(words[0]) not in [10]:
        if len(words[0]) not in [9,8,7,6]:
            continue
        print('starting time', datetime.datetime.now())
        print('trying words of length, {}({})'.format(len(words[0]), len(words)))
        if not is_satisfied_requirement(words):
            continue

        words_cnt = len(words)
        since = datetime.datetime.now()
        for i, word in enumerate(words):
            #if i <= 8540:#skipping ahead
            #    continue
            init_pivot = [word]
            make_words_matrix(init_pivot, words)
            after = datetime.datetime.now()
            print_progress(i+1, words_cnt, since, after)

def print_progress(x, X, since, after):
    diff = after - since
    total_seconds = diff.total_seconds() * (X/x - 1)

    minute = total_seconds // 60
    second = total_seconds % 60

    hour = minute // 60
    minute = minute % 60

    day = hour // 24
    hour = hour % 24

    count_down = "{}:{}:{}:{}".format(int(day), int(hour), int(minute), int(second))
    print("%0.5f"%(100*x/X), '%', count_down, end='\r')
    
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
    #for words in words_by_same_length[3:]:
        #[' ']가 존재해 에러나므로.
        yield words

def make_words_matrix(pivots, words, depth=0):
    #import pdb; pdb.set_trace()
    #print(pivots)
    if DEBUG:
        assert isinstance(pivots, list)
        assert len(words) >= len(words[0])*2

    word_len = len(words[0])
    if DEBUG:
        assert len(pivots) <= word_len

    if len(pivots) == word_len:
        print('final quest')
        if is_success(pivots, words):
            print(pivots)
            #yield pivots
        else:
            print('failed...so sorry')

    else:
        #recursive part
        for word in words:
            if word in pivots:
                continue

            #print(word)
            new_pivots = pivots[:]
            new_pivots.append(word)
            pre_list, candidates_list = get_candidates_list(new_pivots, words)
            if candidates_list:
                if is_worth_throttling(pre_list, candidates_list):
                    print('depth({}) - its worth!'.format(depth))
                    make_words_matrix(new_pivots, words, depth+1)


def get_candidates_list(pivots, words):
    prefix_list = [''.join(ch_list) for ch_list in zip(*pivots)]
    candidates_list = []

    word_len = len(words[0])
    for prefix in prefix_list:
        try:
            candidates = rainbow_table[(word_len, prefix)]
        except KeyError:
            return [prefix_list, None]
        candidates_list.append(candidates)
    return [prefix_list, candidates_list]


def is_worth_throttling(prefix_list, candidates_list):
    if DEBUG:
        assert len(prefix_list) == len(candidates_list)

    i=0
    for prefix, cnt in Counter(prefix_list).items():
        if cnt > len(candidates_list[i]):
            return False
        i+=1
    return True

def get_permutations_count(n, r):
    if DEBUG:
        assert n>=r
    if (n,r) in perm_dict:
        return perm_dict[(n,r)]
    else:
        result = 1
        for i in range(r):
            result *= (n-i)
        perm_dict[(n,r)] = result
        return result

def is_success(pivots, words):
    for pivot in pivots:
        if pivot not in words:
            return False

    new_words = [''.join(ch_list) for ch_list in zip(*pivots)]
    for new_word in new_words:
        if new_word not in words:
            return False
    print('Success')
    return True
    

#make_words_matrix(['abc','air','hoc'], ['abc','air','hoc','aah','bio','crc'])

DEBUG = False
print('START TIME', datetime.datetime.now())
the_matrix= main(WORD_LIST)
#for matrix in the_matrix:
#    print('FOUND!')
#    for word in matrix:
#        print(word)
#    print('')
print('END TIME', datetime.datetime.now())
