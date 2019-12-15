#!/usr/bin/env python3

def solve(n, her_path):
    return ''.join(['E' if c=='S' else 'S' for c in her_path])

def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        her_path = input().strip()
        my_path = solve(n, her_path)
        print("Case #{}: {}".format(i, my_path))

if __name__ == "__main__":
    main()
