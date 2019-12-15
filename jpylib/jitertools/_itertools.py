#!/usr/bin/python3
## author : jinchoiseoul@gmail.com


from collections import Iterable, Iterator


def ring_iter(T, B, L, R):
    r, c = T, L

    for c in range(L, R+1):
        yield r, c
    T += 1
    for r in range(T, B+1):
        yield r, c
    R -= 1
    for c in range(R, L-1, -1):
        yield r, c
    B -= 1
    for r in range(B, T-1, -1):
        yield r, c
    L += 1


def flatten(obj):
    if isinstance(obj, Iterable):
        for o in obj:
            yield from flatten(o)
    else:
        yield obj


def group_by(iterable):
    ''' @param iterable such as list, tuple, only that generator is not supported
        @yield [(key, count::int)] '''
    if not iterable:
        return []

    i, j, n = 0, 1, len(iterable)
    while i < n:
        while j < n and iterable[i] == iterable[j]:
            j += 1
        yield iterable[i], j-i
        i,j = j,j+1
    

def igroup_by0(it):
    assert isinstance(it, Iterator)
    nil = object()
    cur = next(it, nil)
    if cur == nil:
        return
    prev, cur = cur, cur
    i,j = 0, 0
    while prev != nil:
        while prev == cur:
            cur = next(it, nil)
            j += 1
        yield prev, j-i
        prev, cur = cur, next(it, nil)
        i,j = j, j+1


def igroup_by1(it):
    ''' @@param it: iterator or generator 
        @yield [(key, count::int)] '''
    assert isinstance(it, Iterator)
    nil = object()
    cur = next(it, nil)
    if cur == nil:
        return
    prev = cur
    i,j = 0,0
    while prev != nil:
        if prev != cur:
            yield prev, j-i
            i, prev = j, cur

        cur = next(it, nil)
        j += 1


def igroup_by2(it):
    ''' @@param it: iterator or generator 
        @yield [(key, count::int)] '''
    assert isinstance(it, Iterator)
    nil = object()
    cur = next(it, nil)
    if cur == nil:
        return
    i,j = 0,0
    prev = cur
    while True:
        if cur == nil:
            yield prev, j-i
            break
        elif prev != cur:
            yield prev, j-i
            prev,i = cur,j
        cur = next(it, nil)
        j += 1


def igroup_by3(it):
    assert isinstance(it, Iterator)
    try:
        prev = next(it)
    except StopIteration:
        return
    cur = prev
    i,j = 0,0
    while True:
        if prev != cur:
            yield prev, j-i
            i,prev = j,cur

        j += 1
        try:
            cur = next(it)
        except StopIteration:
            yield prev, j-i
            break


igroup_by = igroup_by0


def permutations(n, r):
    yield from _permutations(n, r, visited=[False]*n)


def factorial(n):
    yield from permutations(n, n)


def permutations_with_replacement(n, r, chosen=[]):
    assert 0<=n and 0<=r
    #basis
    if len(chosen) == r:
        if chosen:
            yield chosen[:]
    else:
        for choice in range(n):
            chosen.append(choice)
            yield from permutations_with_replacement(n, r, chosen)
            chosen.pop(-1)


def _permutations(n, r, visited, chosen=[]):
    ''' generate [index::int] '''
    assert 0 <= len(chosen) <= r <= n, "0 <= {}({}) <= {} <= {}".format(len(chosen), chosen, r, n)
    #basis
    if len(chosen) == r:
        if chosen:
            yield chosen[:]
    else:
        for choice in range(n):
            if visited[choice]:
                continue
            visited[choice] = True
            chosen.append(choice)
            yield from _permutations(n, r, visited, chosen)
            chosen.pop(-1)
            visited[choice] = False


def combinations(n, r, chosen=[]):
    ''' yield [index::int] '''
    assert 0 <= len(chosen) <= r <= n

    s = chosen[-1] + 1 if chosen else 0
    #basis
    if len(chosen) == r:
        if chosen:
            yield chosen[:]
    elif n-s < r-len(chosen):
        #back-tracking by pigion principle
        return
    else:
        for choice in range(s, n):
            chosen.append(choice)
            yield from combinations(n, r, chosen)
            chosen.pop(-1)


def combinations_with_replacement(n, r, chosen=[]):
    if len(chosen) == r:
        if chosen:
            yield chosen[:]
    else:
        s = chosen[-1] if chosen else 0
        for choice in range(s, n):
            chosen.append(choice)
            yield from combinations_with_replacement(n, r, chosen)
            chosen.pop(-1)


def subset(n, chosen=[]):
    ''' generate - chosen
        chosen : [choice on each idx :: bool] '''
    assert 0 <= len(chosen) <= n
    #basis
    if len(chosen) == n:
        if chosen:
            yield chosen[:]
    else:
        for choice in [False, True]:
            chosen.append(choice)
            yield from subset(n, chosen)
            chosen.pop(-1)


import unittest


class UtilTest(unittest.TestCase):

    def test_ring_iter_basics(self):
        ring_it = ring_iter(0, -1, 0, -1)
        self.assertEqual(list(ring_it), [])

        ring_it = ring_iter(0, 0, 0, 0)
        self.assertEqual(list(ring_it), [(0,0)])

        ring_it = ring_iter(0, 1, 0, 1)
        self.assertEqual(list(ring_it), [(0,0),(0,1),(1,1),(1,0)])

        ring_it = ring_iter(3, 5, 1, 3)
        self.assertEqual(list(ring_it), [(3,1),(3,2),(3,3),(4,3),(5,3),(5,2),(5,1),(4,1)])

    def test_flatten_basics(self):
        self.assertEqual(list(flatten([])), [])
        self.assertEqual(list(flatten(3)), [3])
        self.assertEqual(list(flatten([3,5,(1,2),[1,[2,[3]],[],(),[4],5,[[6],7]]])), [3,5,1,2,1,2,3,4,5,6,7])

    def test_group_by(self):
        self.assertEqual(list(group_by("aabcccda")), [('a',2),('b',1),('c',3),('d',1),('a',1)])

    def test_igroup_by(self):
        igroup_by_methods = [igroup_by0, igroup_by1, igroup_by2, igroup_by3]
        for igroup_by in igroup_by_methods:
            self.assertEqual(list(igroup_by(iter([]))), [])
            self.assertEqual(list(igroup_by(iter("aabcccda"))), [('a',2),('b',1),('c',3),('d',1),('a',1)], msg=igroup_by)
            self.assertEqual(list(igroup_by(iter([None, None, 1,1,3]))), [(None,2),(1,2),(3,1)])


class PermTest(unittest.TestCase):

    def test_permutations(self):
        self.assertEqual(list(permutations(3,0)), [])
        self.assertEqual(list(permutations(3,1)), [[0], [1], [2]])
        self.assertEqual(list(permutations(3,2)), [[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]])
        self.assertEqual(list(permutations(3,3)), [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]])

    def test_factorial(self):
        self.assertEqual(list(factorial(0)), [])
        self.assertEqual(list(factorial(1)), [[0]])
        self.assertEqual(list(factorial(2)), [[0,1],[1,0]])
        self.assertEqual(list(factorial(3)), [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]])

    def test_permutations_with_replacement(self):
        self.assertEqual(list(permutations_with_replacement(2,0)), [])
        self.assertEqual(list(permutations_with_replacement(2,1)), [[0],[1]])
        self.assertEqual(list(permutations_with_replacement(2,2)), [[0,0],[0,1],[1,0],[1,1]])
        self.assertEqual(list(permutations_with_replacement(2,3)), [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])


class CombiTest(unittest.TestCase):

    def test_combinations(self):
        self.assertEqual(list(combinations(3,0)), [])
        self.assertEqual(list(combinations(3,1)), [[0], [1], [2]])
        self.assertEqual(list(combinations(3,2)), [[0,1],[0,2],[1,2]])
        self.assertEqual(list(combinations(3,3)), [[0,1,2]])

    def test_combinations_with_replacement(self):
        self.assertEqual(list(combinations_with_replacement(3,0)), [])
        self.assertEqual(list(combinations_with_replacement(3,1)), [[0], [1], [2]])
        self.assertEqual(list(combinations_with_replacement(3,2)), [[0,0],[0,1],[0,2],[1,1],[1,2],[2,2]])
        self.assertEqual(list(combinations_with_replacement(3,3)), [[0,0,0],[0,0,1],[0,0,2],[0,1,1],[0,1,2],[0,2,2],
                                              [1,1,1],[1,1,2],[1,2,2],[2,2,2]])

        self.assertEqual(list(combinations_with_replacement(3,4)), [[0,0,0,0],[0,0,0,1],[0,0,0,2],[0,0,1,1],[0,0,1,2],
                                              [0,0,2,2],[0,1,1,1],[0,1,1,2],[0,1,2,2],[0,2,2,2],
                                              [1,1,1,1],[1,1,1,2],[1,1,2,2],[1,2,2,2],[2,2,2,2]])

        
class SubsetTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(list(subset(0)), [])
        self.assertEqual(list(subset(1)), [[False], [True]])
        self.assertEqual(list(subset(2)), [[False,False],[False,True],[True,False],[True,True]])


if __name__ == "__main__":

    unittest.main()


