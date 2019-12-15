#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


def comma0(n):
    s = str(n)
    stack = []
    while s:
        s, t = s[:-3], s[-3:]
        stack.append(t)
    return ','.join(stack[::-1])


def comma1(n):
    return '{:,}'.format(n)


comma = comma0

    
import unittest


class CommaTest(unittest.TestCase):

    def setUp(self):
        self.methods = [comma0, comma1]

    def test_basics(self):
        for method in self.methods:
            self.assertEqual(method(1), '1')
            self.assertEqual(method(12), '12')
            self.assertEqual(method(123), '123')
            self.assertEqual(method(1234), '1,234')
            self.assertEqual(method(12345), '12,345')
            self.assertEqual(method(123456), '123,456')
            self.assertEqual(method(1234567), '1,234,567')
            self.assertEqual(method(12345678), '12,345,678')
            self.assertEqual(method(123456789), '123,456,789')
            self.assertEqual(method(1234567890), '1,234,567,890')
            
if __name__ == "__main__":
    unittest.main()
