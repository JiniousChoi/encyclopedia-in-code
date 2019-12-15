#!/usr/bin/env python3
''' 단어가 적혀있는 아주 큰 텍스트 파일이 있다.
단어 두 개가 입력으로 주어졌을 때, 단어간 최단 거리(단어수 기준)를
반환하는 메서드를 작성하시오. O(1)안에 찾아낼 수 있겠는가?
여러분이 작성한 메소드의 시간 복잡도는 어떠한가.'''

import unittest
from math import inf

def shortest_distance(A, B):
    ''' my way - efficient '''
    assert A
    assert B
    mini = inf
    len_a, len_b = len(A), len(B)
    idx_a, idx_b = 0, 0

    while idx_a < len_a and idx_b < len_b:
        val_a, val_b = A[idx_a], B[idx_b]
        mini = min(abs(val_a - val_b), mini)
        if val_a < val_b:
            idx_a += 1
        else:
            idx_b += 1
    return mini

def shortest_distance_merged(A, B):
    ''' as 게일 맥도만suggested '''
    def merge(it_X, it_Y):
        ''' assume it_X and it_Y are in ascending order'''
        #it_x, it_y = it_X, it_Y
        #C = []
        #x = next(it_x, None)
        #y = next(it_y, None)
        #while x and y:
        #    if x < y:
        #        C.append(x)
        #        x = next(it_x, None)
        #    else:
        #        C.append(y)
        #        y = next(it_y, None)
        #if x:
        #    C.append(x)
        #    C.extend(it_x)
        #if y:
        #    C.append(y)
        #    C.extend(it_y)

        #return C

        C = list(it_X) + list(it_Y)
        C.sort()
        return C

    #code starts here
    assert A
    assert B

    mini = inf
    C = merge( ((a, 'a') for a in A), ((b, 'b') for b in B) )

    for i,j in zip(C, C[1:]):
        i_val, i_label = i
        j_val, j_label = j
        if i_label==j_label:
            continue
        mini = min(abs(i_val-j_val), mini)

    return mini

class WordsDistanceTest(unittest.TestCase):
    def test_samples(self):
        self.assertShortestDistance([0], [10], 10)
        self.assertShortestDistance([0], [8, 14], 8)
        self.assertShortestDistance([0,5], [3, 6], 1)
        self.assertShortestDistance([0, 10, 11, 15], [8, 14], 1)

    def assertShortestDistance(self, A, B, expected):
        self.assertEqual(shortest_distance(A, B), expected)
        self.assertEqual(shortest_distance_merged(A, B), expected)

if __name__=="__main__":
    unittest.main()
