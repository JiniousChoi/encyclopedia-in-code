#!/usr/bin/env python3
''' 주어진 단어 리스트에서 , 다른 언어들을 조합하여
만들 수 있는 가장 긴 단어를 찾는 프로그램을 작성하라. '''

import unittest

def find_longest_compound(words):
    words.sort(key=lambda w: len(w), reverse=True)
    db = {}
    for word in words:
        db[word] = None #value is dont-care

    for word in words:
        c = get_compound(db, word)
        if c:
            return ''.join(c)
    return None

def get_compound(db, word):
    ''' returns [sub-word], at least 2 sub-words'''
    def bi_split(word):
        i_min = 1 #todo: optimize this
        i_max = len(word)-i_min
        for i in range(i_max, i_min-1, -1):
            yield word[:i], word[i:]

    for w1, w2 in bi_split(word):
        if w1 in db and w2 in db:
            return [w1, w2]

    for w1, w2 in bi_split(word):
        if w1 in db:
            compound = get_compound(db, w2)
            if compound:
                return [w1] + compound
    return []

class LongestCompoundTest(unittest.TestCase):
    def test_sample(self):
        self.assertLongestCompound(['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker'], 'dogwalker')
        self.assertLongestCompound(['cat', 'banana', 'dog', 'nana', 'walk', 'walker'], None)

    def assertLongestCompound(self, words, longest_compound):
        self.assertEqual(find_longest_compound(words), longest_compound)

if __name__=="__main__":
    unittest.main()
