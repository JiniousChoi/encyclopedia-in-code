#!/usr/bin/env python3
''' 01|^의 조합에 괄호를 섞어 0이 되는 모든 경우의 수를 출력하시오'''

import unittest

def parens(exp):
    ''' returns [exp]'''
    def wrap_paren(s):
        return '(' + s + ')'

    def paren_join(exps1, op, exps2):
        ''' return [exp] '''
        res = []
        for exp1 in exps1:
            for exp2 in exps2:
                if len(exp1)>1:
                    exp1 = wrap_paren(exp1)
                if len(exp2)>1:
                    exp2 = wrap_paren(exp2)
                new_exp = exp1 + op + exp2
                res.append(new_exp)
        return res

    if len(exp)==1:
        return [exp]

    if len(exp)==3:
        return [exp]

    res = []
    for i in range(1, len(exp), 2):
        res += paren_join(parens(exp[:i]), exp[i], parens(exp[i+1:]))
    #res += ['(' +exp + ')']

    return res

def solution(exp):
    ''' return [exp] '''
    res = parens(exp)
    return [e for e in res if eval(e)==0]
    #return [e for e in list(set(res)) if eval(e)==0]

class ParenTest(unittest.TestCase):
    def test_paren_samples(self):
        self.assertParens('0', ['0'])
        self.assertParens('0|0', ['0|0'])
        self.assertParens('0|0|0', ['0|(0|0)', '(0|0)|0'])
        self.assertParens('1^0|0|1', ['0|(0|0)', '(0|0)|0'])

    def test_filter(self):
        self.assertEqual(solution('1^0|0|1'), ['1^(0|(0|1))', '1^((0|0)|1)'])

    def assertParens(self, exp, res):
        self.assertEqual(parens(exp), res)

if __name__=="__main__":
    unittest.main()
