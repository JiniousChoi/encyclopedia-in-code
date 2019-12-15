#!/usr/bin/env python3
'''두 수를 더하는 함수를 작성하라 +를 비롯한 수학 연산자는 이용할 수 없다. '''

import unittest

class SolutionA:
    add_table = {
        (0,0):0 , (0,1):1 , (0,2):2 , (0,3):3 , (0,4):4 , (0,5):5 , (0,6):6 , (0,7):7 , (0,8):8 , (0,9):9 ,
        (1,0):1 , (1,1):2 , (1,2):3 , (1,3):4 , (1,4):5 , (1,5):6 , (1,6):7 , (1,7):8 , (1,8):9 , (1,9):10 ,
        (2,0):2 , (2,1):3 , (2,2):4 , (2,3):5 , (2,4):6 , (2,5):7 , (2,6):8 , (2,7):9 , (2,8):10 , (2,9):11 ,
        (3,0):3 , (3,1):4 , (3,2):5 , (3,3):6 , (3,4):7 , (3,5):8 , (3,6):9 , (3,7):10 , (3,8):11 , (3,9):12 ,
        (4,0):4 , (4,1):5 , (4,2):6 , (4,3):7 , (4,4):8 , (4,5):9 , (4,6):10 , (4,7):11 , (4,8):12 , (4,9):13 ,
        (5,0):5 , (5,1):6 , (5,2):7 , (5,3):8 , (5,4):9 , (5,5):10 , (5,6):11 , (5,7):12 , (5,8):13 , (5,9):14 ,
        (6,0):6 , (6,1):7 , (6,2):8 , (6,3):9 , (6,4):10 , (6,5):11 , (6,6):12 , (6,7):13 , (6,8):14 , (6,9):15 , 
        (7,0):7 , (7,1):8 , (7,2):9 , (7,3):10 , (7,4):11 , (7,5):12 , (7,6):13 , (7,7):14 , (7,8):15 , (7,9):16 , 
        (8,0):8 , (8,1):9 , (8,2):10 , (8,3):11 , (8,4):12 , (8,5):13 , (8,6):14 , (8,7):15 , (8,8):16 , (8,9):17 , 
        (9,0):9 , (9,1):10 , (9,2):11 , (9,3):12 , (9,4):13 , (9,5):14 , (9,6):15 , (9,7):16 , (9,8):17 , (9,9):18 
    }

    def _add(self, x,y):
        assert 0 <= x <= 9
        assert 0 <= y <= 9
        return self.add_table[(x,y)]

    def add(self, x,y):
        res = self.add_by_digit(x,y)
        return self.s_to_i_join(res)

    def add_by_digit(self, x, y):
        sx, sy = str(x), str(y)
        len_sx, len_sy = len(sx), len(sy)
        max_len = max(len_sx, len_sy)
        c_next = 0
        res = []
        for sxi, syi in reversed(list(zip(sx.zfill(max_len), sy.zfill(max_len)))):
            ci = c_next
            xi, yi = int(sxi), int(syi)
            c_next, di = self.csplit(self._add(xi, yi))
            c_next2, di = self.csplit(self._add(di, ci))
            c_next += c_next2
            res.insert(0, di)

        res.insert(0, c_next)
        return res

    def csplit(self, n):
        ''' '''
        assert 0<= n <= 19
        sn = str(n)
        if len(sn)==1:
            return 0, n
        return [int(x) for x in sn]
        
    def s_to_i_join(self, res):
        return int(''.join(str(i) for i in res))

class SolutionB:
    def add(self, x, y):
        if x==0: return y
        if y==0: return x

        d = x ^ y
        c = x & y
        
        return self.add(d, c<<1)


class AddTest(unittest.TestCase):
    def assertAdd(self, twos, res):
        assert len(twos) == 2

        self.assertEqual(twos[0]+twos[1], res)

        solverA = SolutionA()
        self.assertEqual(solverA.add(*twos), res)

        solverB = SolutionB()
        self.assertEqual(solverB.add(*twos), res)

    def test_add_one_digits(self):
        self.assertAdd((5,0), 5)
        self.assertAdd((0,5), 5)
        self.assertAdd((1,1), 2)
        self.assertAdd((4,5), 9)
        self.assertAdd((5,5), 10)
        self.assertAdd((9,9), 18)

    def test_add_one_and_two_digit(self):
        self.assertAdd((0,11), 11)
        self.assertAdd((11,0), 11)
        self.assertAdd((12,11), 23)
        self.assertAdd((9,10), 19)
        self.assertAdd((10,9), 19)
        self.assertAdd((123,321), 444)
        self.assertAdd((12345678, 87654321), 99999999)
        self.assertAdd((123456787654321, 876543212345678), 999999999999999)

if __name__=="__main__":
    unittest.main()
