#!/usr/bin/python3
## author: jinchoiseoul@gmail.com

''' Find if str A can be produced with str B
    when B can be rotate.
    Note: utilize isSubstring method once and only '''


def same_on_rotation(A, B):
    if any(e in ['', None] for e in [A,B]):
        return False
    if len(A) != len(B):
        return False
    return (A+A).find(B) >= 0


if __name__ == "__main__":

    import unittest

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            self.assertTrue(same_on_rotation('abcdefg','cdefgab'))
            self.assertTrue(same_on_rotation('abc','abc'))
            self.assertTrue(same_on_rotation('abcabc','cabcab'))
            self.assertTrue(same_on_rotation('waterbottle', 'erbottlewat'))
            self.assertTrue(same_on_rotation('waterwbottle', 'wbottlewater'))

            self.assertFalse(same_on_rotation('', ''))
            self.assertFalse(same_on_rotation('a', 'ab'))
            self.assertFalse(same_on_rotation('ab', 'a'))
            self.assertFalse(same_on_rotation('ccc', 'abc'))

    unittest.main()
