#!/usr/bin/python3
## author: jinchoiseoul@gmail.com

''' With the given rng, `rand5`
    configure uniformly-distributed `rand7`
    and/or as uniformly distributed as `rand5` '''


def rand5():
    ''' @return randomly generated number in [0,1,2,3,4] '''
    import random
    return random.randint(0,4) #including both end points
    

def rand7():
    while(True):
        #This num part should be inside this while!!!
        num = 5*rand5() + rand5()
        if num < 21:
            return num%7


if __name__ == "__main__":

    import unittest
    from collections import Counter

    class SolutionTest(unittest.TestCase):
        def test_basics(self):
            trial = 50000
            avg = trial/7
            numbers = [rand7() for _ in range(trial)]
            mini, *freq, maxi = sorted(Counter(numbers).values())
            # I am just being creative
            self.assertTrue((maxi-mini)/avg < 0.1)

    unittest.main()
