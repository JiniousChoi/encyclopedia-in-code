#!/usr/bin/env python3

from time import sleep

'''
toy implementation for the javascript-like Promise Design Pattern

TODO
- introduce lock machanism in case of a promise being executed on a worker thread
- implement worker thread
- allow more-than-one chains on a promise
-- as-is: throws an AssertionError
'''

class Promise:
    def __init__(self, f, auto=True):
        self.f = f
        self.v = None
        self.next = None
        self.state = 'pending'
        if auto:
            self.start()

    def start(self):
        if self.state == 'pending':
            self.f(self.resolve, self.reject)
        
    def then(self, t):
        ''' @f is a function that returns a Promise object '''
        def p(resolve, reject):
            res = t(self.v)
            if isinstance(res, Promise):
                def f(res2):
                    resolve(res2)
                res.then(f)
            else:
                resolve(res)
        # to keep it simple as PoC
        assert self.next == None
        self.next = Promise(p, auto=False)
        if self.state == 'done':
            self.try_next()
        return self.next

    def catch(self, err):
        pass

    def resolve(self, v):
        self.v = v
        self.state = 'done'
        self.try_next()

    def try_next(self):
        if self.next != None:
            self.next.start()

    def reject(self, e):
        pass

