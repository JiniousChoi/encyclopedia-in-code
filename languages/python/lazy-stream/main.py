#!/usr/bin/env python3
#- author: jinchoiseoul@gmail.com

from math import sqrt

def lazy_seq(body):
    ''' impossible to implement
        lisp-like languages support macro for its arguments
        not to be evaluated until it's told so.
        So, in python, I need to explicitly define a wrapper fn
        in each stream fn I want to implement. '''
    pass

def natural(n=1):
    def body():
        return (n, natural(n+1))
    return body

def is_even(n):
    return n%2==0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0: return False
    return True

def stream_filter(stream0, pred):
    ''' this also should return a stream '''
    def body():
        # without this, UnboundLocalError: local variable 'stream0' referenced before assignment
        stream = stream0
        while True:
            val, stream = stream()
            if pred(val):
                return (val, stream_filter(stream, pred))
    return body
            
def stream_take(stream0, cnt):
    def body():
        stream = stream0
        if cnt <= 0:
            raise Exception()
        val, stream = stream()
        return (val, stream_take(stream, cnt-1))

    return body
    
def stream_print(stream):
    while True:
        val, stream = stream()
        print(val)

def main():
    #stream_print(natural())

    sf = stream_filter(natural(10**13), is_prime)
    stream_print(sf)

main()
