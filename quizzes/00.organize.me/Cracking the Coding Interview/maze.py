#!/usr/bin/env python3

import unittest

def parse(s):
    return [list(l.strip()) for l in s.strip().splitlines()]

def find_exit_narrow(m, i, j):
    ''' return True if exit is found, False, otherwise
    m will be modified during search
        i,j = current poinrt
        ! : exit point
        X : wall
        - : aisle
        @ : visited
    '''
    def next_point(m, i, j):
        #북동남서 순
        for ni, nj in [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]:
            if 0 <= ni < len(m) and 0 <= nj < len(m[0]) \
                    and m[ni][nj] not in "@X":
                yield ni, nj

    if m[i][j]=='!':
        return True

    m[i][j] = '@'

    for n in next_point(m, i, j):
        if find_exit_narrow(m, *n):
            return True

    m[i][j] = '-'
    return False

def find_exit_narrow_by_stack(m, i, j):
    def get_neighbors(m, i, j):
        for ni, nj in [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]:
            if 0 <= ni < len(m) and 0 <= nj < len(m[0]) \
                    and m[ni][nj] in "-!":
                yield ni, nj

    assert m[i][j] in '-!'
    visited = set()
    stack = [(i,j)]
    found = False

    while stack:
        i,j = stack[-1]

        if (i,j) not in visited:
            visited.add((i,j))
            if m[i][j] == '!':
                found = True
                break
        
        neighbor_found = False
        for neighbor_pos in get_neighbors(m, i, j):
            if neighbor_pos not in visited:
                stack.append(neighbor_pos)
                neighbor_found = True
                break
        if neighbor_found:
            continue

        stack.pop(-1)

    #maybe modify m along stack for road map
    for i,j in stack:
        if m[i][j] == '-':
            m[i][j] = '@'
    return found

def find_exit_wide(m, i, j):
    ''' return True if exit is found, False, otherwise
    m will be modified during search
        i,j = current poinrt
        ! : exit point
        X : wall
        - : aisle
        @ : visited
    '''
    def next_point(m, i, j):
        #북동남서 순
        for ni, nj in [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]:
            if 0 <= ni < len(m) and 0 <= nj < len(m[0]) \
                    and m[ni][nj] not in "@X":
                yield ni, nj

    if m[i][j]=='!':
        return True

    m[i][j] = '@'

    for n in next_point(m, i, j):
        if find_exit_wide(m, *n):
            return True

    #m[i][j] = '-'
    return False

def pretty_print_maze(m):
    for line in m:
        print(''.join(line))

class MazeTest(unittest.TestCase):
    def setUp(self):
        self.solutions = [find_exit_narrow, find_exit_wide, find_exit_narrow_by_stack]

        self.sample = '''
            -XXXXXX-XXXXXXXXXXXXX
            --------XXX---------X
            XX-XX-XXXXX-XXXXXXX-X
            X--XX-X-XX-------XX-X
            X-XXX-X-XX-XX-XXXXX-X
            X--XX-X----XX-XX-XX-X
            XX-XX-XXXX-XX-XX-XX-X
            XX-XX-XXXX-XX-XX-XX-X
            XX-XXXXXXX-XX-XX-XX-X
            XX---------XX-XX-XX-X
            XXXX-XX-XXXXX-XX-XX-X
            X-XX-XX-X-----XX-XX-X
            X-XX----X-XXX-XX----X
            X-XXXXXXXXXXX-XXXXXXX
            X-------------------!
            XXXXXXXXXXXXXXXXXXXXX'''

        self.sample2 = '''
            -XXXXXX-XXXXXXXXXXXXX
            --------XXX---------X
            --------------------X
            --------------------X
            --------------------X
            --------------------X
            --------------------X
            -------------------XX
            XX-XXXXXXX-XXX-X-XX-X
            XX---------XXX-X-XX-X
            XXXX-XX-XXXXXX-X-XX-X
            X-XX-XX-X----X-X-XX-X
            X-XX----X-XXXX-X----X
            X-XXXXXXXXXXXX-XXXXXX
            X-------------------!
            XXXXXXXXXXXXXXXXXXXXX'''

        self.sample3 = '''
            -----
            -----
            -----
            ----!'''

        self.sample4 = '''
            -XXX
            -XXX
            -XXX
            --X!'''

    def test_parse(self):
        m = parse(self.sample)
        assert len(m) > 1
        first_len = len(m[0])
        self.assertTrue(all(first_len==len(l) for l in m[1:]))

    def test_narrow_maze(self):
        for solution in self.solutions:
            m = parse(self.sample)
            self.assertTrue(solution(m, 0, 0))
            #pretty_print_maze(m)

    def test_wide_maze(self):
        for solution in [find_exit_wide, find_exit_narrow_by_stack]:
            m = parse(self.sample2)
            self.assertTrue(solution(m, 0, 0))
            #pretty_print_maze(m)

    def test_fail_cases(self):
        m = parse(self.sample4)
        self.assertFalse(find_exit_narrow(m, 0, 0))
        self.assertFalse(find_exit_wide(m, 0, 0))

if __name__=="__main__":
    unittest.main()
