#!/usr/bin/python3
## author: jinchoiseoul@gmail.com

from jpylib.jtests import parse_io, joiner

def exponentiate(a,b,k,m):
    ''' reference - http://lafstern.org/matt/col3.pdf '''
    while k&1==0:
        a,b = imaginary_square(a, b, m)
        k >>= 1
    P = (a,b)
    k >>= 1
    while k > 0:
        a,b = imaginary_square(a, b, m)
        if k&1 > 0:
            P = imaginary_mul(P, (a, b), m)
        k >>= 1
    return P

def imaginary_mul(X, Y, mod):
    xa,xb = X
    ya,yb = Y
    c, d = xa*ya-xb*yb, xa*yb+xb*ya
    return c % mod, d % mod

def imaginary_square(a, b, mod):
    c, d= a**2-b**2, 2*a*b
    return c % mod, d % mod

def main():
    t = int(input())
    for _ in range(t):
        a,b,k,m = map(int, input().split())
        c, d = exponentiate(a,b,k,m)
        print(c, d)
        
if __name__=="__main__":
    #main()

    import unittest

    class SolutionTest(unittest.TestCase):
        def setUp(self):
            self.inp = '''3
                          2 0 9 1000
                          0 1 5 10
                          8 2 10 1000000000'''
            self.out = '''512 0
                          0 1
                          880332800 927506432'''
        def test_main(self):
            inp, out = parse_io(self.inp, self.out)
            for i,o in zip(inp[1:], out):
                a,b,k,m = map(int, i.split())
                actual = joiner(exponentiate(a,b,k,m))
                self.assertEqual(actual, o)

    unittest.main()
