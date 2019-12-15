#!/usr/bin/env python3
''' 52장의 카드를 완벽히 섞는 함수를 작성하라. 완벽한 난수 생성기는 주어진다 '''

import unittest
from random import randint
from operator import itemgetter

def shuffled_cards_index():
    return shuffled_index(52)

def shuffled_index(cnt):
    res = list(range(cnt))
    for i in range(cnt):
        #invariant
        #res[0:i] is selected
        #res[i:] is NOT selected
        nextint = randint(i, cnt-1)
        res[nextint], res[i] = res[i], res[nextint]
        #invariant
        #res[0:i+1] is selected
        #res[i+1:] is NOT selected

    #invariant
    #res[0:52], which is res[:], is selected
    return res

def shuffled_of(items):
    len_items = len(items)
    ran_idx = shuffled_index(len_items)
    
    shuffled = sorted(zip(ran_idx, items), key=itemgetter(0))
    shuffled = list(item for i,item in shuffled)
    
    return shuffled

class CardShuffleTest(unittest.TestCase):
    def test_shuffled(self):
        self.assertShuffled(shuffled_cards_index())

    def assertShuffled(self, cards):
        for i in range(len(cards)):
            self.assertTrue(i in cards)

    def test_application(self):
        alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        shuffled = shuffled_of(alphas)
        
        self.assertNotEqual(alphas, ''.join(shuffled))

        for a in alphas:
            self.assertTrue(a in shuffled)


if __name__=="__main__":
    unittest.main()
