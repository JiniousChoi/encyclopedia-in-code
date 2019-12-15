#!/usr/bin/python3

from math import inf

def jlis(A, B, n, m, i, j):
    assert i in range(-1, n) and j in range(-1, m)
    
    a = A[i] if i >= 0 else -inf
    b = B[j] if j >= 0 else -inf + 1
    
    ans = 2
    
    max_element = max(a, b)
    for next_i in range(i+1, n):
        next_a = A[next_i]
        if max_element >= next_a:
            continue
        assert max_element < next_a
        ans = max(ans, 1+jlis(A, B, n, m, next_i, j))

    for next_j in range(j+1, m):
        next_b = B[next_j]
        if max_element >= next_b:
            continue
        assert max_element < next_b
        ans = max(ans, 1+jlis(A, B, n, m, i, next_j))
    
    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ans = jlis(A, B, n, m, -1, -1) - 2
        print(ans)

main()
