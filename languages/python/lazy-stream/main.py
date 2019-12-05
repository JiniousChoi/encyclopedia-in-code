#!/usr/bin/env python3
#- author: jinchoiseoul@gmail.com

from math import sqrt

nil = object()

def lazy_seq(body):
    ''' impossible to implement
        lisp-like languages support macro for its arguments
        not to be evaluated until it's told so.
        So, in python, I need to explicitly define a wrapper fn
        in each stream fn I want to implement. '''
    pass

def lazy(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        def body():
            return func(*args, **kwargs)
        return body
    return wrapper

@lazy
def stream_null():
    return (nil, stream_null)

@lazy
def stream(col, i=0):
    if len(col) <= i:
        return stream_null()()
    return col[i], stream(col, i+1)

@lazy
def stream_it(it):
    v = next(it, nil)
    if v==nil:
        return (nil, stream_null)
    else:
        return (v, stream_it(it))

@lazy
def stream_chain(*streams, i=0):
    #import pdb; pdb.set_trace()
    if len(streams) <= i:
        return (nil, stream_null)
    v, s = (streams[i])()
    if v == nil:
        return stream_chain(*streams, i=i+1)()
    new_streams = list(streams)
    new_streams[i] = s
    return v, stream_chain(*new_streams, i=i)

@lazy
def natural(n=1):
    return (n, natural(n+1))

@lazy
def stream_filter(stream, pred):
    while True:
        val, stream = stream()
        if pred(val):
            return (val, stream_filter(stream, pred))

@lazy
def stream_take(stream, cnt):
    if cnt <= 0:
        # return (nil, stream_null)
        return stream_null()()
    val, stream = stream()
    return (val, stream_take(stream, cnt-1))

@lazy
def stream_drop(stream, cnt):
    for i in range(cnt):
        _, stream = stream()
    return stream()

@lazy
def stream_map(stream, fn):
    while True:
        val, stream = stream()
        if val==nil:
            return (nil, stream)
        return (fn(val), stream)

######################
# stream terminators #
######################

def stream_reduce(stream, f, z=None):
    while True:
        val, stream = stream()
        if val == nil:
            return z
        z = f(z, val)
   
def stream_sum(stream):
    return stream_reduce(stream, lambda z,v: z+v, 0)

def stream_mult(stream):
    return stream_reduce(stream, lambda z,v: z*v, 1)

def stream_print(stream):
    while True:
        val, stream = stream()
        if val == nil:
            break
        print(val)
    print()

##############
# predicates #
##############

def is_even(n):
    return n%2==0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0: return False
    return True

########
# main #
########

def main7():
    ''' test chain '''
    some_nums = stream([3,6,9])
    other_chs = stream(list("abc"))
    some_primes = stream([2,3,5,7,11,13,17,19])
    chained = stream_chain(some_nums, other_chs, some_primes)
    stream_print(chained)
