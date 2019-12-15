#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: sync error between memory and register during context changes among threads


from threading import Thread, Lock


class UnsafeCounter:

    def __init__(self):
        self.tot = 0

    def incr(self, n):
        for _ in range(n):
            self.tot += 1


class SafeCounter:

    def __init__(self):
        self.tot = 0
        self.lock = Lock()

    def incr(self, n):
        for _ in range(n):
            self.lock.acquire(blocking=True)
            self.tot += 1
            self.lock.release()


import unittest


class CounterTest(unittest.TestCase):

    def test_thread_unsafe_counter(self):

        c = UnsafeCounter()
        n = 1000000
        a, b = n//2, n-n//2

        t1 = Thread(target=c.incr, args=(a,))
        t2 = Thread(target=c.incr, args=(b,))

        t1.start(); t2.start()
        t1.join(); t2.join()

        assert c.tot != n

    def test_thread_safe_counter(self):
        c = SafeCounter()
        n = 1000000
        a, b = n//2, n-n//2

        t1 = Thread(target=c.incr, args=(a,))
        t2 = Thread(target=c.incr, args=(b,))

        t1.start(); t2.start()
        t1.join(); t2.join()

        assert c.tot == n


if __name__ == "__main__":

    unittest.main()
