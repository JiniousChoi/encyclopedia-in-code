#!/usr/bin/python3

import unittest

class PickMarvelTest(unittest.TestCase):
    def test_basecase1(self):
        marvels = [1,1]
        result = pick_marvel(marvels)
        self.assertEqual(result, [[1],[1]])

    def test_basecase2(self):
        marvels = [2,1]
        result = pick_marvel(marvels)
        self.assertEqual(result, [[2],[1]])
        
    def test_four_marvels1(self):
        marvels = [1,2,3,4]
        result = pick_marvel(marvels)
        self.assertEqual(result, [[4,2],[3,1]])

    def test_four_marvels2(self):
        marvels = [1,4,3,2]
        result = pick_marvel(marvels)
        self.assertTrue(sum(result[0])>sum(result[1]))
        #self.assertEqual(result, [[2,4],[1,3]])

    def test_four_marvels3(self):
        marvels = [4,5,3,1]
        result = pick_marvel(marvels)
        self.assertTrue(sum(result[0])>sum(result[1]))

# pick_marvel(marvels) => max(
def pick_marvel(marvels):
    assert len(marvels) >= 2
    if len(marvels)==2:
        return [[max(marvels)], [min(marvels)]]
    
    turn = decideTurn(marvels)
    
    # case1: pick first marvel
    pick, rest = marvels[0], marvels[1:]
    sub_result1 = pick_marvel(rest)
    sub_result1[turn].insert(0, pick)
    
    # case2: pick last marvel
    rest, pick = marvels[:-1], marvels[-1]
    sub_result2 = pick_marvel(rest)
    sub_result2[turn].insert(0, pick)
    
    #decide which is better
    if sum(sub_result1[turn]) >= sum(sub_result2[turn]):
        return sub_result1
    else:
        return sub_result2

def decideTurn(marvels):
    return 0 if len(marvels)%2==0 else 1


if __name__=='__main__':
    unittest.main()
