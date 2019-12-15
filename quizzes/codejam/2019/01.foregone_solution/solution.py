#!/usr/bin/env python3

M = { '0': ('0','0'),
      '1': ('1','0'),
      '2': ('1','1'),
      '3': ('2','1'),
      '4': ('2','2'),
      '5': ('3','2'),
      '6': ('3','3'),
      '7': ('2','5'),
      '8': ('3','5'),
      '9': ('3','6') }

def solve(n : int):
    s = str(n)
    s1, s2 = [], []
    for c in s:
        c1, c2 = M[c]
        s1.append(c1)
        s2.append(c2)
    return (int(''.join(s1)), int(''.join(s2)))

def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        n1, n2 = solve(n)
        print("Case #{}: {} {}".format(i, n1, n2))

if __name__ == "__main__":
    main()
