#!/usr/bin/env python3

def solve(cipher_text):
    # assert 25 <= L <= 100
    # pp := prime1 * prime2
    pps = [int(pp) for pp in cipher_text.split()]

    L = len(pps)
    # pp2 := [(p1, p2)]
    pp2s = [None] * L

    min_i, min_pp = min(enumerate(pps), key=lambda x: x[1])
    min_p1, min_p2 = factorize(min_pp)
    
    # sort pp2s[i]
    if min_i < L-1:
        if pps[min_i+1] % min_p1 == 0:
            pp2s[min_i] = (min_p2, min_p1)
        else:
            pp2s[min_i] = (min_p1, min_p2)
    else:
        if pps[min_i-1] % min_p1 == 0:
            pp2s[min_i] = (min_p1, min_p2)
        else:
            pp2s[min_i] = (min_p2, min_p1)
            
    # towards right
    for j in range(min_i+1, L):
        p1 = pp2s[j-1][1]
        p2 = pps[j] // p1
        pp2s[j] = (p1, p2)
    
    # towards left
    for j in range(min_i-1, -1, -1):
        p2 = pp2s[j+1][0]
        p1 = pps[j] // p2
        pp2s[j] = (p1, p2)

    found_ps = [p for (p,_) in pp2s] + [pp2s[-1][-1]]
    ps_in_order = sorted(set(found_ps))
    assert(len(ps_in_order) == 26)
    prime_to_char = {p:c for p,c in zip(ps_in_order, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    plain_text = ''.join(prime_to_char[p] for p in found_ps)
    return plain_text

def factorize(pp):
    for i in range(2, pp):
        if pp % i == 0:
            return (i, pp//i)

def main():
    T = int(input())
    for t in range(1, T+1):
        N, L = map(int, input().strip().split())
        cipher_text = input().strip()
        plain_text = solve(cipher_text)
        print("Case #{}: {}".format(t, plain_text))

if __name__ == "__main__":
    main()
