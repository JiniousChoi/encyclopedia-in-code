#!/usr/bin/env python3

import unittest

def parse(s):
    lines = [line.strip() for line in s.strip().splitlines()]
    res = []
    for line in lines:
        li = []
        for e in line:
            if e == '*':
                li.append(None)
            else:
                li.append(int(e))
        res.append(li)
    return res

def sudoku(s):
    ''' returns True if s is fully filled successfully. False, otherwise '''
    def pick_one(s):
        for i in range(9):
            for j in range(9):
                if s[i][j] == None:
                    return i,j

    def is_sudoku_complete(s):
        for line in s:
            if None in line:
                return False
        return True

    def is_possible(s, i, j, v):
        if v in s[i]:
            return False
        for r in range(9):
            if s[r][j] == v:
                return False
        r_start = (i//3)*3
        c_start = (j//3)*3
        for r in range(r_start, r_start+3):
            for c in range(c_start, c_start+3):
                if s[r][c]==v:
                    return False
        return True

    i,j = pick_one(s)
    for v in range(1,10):
        if not is_possible(s,i,j,v):
            continue
        s[i][j] = v
        if is_sudoku_complete(s):
            return True
        if sudoku(s):
            return True
        s[i][j] = None
    return False

class SudokuTest(unittest.TestCase):
    def setUp(self):
        self.sample = '''
            128**547*
            **5*8*39*
            9*36428**
            4**51*68*
            78*4*3*59
            *36*98**1
            **43791*8
            *69*2*5**
            *178**924'''
        self.sample2 = '''
            *2*63****
            6**4***1*
            ****5**7*
            **39****4
            **8***6**
            7****35**
            *4**2****
            *5***8**9
            ****91*3*
            '''
        self.sample3 = '''
            *********
            *********
            *********
            *********
            *********
            *********
            *********
            *********
            *********
            '''
    def test_parse(self):
        s = parse(self.sample)
        
        self.assertEqual(len(s), 9)
        for i in range(9):
            self.assertEqual(len(s[i]), 9)

    def test_sudoku(self):
        s = parse(self.sample3)

        succeed = sudoku(s)
        self.assertTrue(succeed)

        import pprint
        pprint.pprint(s)

        for line in s:
            self.assertEqual(sum(line), 45)

        for col in range(9):
            col_sum = 0
            for row in range(9):
                col_sum += s[row][col]
            self.assertEqual(col_sum, 45)
        
        for r in [0,3,6]:
            for c in [0,3,6]:
               self.assertEqual(sum(s[x][y] for x in [r,r+1,r+2] for y in [c,c+1,c+2]), 45)

if __name__=="__main__":
    unittest.main()
