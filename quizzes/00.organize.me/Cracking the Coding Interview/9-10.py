#!/usr/bin/env python3

import unittest
from math import inf

def max_height_combi(boxes):
    ''' return max [box] of height
        box : (w,h,d) '''
    if boxes == [] or len(boxes) == 1:
        return boxes
    max_combi = [(-inf, -inf, -inf)]
    for chosen_box in boxes:
        smaller_boxes = filter_smaller_boxes(chosen_box, boxes)
        chosen_combi = [chosen_box] + max_height_combi(smaller_boxes)
        if is_larger(max_combi, chosen_combi):
            max_combi = chosen_combi
    return max_combi

def filter_smaller_boxes(chosen_box, boxes):
    ''' return [box] '''
    cw, ch, cd = chosen_box
    #return list(filter(lambda w,h,d: w<cw and h<ch and d<cd, boxes))
    return [(w,h,d) for (w,h,d) in boxes if (cw>w and ch>h and cd>d)]

def is_larger(boxes_a, boxes_b):
    ''' return True if sum of height of
        boxes_b is larger than that of boxes_a '''
    return sum(h for w,h,d in boxes_a) < sum(h for w,h,d in boxes_b)

def max_height(boxes):
    boxes = max_height_combi(boxes)
    return sum(h for w,h,d in boxes)

class MaxHeightBoxesTest(unittest.TestCase):
    def test_max_height_combi_samples(self):
        self.assertMaxCombi([], [])
        self.assertMaxCombi([(3,3,3)], [(3,3,3)])

        self.assertMaxCombi([(3,3,3), (1,1,1)], [(3,3,3), (1,1,1)])
        self.assertMaxCombi([(1,1,1), (3,3,3)], [(3,3,3), (1,1,1)])

        self.assertMaxCombi([(2,3,1), (100,2,100)], [(2,3,1)])
        self.assertMaxCombi([(3,3,3), (2,2,2), (100,100,100), (1,1,1)], [(100,100,100),(3,3,3),(2,2,2),(1,1,1)])

        self.assertMaxCombi([(3,3,3), (2,2,2), (1,10,100), (1,1,1)], [(1,10,100)])

    def assertMaxCombi(self, boxes, max_combi):
        self.assertEqual(max_height_combi(boxes), max_combi)

    def test_solution(self):
        self.assertMaxHeight([], 0)
        self.assertMaxHeight([(3,3,3)], 3)

        self.assertMaxHeight([(3,3,3), (1,1,1)], 4)
        self.assertMaxHeight([(1,1,1), (3,3,3)], 4)

        self.assertMaxHeight([(2,3,1), (100,2,100)], 3)
        self.assertMaxHeight([(3,3,3), (2,2,2), (100,100,100), (1,1,1)], 106)

    def assertMaxHeight(self, boxes, height):
        self.assertEqual(max_height(boxes), height)

if __name__=="__main__":
    unittest.main()
