#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from jpylib.jitertools import group_by


def string_compresser(original):
    ''' @param original: a string to be compressed
        @return compressed if it's shorter than original '''
    compressed = ''.join((ch+str(cnt) for ch,cnt in group_by(original)))

    return compressed if len(compressed) < len(original) else original


if __name__=="__main__":

    import unittest

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            self.assertCompress('', '')
            self.assertCompress('a', 'a')
            self.assertCompress('aa', 'aa')
            self.assertCompress('aaa', 'a3')

            self.assertCompress('abcdefg', 'abcdefg')
            self.assertCompress('aabbccdeeeeee', 'a2b2c2d1e6')
            self.assertCompress('aabccccccccaaa', 'a2b1c8a3')

        def assertCompress(self, original, expected):
            compressed = string_compresser(original)
            self.assertEqual(compressed, expected)
            if len(original) <= len(compressed):
                self.assertEqual(expected, original)
            else:
                self.assertEqual(expected, compressed)

    unittest.main()
