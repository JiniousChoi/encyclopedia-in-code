#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: 1st interview quiz from serverless.kakaogroup.com
## Try not to use list-like collections
## In other words, use space of O(1) complexity


def fibonacci_iter1(n):
    ''' naive implementation '''
    if n<=0:
        return
    assert n>=1
    if n==1:
        yield 1
        return
    if n==2:
        yield 1
        yield 1
        return
    
    yield 1
    yield 1
    n -= 2
    p2, p1, cur = 1, 1, 2
    while n > 0:
        yield cur
        p2, p1 = p1, cur
        cur = p2 + p1
        n -= 1
    

def fibonacci_iter2(n):
    ''' More compressive way to implement
        (1, 0,) 1, 1, 2, 3, 5. 8, ,,, '''
    if n<=0:
        return
    assert n>=1
    p2, p1 = 1, 0
    while n > 0:
        cur = p2 + p1
        yield cur
        p2, p1 = p1, cur
        n -= 1


def fibonacci_iter3(n):
    def fib():
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a+b

    it = fib()
    for _ in range(n):
        yield next(it)


import unittest


class SolutionTest(unittest.TestCase):

    def test_basics(self):
        self.assertFib(0, [])
        self.assertFib(1, [1])
        self.assertFib(2, [1,1])
        self.assertFib(3, [1,1,2])
        self.assertFib(4, [1,1,2,3])
        self.assertFib(5, [1,1,2,3,5])
    
    def assertFib(self, n, expected):
        fibs = [fibonacci_iter1, fibonacci_iter2, fibonacci_iter3]
        for fib in fibs:
            actual = list(fib(n))
            self.assertEqual(actual, expected)


if __name__ == "__main__":

    unittest.main()
