#!/usr/bin/env python

def hanoi(N, a):
    ''' :N: total number of array `a`
        :a: [rod# for ith disk]
        :return: the shortest dist for the given hanoi to be the original state '''
    if N==0: return 0
    assert N > 0
    assert N == len(a)
    
    original = (1<<N)-1
    start = make_state(N, a)
    #todo make cur_state
    q = [(start,0)]
    discovered = set([start]) #to_visit + visited
    to_visit = [start]
    visited = set()
    
    while q:
        here, dist = q.pop(0)
        to_visit.pop(0)
        visited.add(here)
        print_current_state(dist, here) ###
        if here == original:
            return dist

        all_nexts = list(possible_theres(here))
        print_all_nexts(all_nexts, visited, to_visit)
        for there in all_nexts:
            if there in discovered:
                assert (there in visited) or (there in to_visit)
                assert there in discovered
                #print('[*]', here, there)
                continue
            q.append((there, dist+1))
            to_visit.append(there)
            discovered.add(there)
            assert there not in visited
            assert there in to_visit
            assert there in discovered

    assert False, 'cannot reach here'

def print_current_state(dist, here):
    print('***** START *****')
    print(dist)
    print('here:', here)
    print('here desc:', end=' ')
    show_state(here)

def print_all_nexts(all_nexts, visited, to_visit):
    next_visited = []
    next_tovisit = []
    for next in all_nexts:
        if next in visited:
            next_visited.append(next)
        else:
            next_tovisit.append(next)
    #todo: show next_visited, next_tovisit
    print('next_visited:', next_visited)
    print('next_tovisit:', next_tovisit)
    print()

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
    rel_tops0 = [lowest_bit(e) for e in disks]
    rel_tops = [e if e>0 else (1<<10) for e in rel_tops0]
    abs_tops = [x_top<<i for x_top, i in zip(rel_tops0, range(0,40,10))]
    
    #for a top
    for i,from_top in enumerate(rel_tops):
        for j,to_top in enumerate(rel_tops):
            if i==j: continue
            #assert i != j
            if from_top >= to_top:
                continue
            assert from_top < to_top
            shift = (j-i)*10
            if shift > 0:
                yield state - abs_tops[i] + (abs_tops[i] << shift)
            elif shift < 0:
                yield state - abs_tops[i] + (abs_tops[i] >> -shift)
            else:
                assert False, 'cannot be ==0'
            
def lowest_bit(n):
    return n & (~n + 1)
    
def show_state(state):
    for i in range(0,40,10):
        print(bin((state >> i) & ((1<<10)-1)))
    print()

def main():
    N = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    cnt = hanoi(N, a)
    print(cnt)
    
main()
