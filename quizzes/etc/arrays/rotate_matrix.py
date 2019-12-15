#!/usr/bin/python3

from jpylib.jitertools import ring_iter
from collections import deque

def rotate_matrix(matrix):
    ''' shift elements to clockwise direction by 1 '''
    i, j = 0, 0
    n = len(matrix)
    h = n >> 1

    while i < h:
        #subtask
        rotate_ring(matrix, i, n-1-i, i, n-1-i)
        i += 1
        j += 1

    return matrix

def rotate_ring(matrix, T, B, L, R):
    i0 = T
    dq = deque([matrix[i0+1][i0]])
    for i,j in ring_iter(T, B, L, R):
        dq.append(matrix[i][j])
        val = dq.popleft()
        matrix[i][j] = val


if __name__ == "__main__":
    import unittest

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            self.assertEqual(rotate_matrix([]), [])
            self.assertEqual(rotate_matrix([[1]]), [[1]])
            self.assertEqual(rotate_matrix([[1,2],[3,4]]), [[3,1],[4,2]])
            self.assertEqual(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]), [[4,1,2],[7,5,3],[8,9,6]])
            self.assertEqual(rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]),
                                           [[5,1,2,3],[9,10,6,4],[13,11,7,8],[14,15,16,12]])

    unittest.main()
