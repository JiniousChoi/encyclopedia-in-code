#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Given first two elements of a fibonacci sequence,
## find n-th element of the sequence 
## Note: It's 1-indexed


def solve_fibonacci(t1, t2, n):
    seq = [t1] + [t2]
    return fibo(seq, n)
    

def fibo(seq, n):
    assert 3 <= n <= 20
    while len(seq) < n:
        new_val = seq[-1]**2 + seq[-2]
        seq.append(new_val)
    
    assert len(seq) == n
    return seq[-1]
    
        
def main():
    t1, t2, n = map(int, input().strip().split())
    val_n = solve_fibonacci(t1, t2, n)
    print(val_n)
    

#main()


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(solve_fibonacci(0,1,5), 5)


if __name__ == "__main__":

    unittest.main()
