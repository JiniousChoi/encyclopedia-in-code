#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: find -kth node in uni-directional linked link


def inversely_kth(ll, k):
    pass


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        self.assertInverselyKth([], 0, None)
        self.assertInverselyKth([], 3, None)

        self.assertInverselyKth([1], 0, 1)
        self.assertInverselyKth([1], 1, None)

        self.assertInverselyKth([1,2], 0, 2)
        self.assertInverselyKth([1,2], 1, 1)
        self.assertInverselyKth([1,2], 2, None)

        self.assertInverselyKth([1,2,3,4,5], 0, 5)
        self.assertInverselyKth([1,2,3,4,5], 1, 4)
        self.assertInverselyKth([1,2,3,4,5], 2, 3)
        self.assertInverselyKth([1,2,3,4,5], 3, 2)
        self.assertInverselyKth([1,2,3,4,5], 4, 1)
        self.assertInverselyKth([1,2,3,4,5], 5, None)


    def assertInverselyKth(self, ll, k, expected_val):
        pass

if __name__ == "__main__":

    unittest.main()
