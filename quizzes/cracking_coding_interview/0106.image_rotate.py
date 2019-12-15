#!/usr/bin/python3
## author: jinchoiseoul@gmail.com

'''
1.6-이미지를 표현하는 NxN 행렬이 있다. 이미지의 각 픽셀은 4바이트로 표현된다.
이때, 이미지를 90도 회전시키는 메소드를 작성하라.
'''

from math import floor, ceil
from jpylib.jitertools import flatten


def rotate_matrix(matrix):
    for y,x in rotating_zone(matrix):
        rotate_pixel(y,x,matrix)
    return matrix

def rotating_zone(matrix):
    m = (len(matrix)-1)/2
    for y in getClosedRange(m):
        for x in getOpenedRange(m):
            yield y,x

def getClosedRange(m):
    return range(0, floor(m)+1)

def getOpenedRange(m):
    return range(0, ceil(m))

def rotate_pixel(y,x,matrix):
    #1. 좌표전환
    m=(len(matrix)-1)/2
    dy,dx=m-y,m-x

    #2. 4개의 돌림점
    y1,x1=int(m-dy),int(m-dx)
    y2,x2=int(m-dx),int(m+dy)
    y3,x3=int(m+dy),int(m+dx)
    y4,x4=int(m+dx),int(m-dy)
    
    #3. 실제 대입
    matrix[y1][x1],matrix[y2][x2],matrix[y3][x3],matrix[y4][x4] = \
        matrix[y4][x4],matrix[y1][x1],matrix[y2][x2],matrix[y3][x3]

        
if __name__=="__main__":
    
    import unittest

    class SolutionTest(unittest.TestCase):
        def setUp(self):
            matrix0 = []
            matrix1 = [ [1] ]
            matrix2 = [ [1,2],
                        [3,4] ]
            matrix3 = [ [1,2,3],
                        [4,5,6],
                        [7,8,9] ]
            matrix4 = [ [1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,14,15,16] ]
            self.matrixes = [matrix0, matrix1, matrix2, matrix3, matrix4]

        def test_basics(self):
            for matrix in self.matrixes:
                self.assertRotateWorks(matrix)

        def assertRotateWorks(self, matrix):
            expected = list(flatten(list(zip(*matrix[::-1]))))
            actual = list(flatten(rotate_matrix(matrix)))
            self.assertEqual(actual, expected)

    unittest.main()
