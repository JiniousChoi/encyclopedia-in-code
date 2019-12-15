#!/usr/bin/python3
## author: jinchoiseoul@gmail.com
## brief: Demonstrate deadlock-prone simulation with
## dining philosophers problem and its one practical workaround.


from threading import Lock, Thread as Thread0


def Thread(*args, **kwargs):
    ''' daemonic threads are destoryed automatically when the main thread terminates.
        Although python cookbook 3rd says daemonic threads cannot be joined,
        somehow, `daemonic_thread.join()` DOES work in unittest of this module. '''
    return Thread0(*args, **kwargs, daemon=DAEMON)


class Chopstick(object):
    def __init__(self, blocking = True):
        self.blocking = blocking
        self.lock = Lock()

    def pickup(self):
        return self.lock.acquire(blocking=self.blocking)

    def putdown(self):
        self.lock.release()


class NaivePhilosopher(object):
    ''' hungry and selfish, therefore, deadlock-prone '''
    def __init__(self, name, left, right):
        self.name = name
        self.left, self.right = left, right

    def eat(self):
        self.pickup()
        self.chew()
        self.putdown()
        return 1

    def pickup(self):
        self.left.pickup()
        self.right.pickup()

    def chew(self):
        print(self.name, ":", "yum-yum!")

    def putdown(self):
        self.left.putdown()
        self.right.putdown()


class SmartPhilosopher(NaivePhilosopher):
    ''' deadlock prevention of circular wait '''

    def eat(self):
        if self.pickup():
            self.chew()
            self.putdown()
            return 1
        return 0

    def pickup(self):
        if not self.left.pickup():
            return False
        if not self.right.pickup():
            self.left.putdown()
            return False
        return True


def loop(philosopher):
    i = 0
    while i < LOOP:
        i += philosopher.eat()


def simulation(Philosopher, blocking, label=""):
    c1,c2,c3,c4 = [Chopstick(blocking) for _ in range(4)]

    p1 = Philosopher(label + '-' + "No.1", c1, c4)
    p2 = Philosopher(label + '-' + "No.2", c2, c1)
    p3 = Philosopher(label + '-' + "No.3", c3, c2)
    p4 = Philosopher(label + '-' + "No.4", c4, c3)
    
    print("start")

    ts = [Thread(target=loop, args=(p,)) for p in [p1,p2,p3,p4]]

    [t.start() for t in ts]

    [t.join() for t in ts]

    print("teminated")


def deadlock_prone_simulation():
    t = Thread(target=simulation, args=(NaivePhilosopher, True, 'prone'))
    t.start()
    return t


def deadlock_safe_simulation():
    t = Thread(target=simulation, args=(SmartPhilosopher, False, 'safe'))
    t.start()
    return t


import unittest
from unittest.mock import patch
from io import StringIO
from time import sleep


class SolutionTest(unittest.TestCase):

    def test_deadlock_safe(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            t = deadlock_safe_simulation()
            self.assertTrue(t.is_alive())
            t.join()
            self.assertFalse(t.is_alive())

    def test_deadlock_prone(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            t1 = self.run_while_active(fake_out)
            t2 = deadlock_prone_simulation()
            t1.join()
            self.assertFalse(t1.is_alive())
            self.assertTrue(t2.is_alive())

    def run_while_active(self, fake_out):
        def watcher(): 
            last_pos = fake_out.tell()
            while True:
                sleep(0.1)
                this_pos = fake_out.tell()
                if last_pos == this_pos:
                    # finish since it stopped
                    return
                last_pos = this_pos

        t = Thread(target=watcher)
        t.start()
        return t


if __name__ == "__main__":
    
    ''' Note: stubbing sys.stdout with StringIO makes sutble difference
        actual stdout: 100 loop is enough for deadlock reproduction
        StringIO stub: almost as many as 10000 loop is required for the same '''

    LOOP=10000; DAEMON=True;
    unittest.main()

    #LOOP = 100; DAEMON = None
    #deadlock_safe_simulation()
    
    #LOOP = 100; DAEMON = None
    #deadlock_prone_simulation()

