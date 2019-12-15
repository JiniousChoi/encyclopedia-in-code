'''
백만 개의 단어 목록이 주어졌을 때, 각 단어의 글자들을 사용하여 만들 수 있는 최대 크기 직사각형을 구하는 알고리즈을 설계하라. 이 정사각형의 각 행은 하나의 단어여야 하고(왼쪽에서 오른쪽 방향). 리스트에서 단어를 선정할 때 연속된 단어를 선정할 필요는 없다. 모든 행의 길이는 서로 같아야 하고, 모든 열의 길이도 서로 같아야 한다.
'''
import datetime

DEBUG = False

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
            #if DEBUG:
            #    assert word not in rainbow_table[key][0]
            rainbow_table[key][0][word] = True
            rainbow_table[key][1] += 1

        else:
            rainbow_table[key] = [{word:True}, 1]
print('Done!')

from collections import Counter
def main(word_list):
    for words in get_words_by_same_length(word_list):
        #if len(words[0]) not in [10]:
        if len(words[0]) not in [9,8,7,6]:
            continue

        ####################
        words = words[::2]
        ####################

        print('starting time', datetime.datetime.now())
        print('trying words of length, {}({})'.format(len(words[0]), len(words)))
        if not is_satisfied_requirement(words):
            continue

        words_cnt = len(words)
        progress_printer = ProgressPrinter(words_cnt)
        for i, word in enumerate(words):
            if i <= 6438:#skipping ahead
                continue
            progress_printer.set_word_done_cnt(i+1)
            init_pivot = [word]
            make_words_matrix(init_pivot, words, progress_printer)

class ProgressPrinter(object):
    def __init__(self, word_len):
        self.x = 0
        self.X = word_len 
        self.depth_zero_progress_ratio= 0
        self.since = datetime.datetime.now()

        self.depth = -1
        self.depth_value_map = {}

    def set_word_done_cnt(self, word_done_cnt):
        self.x = word_done_cnt

    def set_depth(self, depth):
        self.depth = depth

    def set_depth_value(self, done_cnt):
        total_cnt = self.X
        depth_zero_progress_ratio = '%0.5f' % (100 * done_cnt / total_cnt) + ' %'# + ' {}/{}'.format(done_cnt, total_cnt)
        self.depth_value_map[self.depth] = depth_zero_progress_ratio

    def total_countdown(self):
        after = datetime.datetime.now()
        diff = after - self.since
        total_seconds = diff.total_seconds() * (self.X/self.x - 1)

        minute = total_seconds // 60
        second = total_seconds % 60

        hour = minute // 60
        minute = minute % 60

        day = hour // 24
        hour = hour % 24

        count_down = "{}:{}:{}:{}".format(int(day), int(hour), int(minute), int(second))
        return count_down

    def print(self):
        if self.x == 0:
            print("%0.5f"% 0, '%', end='\r')
            return
        depth_values = [] 
        for d in range(self.depth):
            value = self.depth_value_map[d]
            depth_values.append(value)
        depth_values_str = ' - '.join(depth_values)

        print("%0.5f"%(100*self.x/self.X), '%', '-', depth_values_str, '-', self.total_countdown(), end='\r')

    
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

def make_words_matrix(pivots, words, progress_printer, depth=0):
    #print(pivots) #if DEBUG:
    #    assert isinstance(pivots, list)
    #    assert len(words) >= len(words[0])*2

    word_len = len(words[0])
    #if DEBUG:
    #    assert len(pivots) <= word_len

    if len(pivots) == word_len:
        print('final quest')
        if is_success(pivots, words):
            print(pivots)
            #yield pivots
        else:
            print('failed...so sorry')

    else:
        #recursive part
        for i, word in enumerate(words):
            if word in pivots:
                continue

            if depth <= 0 and (i%1000==0):
                progress_printer.set_depth(depth)
                progress_printer.set_depth_value(i+1)
                progress_printer.print()

            new_pivots = pivots[:]
            new_pivots.append(word)
            pre_list = get_prefix_list(new_pivots)
            candidates_len_list = get_candidates_list(new_pivots, words, pre_list)
            if candidates_len_list:
                if is_worth_throttling(pre_list, candidates_len_list):
                    #print('depth({}) - its worth!'.format(depth))
                    make_words_matrix(new_pivots, words, progress_printer, depth+1)

            #if depth == 0:
            #    progress_printer.set_depth_zero(i+1, words_len)
            #    progress_printer.print()

def get_prefix_list(pivots):
    prefix_list = [''.join(ch_list) for ch_list in zip(*pivots)]
    return prefix_list

def get_candidates_list(pivots, words, prefix_list):
    candidates_len_list = []

    word_len = len(words[0])
    for prefix in prefix_list:
        key = (word_len, prefix)
        if key in rainbow_table:
            candidates_len = rainbow_table[key][1]

            #최적화
            for pivot in pivots:
                if pivot in rainbow_table[key][0]:
                    candidates_len -= 1
                    if candidates_len < 1:
                        return None
            
        else:
            return None
        candidates_len_list.append(candidates_len)

    return candidates_len_list


def is_worth_throttling(prefix_list, candidates_len_list):
    #if DEBUG:
    #    assert len(prefix_list) == len(candidates_len_list)

    i=0
    for prefix, cnt in Counter(prefix_list).items():
        if cnt > candidates_len_list[i]:
            return False
        i+=1
    return True


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

print('START TIME', datetime.datetime.now())
the_matrix= main(WORD_LIST)
#for matrix in the_matrix:
#    print('FOUND!')
#    for word in matrix:
#        print(word)
#    print('')
print('END TIME', datetime.datetime.now())
