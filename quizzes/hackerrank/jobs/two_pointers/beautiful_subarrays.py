#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


def beautiful_arrays(arr, m):
    ''' Time complexity: O(n)
        @param arr: non-negative integers
        @param m: allowed odd numbers count for subarrays btw [i,j]
        @return number of all possible subarrays with `m` odd numbers in them '''

    if not arr:
        return 0
    n = len(arr)
    if m==0:
        i = -1
        j = get_next_odd(arr, 0)
        res = 0
        while i<n:
            res += sigma_n(j-i-1)
            i = j
            j = get_next_odd(arr, j+1)
        return res
    else:
        iprev = -1
        i = get_next_odd(arr, 0)
        m_cnt = 0 if i==n else 1
        j = get_next_odd(arr, i)
        while j<n and m_cnt<m:
            m_cnt += 1
            j = get_next_odd(arr, j+1)
        assert j>=n or m_cnt == m
        jnext = get_next_odd(arr, j+1)
        if m_cnt != m:
            return 0

        res = 0
        while j < jnext: #i < n:
            assert m_cnt == m
            res += (i-iprev) * (jnext-j)
            iprev = i
            i = get_next_odd(arr, i+1)
            j = jnext
            jnext = get_next_odd(arr, jnext+1)

        assert j == jnext
        return res


def sigma_n(n):
    return sum(i for i in range(1, n+1))


def get_next_odd(arr, i):
    if i>=len(arr):
        return len(arr)
    while i<len(arr) and arr[i]%2==0:
        i += 1

    assert i == len(arr) or arr[i]%2 == 1
    return i


if __name__ == "__main__":

    import unittest

    class BeautifulArraysTest(unittest.TestCase):
        
        def test_basics(self):
            self.assertEqual(beautiful_arrays([],  0), 0)

            self.assertEqual(beautiful_arrays([1],  0), 0)
            self.assertEqual(beautiful_arrays([1],  1), 1)

            self.assertEqual(beautiful_arrays([1,1], 0), 0)
            self.assertEqual(beautiful_arrays([1,3], 1), 2)
            self.assertEqual(beautiful_arrays([1,3], 2), 1)
            self.assertEqual(beautiful_arrays([1,3], 3), 0)
            
            self.assertEqual(beautiful_arrays([2,5,4,9], 0), 2)
            self.assertEqual(beautiful_arrays([2,5,4,9], 1), 6)
            self.assertEqual(beautiful_arrays([2,5,4,9], 2), 2)
            self.assertEqual(beautiful_arrays([2,5,4,9], 3), 0)

    unittest.main()

