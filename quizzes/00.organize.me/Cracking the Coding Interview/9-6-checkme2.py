#!/usr/bin/env python3
''' n이 주어졌을 때, n-쌍의 괄호로 마늘 수 있는 모든 합당한 조합
(괄호가 적절히 열리고 닫힌)을 출력하는 알고리즘을 구현하라.
에)
입력: 3
출력: ((())), (()()), (())(), ()(()), ()()() '''

import unittest

def parens(a, b):
    ''' return [combi]
        a - opening parens
        b - closing parens '''
    assert a>=0 and b>=0
    
    if a==b==0:
        return []

    if a==b:
        return product('(', parens(a-1, b))
    else:
        assert a<b
        res = []
        if a>=1:
            res += product('(', parens(a-1, b))
        if b>=1:
            res += product(')', parens(a, b-1))
        return res

def parens_by_stack(cnt):
    ''' returns [combi] '''
    if cnt==0:
        return []

    visited_dic = {}
    stack = [(cnt, cnt)]

    while stack:
        a,b = stack[-1]
        assert a>=0 and b>=0
        if a==b==0:
            visited_dic[(a,b)] = []
            stack.pop()
            continue

        if a==b:
            if (a-1,b) not in visited_dic:
                stack.append((a-1,b))
                continue
        else:
            assert a<b, "%s<%s" %(a,b)
            if a>=1 and (a-1,b) not in visited_dic:
                stack.append((a-1,b))
                continue
            if b>=1 and (a,b-1) not in visited_dic:
                stack.append((a,b-1))
                continue

        assert (a,b) not in visited_dic
        res = []
        if a==b:
            assert (a-1,b) in visited_dic
            res += product('(', visited_dic.get((a-1,b), []))
        else:
            assert a<b
            if a>=1:
                res += product('(', visited_dic.get((a-1,b), []))
            if b>=1:
                res += product(')', visited_dic.get((a,b-1), []))
        visited_dic[(a,b)] = res
        stack.pop()

    return visited_dic[(cnt, cnt)]

def product(s, combis):
    ''' s - ( or )
        combis - [combi]
        returns [combi] '''
    if len(combis) == 0:
        return [s]
    else:
        return [s+combi for combi in combis]

def parens_by_queue(cnt):
    ''' return [combi] '''
    assert cnt >= 0
    if cnt==0:
        return []

    assert cnt>0
    res = []
    queue = [(cnt,cnt,'')]

    while queue: # [(a,b,'()']
        a,b,combi = queue.pop(0)
        if a<0 or b<0:
            pass
        elif a==b==0:
            res.append(combi)
        elif a==b:
            queue.append((a-1,b,combi+'('))
        else:
            assert a<b
            queue.append((a-1, b, combi+'('))
            queue.append((a, b-1, combi+')'))

    return res

class ParenCombisTest(unittest.TestCase):
    def test_method1(self):
        self.assertParens(0, [])
        self.assertParens(1, ['()'])
        self.assertParens(2, ['(())','()()'])
        self.assertParens(3, ['((()))', '(()())', '(())()', '()(())', '()()()'])

    def assertParens(self, cnt, res):
        self.assertEqual(parens(cnt, cnt), res)
        self.assertEqual(parens_by_stack(cnt), res)
        self.assertEqual(parens_by_queue(cnt), res)

if __name__=="__main__":
    unittest.main()
