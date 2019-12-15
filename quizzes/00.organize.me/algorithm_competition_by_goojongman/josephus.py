#!/usr/bin/env python3

#pypi 3rd party module
from llist import sllist as sll
import unittest

def josephus(N, K):
    #문제 조건
    assert len(N) >= 3
    assert K >= 3

    s = sll(N)
    idx = 0
    s.remove(s.nodeat(idx))
    while s.size > 2:
        # move to K-th node
        idx += K-1
        idx %= s.size #최적화 필요한가?

        #remove the node
        s.remove(s.nodeat(idx))

    assert s.size == 2
    return s


class JosephusTest(unittest.TestCase):
    def josephusEqual(self, N, K, survivors):
        jo = josephus(N=range(1,N+1), K=K)
        self.assertEqual([jo.first(), jo.last()], survivors)

    def test_basic(self):
        self.josephusEqual(N=3, K=3, survivors=[2,3])

    def test_sample1(self):
        self.josephusEqual(N=6, K=3, survivors = [3,5])
        self.josephusEqual(N=40, K=3, survivors = [11, 26])


if __name__ == "__main__":
    unittest.main()
