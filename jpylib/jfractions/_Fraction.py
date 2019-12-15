#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from jmath import gcd


class Fraction(object):
    ''' immutable '''
    
    @classmethod
    def parse(cls, s):
        assert '/' in s
        n, d = map(int, s.split('/'))
        return Fraction(n, d)
   
    def __init__(self, numerator, denominator):
        self.n = n = numerator
        self.d = d = denominator
        
        g = gcd(n,d)
        
        self.n //= g
        self.d //= g
    
    def __add__(self, o):
        ''' @return new instance of `self + o` '''
        g = gcd(self.d, o.d)
        self_factor = o.d // g
        o_factor = self.d // g
        
        new_n = self.n * self_factor + o.n * o_factor
        new_d = self.d * o.d // g

        return Fraction(new_n, new_d)
    
    def __sub__(self, o):
        o.n *= -1
        return self + o

    def __mul__(self, o):
        new_n = self.n * o.n
        new_d = self.d * o.d
        return Fraction(new_n, new_d)

    def __truediv__(self, o):
        o.n, o.d = o.d, o.n
        return self * o

    def __eq__(self, o):
        return self.n == o.n and self.d == o.d

    def __repr__(self):
        return 'Fraction({}, {})'.format(self.n, self.d)
    
    def __str__(self):
        return '{}/{}'.format(self.n, self.d)


import unittest


class FractionTest(unittest.TestCase):

    def test_add(self):
        fa, fb = map(Fraction.parse, ['1/3', '1/5'])
        self.assertEqual(str(fa+fb), '8/15')

    def test_sub(self):
        fa, fb = map(Fraction.parse, ['1/3', '1/5'])
        self.assertEqual(str(fa-fb), '2/15')

    def test_mul(self):
        fa, fb = map(Fraction.parse, ['1/3', '1/5'])
        self.assertEqual(str(fa*fb), '1/15')

    def test_div(self):
        fa, fb = map(Fraction.parse, ['1/3', '1/5'])
        self.assertEqual(str(fa/fb), '5/3')

    def test_eq(self):
        f1 = Fraction.parse('1/3')
        f2 = Fraction.parse('3/9')
        self.assertEqual(f1, f2)

    def test_repr(self):
        f1 = Fraction.parse('1/3')
        f2 = eval(repr(f1))
        self.assertEqual(f1, f2)


if __name__ == "__main__":

    unittest.main()
