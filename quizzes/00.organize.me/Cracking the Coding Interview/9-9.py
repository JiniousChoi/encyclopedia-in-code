#!/usr/bin/env python3

import unittest

def eight_queens(queens_pos):
    ''' returns every possible eight queen placements
        return type is [ queens_pos ]
        param quees_pos: [(i,j),]'''

    def colide(i, j, queens):
        def slope(i1,j1,i2,j2):
            return (j1-j2)/(i1-i2)

        for qi,qj in queens:
            if i==qi:
                return True
            if j==qj:
                return True
            if slope(i,j,qi,qj) in [1.0,-1.0]:
                return True
        return False

    if len(queens_pos) == 8:
        return [queens_pos]

    result = []

    i = len(queens_pos) if queens_pos else 0

    for j in range(8):
        #if i,j collide with any of queens_pos:
        if colide(i,j, queens_pos):
            continue
        res_queens_pos_s = eight_queens( queens_pos[:] + [(i,j)] )
        result += res_queens_pos_s

    return result

class EightQueenTest(unittest.TestCase):
    def test_samples(self):
        res = eight_queens([])
        self.assertEqual(len(res), 92)
        
        self.pretty_print(res[0])
        #for queens in res:
        #    i0, j0 = queens[0]
        #    i1, j1 = queens[1]
        #    if i0==0 and j0==0 and i1==1 and j1==1:
        #        self.pretty_print(queens)
        #        break
        #assert False, 'how come is there not a sngle case'

    def pretty_print(self, queens):
        for qi, qj in queens:
            for j in range(8):
                if qj==j:
                    print('O', end='')
                else:
                    print('-', end='')
            print('')

if __name__=="__main__":
    unittest.main()
