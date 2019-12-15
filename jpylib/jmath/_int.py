#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


def len_int(n):
    ''' @param n: number::int
        @return number of digit count '''
    assert n >= 0
    digits = 0
    while n > 0:
        digits += 1
        n //= 10
    return digits
    

import unittest


class LenTest(unittest.TestCase):
    def test_len_int(self):
        with self.assertRaises(AssertionError):
            len_int(-1)
        self.assertEqual(len_int(0), 0)
        self.assertEqual(len_int(1), 1)
        self.assertEqual(len_int(10), 2)
        self.assertEqual(len_int(99), 2)
        self.assertEqual(len_int(555), 3)


if __name__ == "__main__":

    unittest.main()
