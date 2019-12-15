#!/usr/bin/env python3

import time

class Random(object):
    def __init__(self, seed = None):
        if seed is None:
            _seed = int(time.time() * 1000)
        self._seed = (seed ^ 0x5deece66d ) & ((1 << 48) -1)

    def next(self, bits):
        """
        Generate next random number.
        Method returns an int that is `bits` bits long.
        Each bit is nearly equally likely to be 0 or 1.
        """

        if bits < 1:
            bits = 1
        elif bits > 32:
            bits = 32

        self._seed = (self._seed * 0x5deece66d + 0xb) & ((1 << 48) -1)
        retval = self._seed >> (48 - bits)

        if retval & (1 << 31):
            retval -= (1 << 32)

        return retval

    def nextInt(self, n = None):
        """
        Return random int in [0, `n`).
        If `n` is not supplied, random 32-bit int will be returned
        """
        if n is None:
            return self.next(32)

        if n <= 0:
            raise valueError("Argument must be positive!")

        if not (n & (n-1)):
            return (n * self.next(31)) >> 31

        bits = self.next(31)
        val = bits % n
        while (bits - val + n - 1) < 0:
            bits = self.next(31)
            val = bits % n

        return val

def solution():
    tcs = '''643 953 522 277 464 366 321 409 227 702
877 654 2 715 229 255 712 267 19 832
833 973 135 54 665 768 571 305 747 782
737 614 776 36 82 827 151 734 286 102
630 858 561 339 290 517 733 441 501 768
188 750 293 162 342 614 323 609 712 881
536 414 842 944 934 478 974 539 188 260
875 787 919 770 100 469 394 879 579 159
917 178 525 924 165 26 820 915 409 657
846 396 735 741 712 451 402 824 1 335
71 858 956 68 740 794 855 56 554 572
688 780 465 286 133 46 525 359 328 68
171 92 441 813 837 266 892 413 535 265
142 5 584 5 916 277 417 304 327 39
541 134 0 877 386 705 529 864 377 240
361 579 454 581 702 61 294 641 737 304
521 309 908 850 32 471 132 819 636 67
342 717 76 884 637 276 571 779 801 493
    '''
    tcs = '737 614 776 36 82 827 151 734 286 102'
    for tc in tcs.splitlines():
        seed = brute_force(tc)
        print('seed :', seed)

def brute_force(tc):
    values = list(map(int, tc.strip().split()))
    #for seed in range(1000000000, 1501511221):
    for seed in range(1226891300, 1501511221):
        print(seed)
        rng = Random(seed)
        failed = False
        for i in range(10):
            v = rng.nextInt(1000)
            if not v == values[i]:
                failed = True
                break
        if not failed:
            return seed
    print('Failed to find seed for', values)

if __name__ == '__main__':
    solution()
