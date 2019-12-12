#!/usr/bin/env python3

from time import sleep

class Promise:
    def __init__(self, f, x=None):
        self.f = f
        self.state = 'pending'

    def then(self, f):
        ''' @f is a function that returns
            a Promise object or any object ```
        pass

    def catch(self, xxx):
        pass


def fetch_promise():
    def f(resolve, reject):
        # delay as in network
        sleep(2) 
        resolve(10)
    return Promise(f)

def double_promise(res):
    def f(resolve, reject):
        resolve(2*res)
    return Promise(f)

def print_promise(res):
    def f(resolve, reject):
        print(res)
        resolve(res)
    return Promise(f)

def main():
    produce_promise().then(double_promise).then(print_promise)
    

main()
