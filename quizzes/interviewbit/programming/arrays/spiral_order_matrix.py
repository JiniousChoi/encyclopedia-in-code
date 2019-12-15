#!/usr/bin/python2
from jpylib.jitertools import ring_iter


def matrix_spiral_sol1(matrix):
    #auxiliary methods
    def didj():
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        return dirs[dir%4]
    def in_range(i,j):
        return up<=i<=down and left<=j<=right

    n = len(matrix)
    up,down,left,right = 0, n-1, 0, n-1

    dir = 0
    i,j = (0,0)
    
    #strategy: action and then move
    while in_range(i,j):
        #action
        yield matrix[i][j]

        #turn right if blocked ``ahead``
        di, dj = didj()
        if not in_range(i+di, j+dj):
            if dir==0: up += 1
            elif dir==1: right -= 1
            elif dir==2: down -= 1
            elif dir==3: left += 1
            else: assert False, "dir({}) should be in range(4)".format(dir)

            dir += 1
            dir %= 4

        #move
        di, dj = didj()
        i += di
        j += dj


def matrix_spiral_sol2(matrix):
    if not matrix:
        return

    n = len(matrix)
    m = len(matrix[0])
    T,B,L,R = 0, n-1, 0, m-1
    r,c = 0,0
    dir = 0
    while T<=B and L<=R:
        if dir == 0:
            for c in range(L, R+1):
                yield matrix[r][c]
            T += 1
        elif dir == 1:
            for r in range(T, B+1):
                yield matrix[r][c]
            R -= 1
        elif dir == 2:
            for c in range(R, L-1, -1):
                yield matrix[r][c]
            B -= 1
        elif dir == 3:
            for r in range(B, T-1, -1):
                yield matrix[r][c]
            L += 1
        dir = (dir+1) % 4


def matrix_spiral_sol3(matrix):
    if not matrix:
        return

    n = len(matrix)
    m = len(matrix[0])
    T,B,L,R = 0, n-1, 0, m-1
    while T<=B and L<=R:
        for c in range(L, R+1):
            yield matrix[T][c]
        T += 1
        for r in range(T, B+1):
            yield matrix[r][R]
        R -= 1
        for c in range(R, L-1, -1):
            yield matrix[B][c]
        B -= 1
        for r in range(B, T-1, -1):
            yield matrix[r][L]
        L += 1


def matrix_spiral_sol4(matrix):
    if not matrix:
        return

    n = len(matrix)
    m = len(matrix[0])
    T,B,L,R = 0, n-1, 0, m-1
    while T<=B and L<=R:
        for r,c in ring_iter(T,B,L,R):
            yield matrix[r][c]
        T,B,L,R = T+1,B-1,L+1,R-1

    
if __name__ == "__main__":
    import unittest

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            self.assertSpiral([],[])
            self.assertSpiral([[1]], [1])
            self.assertSpiral([[1,2],[3,4]], [1,2,4,3])
            self.assertSpiral([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5])
            self.assertSpiral([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
                              [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])

        def assertSpiral(self, matrix, expected):
            self.assertEqual(list(matrix_spiral_sol1(matrix)), expected)
            self.assertEqual(list(matrix_spiral_sol2(matrix)), expected)
            self.assertEqual(list(matrix_spiral_sol3(matrix)), expected)
            self.assertEqual(list(matrix_spiral_sol4(matrix)), expected)

    unittest.main()
