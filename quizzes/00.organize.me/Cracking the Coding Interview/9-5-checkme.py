#!/usr/bin/env python3

import unittest

def permutations(selected, unselected, cnt):
    # 인자부가 복잡하다는 단점이 있으나, yield를 써서 해결할 수 있다는 장점 있음.
    # 왜냐하면 boundary condition 만족시 ```parameter의 하나가 결과값이기 때문```이다.
    # 이를 부모 호출 함수로 넘겨 추합해 가며 최종 부모로 올려보낼 수도 있지만,
    # yield를 통하면 더욱 간단하고도 유연한 구성이 가능해진다.
    ''' selected : str
        unselected : str '''
    #assert len(set(unselected)) == len(unselected)
    #assert len(selected)+len(unselected) >= cnt

    if len(selected) == cnt:
        yield selected
    else:
        for unsel in unselected:
            yield from permutations(selected+unsel, unselected.replace(unsel, ''), cnt)

def permutations2(s, cnt):
    # 인수부는 하나로서 간단하지만, sub-routine call 결과값들을
    # 돌려받아 바로 쓸 수 없고 이를 가공해 내야 하는 형태이므로
    # yield 사용은 불가능하다. 굳이 따지자면 yield의 경우보단 메모리 효율이 좋지 않은 셈.
    ''' return [str] '''
    def product(a, ss):
        ''' return [str]
            ss : [str]
            a : str '''
        return [a+aa for aa in ss]

    assert len(s) >= cnt
    if cnt == 0:
        return ['']
    res = []
    for a in s:
        res += product(a, permutations2(s.replace(a, ''), cnt-1))
    return res

class PermTest(unittest.TestCase):
    def test_method1(self):
        self.assertPermutation('', [''])
        self.assertPermutation('a', ['a'])
        self.assertPermutation('ab', ['ab', 'ba'])

        self.assertPermutation('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertPermutation('abc', ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'], 2)
        self.assertPermutation('abc', ['a', 'b', 'c'], 1)
        self.assertPermutation('abc', [''], 0)
    
    def assertPermutation(self, s, res, cnt=None):
        if cnt==None:
            cnt = len(s)
        self.assertEqual(list(permutations('', s, cnt)), res)
        self.assertEqual(permutations2(s, cnt), res)

def combinations(selected, unselected, cnt):
    if len(selected) == cnt:
        yield selected
    elif len(selected) + len(unselected) >= cnt:
        yield from combinations(selected+unselected[0], unselected[1:], cnt)
        yield from combinations(selected, unselected[1:], cnt)

def bubun(s):
    for i in range(len(s)+1):
        yield from combinations('', s, i)

class CombiTest(unittest.TestCase):
    def test_samples(self):
        self.assertCombis('abc', 0, [''])
        self.assertCombis('abc', 1, ['a','b','c'])
        self.assertCombis('abc', 2, ['ab','ac','bc'])
        self.assertCombis('abc', 3, ['abc'])
        self.assertCombis('abc', 4, [])

    def assertCombis(self, s, cnt, res):
        self.assertEqual(list(combinations('', s, cnt)), res)

    def test_bubun(self):
        self.assertEqual(list(bubun('ab')), ['', 'a', 'b', 'ab'])
        self.assertEqual(list(bubun('abc')), ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'])

if __name__=="__main__":
    unittest.main()
