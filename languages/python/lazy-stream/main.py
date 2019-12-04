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
        return (nil, stream_null)
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

def main():
    #stream_print(natural())

    sf = stream_filter(natural(10**13), is_prime)
    stream_print(sf)

def main2():
    nat = natural(1)
    nat10 = stream_take(nat, 10)
    nat5 = stream_take(nat10, 5)
    nat15 = stream_take(nat5, 15)
    stream_print(nat15)

def main3():
    nat = natural(1)
    nat10 = stream_take(nat, 10)
    # to make nat10 be usable in builtin sum fn,
    # it should be of an Iterator type,
    # implementing: __iter__, __next__ methods
    # but I prefer to make a general reduce fn for such accumulating fns
    print(sum(nat10))

def main4():
    nat = natural(1)
    nat_from_10 = stream_drop(nat, 10)
    nat_10_to_20 = stream_take(nat_from_10, 10)
    stream_print(nat_10_to_20)
    print(stream_sum(nat_10_to_20))

main4()
