#!/usr/bin/env python3


'''
This script calculates the shortest relative path
from current position to the destination

For example,
curr: /home/jin/program/ninja.py
dest: /home/ted/program/
res:  ../../ted/program/

NOTE: folder always should have a trailing slash at the end. For example,
right: /dir1/dir2/, /dir1/file2
wrong: /dir3/dir4,  /dir3/file4/
'''


import re
import unittest


def calc_rel(p1, p2):
    assert p1 and p2
    if p1==p2: return p1

    ps1, ps2 = map(split, [p1, p2])
    rs1, rs2 = lca_removed(ps1, ps2)
    res = ''
    if len(rs1) == 1:
        res += './'
    else:
        res += '../' * (len(rs1) - 1)

    if (''.join(rs2))[0] == '/':
        res += ''.join(rs2)[1:]
    else:
        res += ''.join(rs2)

    return res


def split(s):
    ''' split path in str into list of path elements '''
    return re.findall('/[\w.-]*', s)
    

def lca_removed(ps1, ps2):
    cnt = 0
    for p1, p2 in zip(ps1, ps2):
        if p1==p2:
            cnt += 1
        else:
            break
    return ps1[cnt:], ps2[cnt:]


##########
## test ##
##########


class SplitTest(unittest.TestCase):
    
    def assertSplit(self, p, expected):
        self.assertEqual(split(p), expected)

    def test_errors(self):
        with self.assertRaises(AssertionError):
            calc_rel('/A', '')
        with self.assertRaises(AssertionError):
            calc_rel('', '/B')

    def test_ends_with_file(self):
        self.assertSplit('/A/README.md', ['/A','/README.md'])
        self.assertSplit('/A/B/README.md', ['/A','/B', '/README.md'])

    def test_folders_only(self):
        self.assertSplit('/A/B/', ['/A','/B', '/'])


class LCARemovedTest(unittest.TestCase):
    
    def assertRemoved(self, path1, path2, removed1, removed2):
        actual1, actual2 = lca_removed(path1, path2)
        self.assertEqual(actual1, removed1)
        self.assertEqual(actual2, removed2)

    def test_basics(self):
        self.assertRemoved(['/A','/B'], ['/A','/C'], ['/B'], ['/C'])


class CalcRelTest(unittest.TestCase):

    def assertRelative(self, p1, p2, expected):
        actual = calc_rel(p1, p2)
        self.assertEqual(actual, expected)

    def test_file_to_file(self):
        '''file to file'''
        self.assertRelative('/A', '/B', './B')
        self.assertRelative('/A/B', '/A/C', './C')
        self.assertRelative('/A/B', '/A/B', '/A/B')
        self.assertRelative('/A/B/C', '/A/X/Y', '../X/Y')

    def test_file_to_folder(self):
        '''file to folder'''
        self.assertRelative('/A', '/B/', './B/')
        self.assertRelative('/A/B', '/C/', '../C/')
        self.assertRelative('/A/B/C', '/A/B/D/', './D/')

    def test_folder_to_file(self):
        '''folder to file'''
        self.assertRelative('/A/', '/B', '../B')
        self.assertRelative('/A/', '/B/C', '../B/C')
        self.assertRelative('/A/B/', '/C/D', '../../C/D')

    def test_folder_to_folder(self):
        '''folder to folder'''
        self.assertRelative('/A/', '/B/', '../B/')
        self.assertRelative('/A/B/', '/C/', '../../C/')
        self.assertRelative('/A/B/', '/A/C/', '../C/')
        self.assertRelative('/A/B/C/', '/A/X/Y/', '../../X/Y/')
        

# unittest.main()


if __name__ == "__main__":
    import sys

    curr, dest = sys.argv[1], sys.argv[2]
    print(calc_rel(curr, dest))

