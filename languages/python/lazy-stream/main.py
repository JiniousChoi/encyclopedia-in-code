#!/usr/bin/env python3
#- author: jinchoiseoul@gmail.com

from math import sqrt
from functools import reduce

nil = object()

def lazy_seq(body):
    ''' impossible to implement
        lisp-like languages support macro for its arguments
        not to be evaluated until it's told so.
        So, in python, I need to explicitly define a wrapper fn
        in each stream fn I want to implement. '''
    pass

def lazy(func, *args, **kwargs):
    ''' every function decorated with `lazy` should be 
        applied twice to get cons. It's because they 
        get to be wrapped in a hidden function named `body`
        to defer the immediate application of the function.
        for example, a function, stream_nil, decorated with `lazy`:
            stream_nil is \->\->(nil, stream_nil()) # lazy_cons_maker
            stream_nil() is \->(nil, stream_nil()) # lazy_cons # THIS IS THE ACTUAL STREAM
            stream_nil()() is (nil, stream_nil()) # cons '''
    def wrapper(*args, **kwargs):
        def body():
            return func(*args, **kwargs)
        return body
    return wrapper

@lazy
def stream_nil():
    return (nil, stream_nil())

@lazy
def stream_from(col, i=0):
    if len(col) <= i:
        return stream_nil()()
    return col[i], stream_from(col, i+1)

@lazy
def stream_it(it):
    v = next(it, nil)
    if v==nil:
        return (nil, stream_nil())
    else:
        return (v, stream_it(it))

@lazy
def stream_chain(*streams, i=0):
    if len(streams) <= i:
        return (nil, stream_nil())
    v, s = (streams[i])()
    if v == nil:
        return stream_chain(*streams, i=i+1)()
    new_streams = list(streams)
    new_streams[i] = s
    return v, stream_chain(*new_streams, i=i)

def stream_chain_reduce(*streams):
    ''' How about make stream_chain by utilizing reduce '''
    return reduce(stream_chain_two, streams, stream_nil())

@lazy
def stream_chain_two(stream1, stream2, i=0):
    if 2 <= i:
        return (nil, stream_nil())
    s = stream1 if i==0 else stream2
    v, s = s()
    if v == nil:
        return stream_chain_two(stream1, stream2, i+1)()
    stream1 = s if i==0 else stream1
    stream2 = s if i==1 else stream2
    return v, stream_chain_two(stream1, stream2, i)

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
        # return (nil, stream_nil())
        return stream_nil()()
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
    ''' to make a stream usable in builtin sum fn,
        it should be of an Iterator type,
        implementing: __iter__, __next__ methods,
        However, for simplicity, I prefer to make 
        a general reduce fn for such accumulating ones '''
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

