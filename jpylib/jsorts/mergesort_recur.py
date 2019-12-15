#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from math import ceil
import sys
sys.setrecursionlimit(10000)


def mergesort_recur(arr):
    n = len(arr)
    half = n >> 1

    if n <= 1:
        return arr

    first = mergesort_recur(arr[:half])
    secon = mergesort_recur(arr[half:])

    i1, j1 = 0, half
    i2, j2 = 0, n-half
    
    res = []
    while i1 < j1 and i2 < j2:
        if first[i1] <= secon[i2]:
            res.append(first[i1])
            i1 += 1
        else:
            res.append(secon[i2])
            i2 += 1

    while i1 < j1:
        res.append(first[i1])
        i1 += 1
    while i2 < j2:
        res.append(secon[i2])
        i2 += 1

    return res


def main():
    import time
    arr = list(map(int, input("input arr:").split()))
    start = time.time()
    mergesort_recur(arr)
    end = time.time()
    print(end-start)

main()
