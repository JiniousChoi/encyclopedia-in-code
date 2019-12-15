#!/usr/bin/env python3

from math import sqrt
import unittest

INFINITE = 987654321

def make_triangle(s):
    ''' ex) "0 1 2" -> [[0], [1,2]] '''
    res = []
    numbers = [int(e) for e in s.strip().split()]
    for i in range(1, INFINITE):
        if len(numbers)==0:
            break
        tmp = []
        for j in range(i):
            n = numbers.pop(0)
            tmp.append(n)
        res.append(tmp)

    return res

def trianglepath(x, y, triangle):
    ''' returns maximum path [a,b,c,..] '''
    #basis
    if len(triangle) == x+1:
        return [triangle[x][y]]
    
    return [triangle[x][y]] + max(trianglepath(x+1,y,triangle),\
                                trianglepath(x+1,y+1,triangle),\
                                key=sum)


class MakeTriangleTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(make_triangle('1'), [[1]])
        self.assertEqual(make_triangle('1 2 3'), [[1], [2,3]])
        self.assertEqual(make_triangle('1 2 3 4 5 6'), [[1], [2,3], [4,5,6]])

class TrianglepathTest(unittest.TestCase):
    def test_boundary(self):
        self.assertEqual(trianglepath(0, 0, make_triangle('3')), [3])

    def test_basic(self):
        self.assertEqual(trianglepath(0, 0, make_triangle('1 2 3')), [1,3])
        self.assertEqual(trianglepath(0, 0, make_triangle('6 1 2 3 7 4 9 4 1 7 2 7 5 9 4')), [6,2,4,7,9])


if __name__=="__main__":
    unittest.main()
