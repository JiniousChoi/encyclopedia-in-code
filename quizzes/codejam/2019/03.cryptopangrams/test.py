#!/usr/bin/env python3

import unittest
from solution import solve
from string import ascii_uppercase

C2P = {'A': 2, 'B': 3, 'C': 5, 'D': 7, 'E': 11, 'F': 13, 'G': 17, 'H': 19, 'I': 23, 'J': 29, 'K': 31, 'L': 37, 'M': 41, 'N': 43, 'O': 47, 'P': 53, 'Q': 59, 'R': 61, 'S': 67, 'T': 71, 'U': 73, 'V': 79, 'W': 83, 'X': 89, 'Y': 97, 'Z': 101}

P2C = {2: 'A', 3: 'B', 5: 'C', 7: 'D', 11: 'E', 13: 'F', 17: 'G', 19: 'H', 23: 'I', 29: 'J', 31: 'K', 37: 'L', 41: 'M', 43: 'N', 47: 'O', 53: 'P', 59: 'Q', 61: 'R', 67: 'S', 71: 'T', 73: 'U', 79: 'V', 83: 'W', 89: 'X', 97: 'Y', 101: 'Z'}

def assert_pangram(text):
    assert len(set(text)) == 26

def make_ciphertext(plain_text):
    text = plain_text.replace(' ', '').upper()
    assert_pangram(text)
    
    cipher = []
    for c1, c2 in zip(text, text[1:]):
        cipher.append(C2P[c1] * C2P[c2])
    return ' '.join(map(str, cipher))

class SolutionTest(unittest.TestCase):
    def test_make_ciphertext(self):
        cipher = make_ciphertext('jin choi' + ascii_uppercase)
        print(cipher)

    def test_basic1(self):
        cipher = make_ciphertext('jin choi' + ascii_uppercase)
        plain = solve(cipher)
        print(plain)

    def test_min_at_first(self):
        ''' enforce min_i is the first'''
        cipher = make_ciphertext('aa' + ascii_uppercase + 'zz')
        plain = solve(cipher)
        print(plain)

    def test_min_at_last(self):
        ''' enforce min_i is the last'''
        cipher = make_ciphertext('zz' + ascii_uppercase + 'aa')
        plain = solve(cipher)
        print(plain)

unittest.main()
