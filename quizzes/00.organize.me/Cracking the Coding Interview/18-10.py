#!/usr/bin/env python3
''' 사전에 등장하고 길이가 같은 두 단어가 주어졌을 때,
한 번에 글자 하나만 바꾸어 한 단어를 다른 단어로 변환하는 메서드를 작성하라.
변환과정에서 만들어지는 각 단어도 사전에 있는 단어여야 한다.
input: DAMP, LIKE
OUTPUT: DAMP -> LAMP -> LIMP -> LIME -> LIKE
'''

import unittest
WORDS = ['FISH', 'HACK', 'DAMP', 'LAMP', 'LIMP', 'LIME', 'LIKE', 'HELL',
        'DICK', 'DICT', 'KNOW', 'BOWL', 'ROSE', 'ROLL', 'KILL', 'LOVE']

DIC = {word:True for word in WORDS}

def wordjump(dic, start, stop):
    def get_neighbors(v):
        for i in range(len(v)):
            for alpha in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                new_word = v[:i] + alpha + v[i+1:]
                if new_word in dic:
                    yield new_word

    if start not in dic:
        return None

    parent = {start : None}
    to_visit = [start] # to visit
    discovered = {start} # discovered == to_visit + visited

    found = False
    while to_visit:
        v = to_visit.pop(0) #now, v is visited
        if v == stop:
            found = True
            break

        for neigh_v in get_neighbors(v):
            if neigh_v not in discovered:
                parent[neigh_v] = v
                to_visit.append(neigh_v)
                discovered.add(neigh_v)
    
    if not found:
        return None

    path = []
    while v:
        path.append(v)
        v = parent[v]

    return list(reversed(path))

class WordjumpTest(unittest.TestCase):
    def test_samples(self):
        i = ['DAMP', 'LIKE']
        o = ['DAMP', 'LAMP', 'LIMP', 'LIME', 'LIKE']
        self.assertWordjump(i, o)

    def test_sample2s(self):
        self.assertWordjump(['LIME', 'XXXX'], None)
        self.assertWordjump(['XXXX', 'YYYY'], None)

    def assertWordjump(self, i, o):
        self.assertEqual(wordjump(DIC, *i), o)

if __name__=="__main__":
    unittest.main()
