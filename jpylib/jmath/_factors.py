#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


def divisor_factors(n):
    ''' return [divisor]
        i.e. 1 -> [1]
             2 -> [1,2]
             4 -> [1,2,4]
             10 -> [1,2,5,10] '''
    left, right = [], []
    for f in range(1, int(n**.5)+1):
        if n%f == 0:
            l, r = f, n//f
            left.append(l)
            if l != r: right.append(r)
    while right:
        left.append(right.pop(-1))

    #assert right == []
    return left


def prime_factors(n):
    ''' return [prime_factor]
        i.e. 4 -> [2,2]
             6 -> [2,3]
             7 -> [7]
             9 -> [3,3]
             12 -> [2,2,3] '''
    assert n >= 1
    factors = []
    while n%2==0:
        factors.append(2)
        n //= 2

    p = 3
    while n > 1:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    assert n == 1
    return factors
    

def gcd(a, b):
    if b==0: return a
    return gcd(b, a%b)


def lcm(a,b):
    return a * b // gcd(a,b)


import unittest


class FactorsTest(unittest.TestCase):
    def test_divisor_factors(self):
        self.assertEqual(divisor_factors(1), [1])
        self.assertEqual(divisor_factors(2), [1,2])
        self.assertEqual(divisor_factors(4), [1,2,4])
        self.assertEqual(divisor_factors(10), [1,2,5,10])

    def test_prime_factors(self):
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(4), [2,2])
        self.assertEqual(prime_factors(6), [2,3])
        self.assertEqual(prime_factors(7), [7])
        self.assertEqual(prime_factors(9), [3,3])
        self.assertEqual(prime_factors(12), [2,2,3])


class GCDTest(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(gcd(1,1), 1)
        self.assertEqual(gcd(1,3), 1)
        self.assertEqual(gcd(3,1), 1)
        self.assertEqual(gcd(3,7), 1)

        self.assertEqual(gcd(2,2), 2)
        self.assertEqual(gcd(2,4), 2)

        self.assertEqual(gcd(55,11), 11)


class LCMTest(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(lcm(1,1), 1)
        self.assertEqual(lcm(1,3), 3)
        self.assertEqual(lcm(3,1), 3)
        self.assertEqual(lcm(3,7), 21)

        self.assertEqual(lcm(2,2), 2)
        self.assertEqual(lcm(2,4), 4)

        self.assertEqual(lcm(55,11), 55)


if __name__ == "__main__":

    unittest.main()
