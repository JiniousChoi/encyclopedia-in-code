#!/usr/bin/python3
## author: jinchoiseoul@gmail.com

''' For given string, Encode every space to `%20`.
    This operation should occur in-place.
    The string has unused, available, sufficient memory cells in its tail. '''


SPACE='_' # For readaility issue, underbar is the replacement


def space_encoder(str_ls, str_ln):
    ''' @param str_ls::[char]
        @param str_ln::int
        @return str_ls with space-encoded '''
    spaces = str_ls[:str_ln].count(SPACE)
    encoded_str_ls = str_ln + 2*spaces
    assert len(str_ls) >= encoded_str_ls

    i, j = str_ln-1, encoded_str_ls-1
    while i >= 0:
        c = str_ls[i]
        if c == SPACE:
            str_ls[j] = '0'
            str_ls[j-1] = '2'
            str_ls[j-2] = '%'
            i, j = i-1, j-3
        else:
            str_ls[j] = str_ls[i]
            i, j = i-1, j-1
    assert i==j==-1
    return str_ls


def guess_ln(string):
    ''' @param string::[char]
        @return len(string) - len(empty_tail) '''
    j = -1
    for i,c in enumerate(string):
        if c != SPACE:
            j = i
    #assert 0 <= j+1 <= len(string)
    return j+1

if __name__=="__main__":

    import unittest

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            with self.assertRaises(AssertionError):
                space_encoder(list('Mr_John_Smith'), 987654321)

            self.assertEncodedTo('Mr_John_Smith____', 'Mr%20John%20Smith')

            self.assertEncodedTo('Mr_John_Smith______', 'Mr%20John%20Smith__')

        def test_guess_ln(self):
            self.assertEqual(guess_ln(''), 0)
            self.assertEqual(guess_ln('_'), 0)
            self.assertEqual(guess_ln('a'), 1)
            self.assertEqual(guess_ln('___'), 0)
            self.assertEqual(guess_ln('_ab__'), 3)
            self.assertEqual(guess_ln('abc__'), 3)
            self.assertEqual(guess_ln('abc_de__'), 6)
            self.assertEqual(guess_ln('abc_de_f'), 8)

        def assertEncodedTo(self, orig, expected):
            actual = space_encoder(list(orig), guess_ln(orig))
            self.assertEqual(actual, list(expected))

    unittest.main()
