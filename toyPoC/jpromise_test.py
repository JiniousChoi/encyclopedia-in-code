#!/usr/bin/env python3

import unittest
from jpromise import Promise
from time import sleep
from threading import Thread
from io import StringIO
import sys

class PromiseTest(unittest.TestCase):

    def test_make_promise1(self):
        def f(resolve, reject):
            resolve(True)
        def assert_callback(res):
            self.assertTrue(res)
        p = Promise(f)
        p.then(assert_callback)

    def test_promise_sleep_on_main_thread(self):
        def f(resolve, reject):
            sleep(1)
            resolve(1)
        def assert_callback(v):
            self.assertEqual(10, v)
        p = Promise(f).then(lambda v: v*2).then(lambda v: v+8)
        p.then(assert_callback)

    def test_promise_sleep_on_worker_thread(self):
        def f(resolve, reject):
            def f2():
                resolve(1)
            setTimeout(f2, 1)
        def assert_callback(v):
            self.assertEqual(10, v)
        p = Promise(f).then(lambda v: v*2).then(lambda v: v+8)
        p.then(assert_callback)

    def test_promise_order_on_worker_thread(self):
        def f(resolve, reject):
            def f2():
                order.append('in promise')
                resolve(1)
            setTimeout(f2, 1)
        def assert_callback(v):
            self.assertEqual(10, v)
            self.assertEqual(order, ['begin', 'end', 'in promise'])
        order = []
        order.append('begin')
        p = Promise(f).then(lambda v: v*2).then(lambda v: v+8)
        p.then(assert_callback)
        order.append("end")

    def test_promise_then_fn_with_promise(self):
        def f(resolve, reject):
            def f2():
                resolve(1)
            setTimeout(f2, 1)
        def g(v):
            def g2(resolve, reject):
                resolve(v*2)
            return Promise(g2)
        def assert_callback(v):
            self.assertEqual(10, v)
        p = Promise(f).then(g).then(lambda v: v+8)
        p.then(assert_callback)
        

def setTimeout(f, t):
    def f2():
        sleep(t)
        f()
    t1 = Thread(target=f2)
    t1.daemon = False
    t1.start()

if __name__=="__main__":
    unittest.main()

