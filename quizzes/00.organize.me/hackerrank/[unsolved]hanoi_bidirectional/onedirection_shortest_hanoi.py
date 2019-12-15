#!/bin/python3

from collections import deque
def hanoi(N, a):
    ''' :N: total number of array `a`
        :a: [rod# for ith disk]
        :return: the shortest dist for the given hanoi to be the original state '''
    if N==0: return 0
    assert N > 0
    assert N == len(a)
    
    start = make_state(N, a)
    #todo make cur_state
    dists = {start:0} # visited + to_visit
    to_visit = deque([start])
    original = (1<<10)-1
    
    while to_visit:
        here = to_visit.popleft()
        dist = dists[here]
        if here == original:
            return dist
        for there in possible_theres(here):
            if there in dists:
                continue
            to_visit.append(there)
            dists[there] = dist + 1
    assert False, 'cannot reach here'

def make_state(N, a):
    state = 0
    rods = [rod-1 for rod in a]
    for i, rod in enumerate(rods):
        state |= 1<<(10*rod+i)
    return state
    
def possible_theres(state):
    ''' yield possible next state from the given '''
    a = state & ((1<<10)-1)
    b = (state >> 10) & ((1<<10)-1)
    c = (state >> 20) & ((1<<10)-1)
    d = (state >> 30) & ((1<<10)-1)
    disks = [a,b,c,d]
    rel_tops0 = [lowest_bit(e) for e in (a,b,c,d)]
    rel_tops = [e if e>0 else 11 for e in rel_tops0]
    abs_tops = [x_top<<i for x_top, i in zip(rel_tops0, range(0,40,10))]
    
    #for a top
    for i,from_top in enumerate(rel_tops):
        for j,to_top in enumerate(rel_tops):
            if i==j: continue
            #assert i != j
            if from_top >= to_top:
                continue
            assert from_top < to_top
            yield state - abs_tops[i] + abs_tops[j]
            
def lowest_bit(n):
    return n & (~n + 1)
    
def main():
    N = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    cnt = hanoi(N, a)
    print(cnt)
    
main()
