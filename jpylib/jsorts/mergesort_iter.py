#!/usr/bin/python3
## author: jinchoiseoul@gmail.com 


from math import ceil


def mergesort_iter(arr):
    n = len(arr)
    tmp = [None] * n
    if n%2==1:
        #optimization
        tmp[-1] = arr[-1]
    unit = 1
    while unit < n:
        for i in range(int(ceil(n/2/unit))):
            begin, end = 2*i*unit, 2*(i+1)*unit
            
            b1, e1 = begin, begin + unit
            b2, e2 = begin + unit, min(end, n)
            i1, i2, i3 = b1, b2, b1

            if e1 >= n:
                #optimization
                continue

            while i1 < e1 and i2 < e2:
                if arr[i1] <= arr[i2]:
                    tmp[i3] = arr[i1]
                    i1 += 1
                    i3 += 1
                else:
                    tmp[i3] = arr[i2]
                    i2 += 1
                    i3 += 1

            while i1 < e1:
                tmp[i3] = arr[i1]
                i1 += 1
                i3 += 1
            #assert i1 == e1 #

            while i2 < e2:
                tmp[i3] = arr[i2]
                i2 += 1
                i3 += 1
            #assert i2 == e2 #

        #assert len(tmp) == n, 'tmp({})'.format(tmp) #
        arr, tmp = tmp, arr
        unit *= 2

    #assert unit >= n #
    return arr

def main():
    import time
    arr = list(map(int, input("input arr:").split()))
    start = time.time()
    #print(mergesort_iter(arr))
    mergesort_iter(arr)
    end = time.time()
    print(end-start)

main()
