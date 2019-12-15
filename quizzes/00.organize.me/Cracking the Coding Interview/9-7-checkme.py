#!/usr/bin/env python3

import unittest

def parse(s):
    return [[cell for cell in line.strip()] for line in s.strip().splitlines()]

def fill_paint_dfs1(s, i, j):
    ''' s is [[cell]]
        cell is one of .XO
        . is aisle
        X is wall
        O is visited aisle
        i,j is starting point
        
        return printable result in string'''

    assert s[i][j] == '.'

    s[i][j] = 'O' #mark visited
    for ni, nj in get_visitable_neighbors(s,i,j):
        fill_paint_dfs1(s, ni, nj)
    
    return make_printable(s)

def fill_paint_dfs2(s, i, j):
    
    stack = [(i,j)]

    while stack:
        ci, cj = stack[-1]
        if s[ci][cj] == '.':
            s[ci][cj] = 'O'

        for ni, nj in get_visitable_neighbors(s,ci,cj):
            stack.append([ni, nj])
            break
        else:
            stack.pop(-1)

    return make_printable(s)

def fill_paint_bfs(s, i, j):

    q = [(i,j)] #to visit
    discovered = set((i,j)) #to_visit + visited

    while q:
        ci, cj = q.pop(0)
        s[ci][cj] = 'O'
        for ni, nj in get_visitable_neighbors(s,ci,cj):
            if (ni, nj) not in discovered:
                q.append((ni, nj))
                discovered.add((ni, nj))
    
    return make_printable(s)

def get_visitable_neighbors(s,i,j):
    for ni, nj in [(i+di, j+dj) for di,dj in [(-1,0),(0,1),(1,0),(0,-1)]]:
        if is_aisle(s, ni, nj):
            yield ni, nj

def is_aisle(s, i, j):
    if 0<=i<len(s) and 0<=j<len(s[0]) and s[i][j]=='.':
        return True
    return False

def make_printable(s):
    return '\n'.join(''.join(line) for line in s)

class XTest(unittest.TestCase):
    def setUp(self):
        self.sample = """
            ..X..
            X.XXX
            X...X
            X...X
            XXXXX"""

    def test_samples(self):
        s = parse(self.sample)

        res1 = fill_paint_dfs1(parse(self.sample), 0, 0)
        res2 = fill_paint_dfs2(parse(self.sample), 0, 0)
        res3 = fill_paint_bfs(parse(self.sample), 0, 0)

        self.assertEqual(res1, res2)
        self.assertEqual(res2, res3)
        #print(res1)
        #print(res2)
        #print(res3)

    def test_timeit_performance(self):
        ss = '''
        ..............................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XX.XXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XX.XXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XX.XXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XX........................................................XX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''

        try:
            fill_paint_dfs1(parse(ss), 0, 0)
            assert False, "cannot reach here"
        except RecursionError as re:
            pass

        res2 = fill_paint_dfs2(parse(ss), 0, 0)
        res3 = fill_paint_bfs(parse(ss), 0, 0)
        self.assertEqual(res2, res3)
        print(res3)

if __name__=="__main__":
    unittest.main()
