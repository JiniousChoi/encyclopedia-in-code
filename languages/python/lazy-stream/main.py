#!/usr/bin/env python3
#- author: jinchoiseoul@gmail.com
#- this is an educational implementation for stream authored by me.

from math import sqrt
from functools import reduce

###################
# LAZY DECORATORS #
###################

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
        for example, a function, repeat, decorated with `lazy`:
            repeat: \v->\->(v, repeat(v)) # lazy_cons_maker
            repeat(v) : \->(v, repeat(v)) # lazy_cons # a.k.a STREAM
            repeat(v)() :  (v, repeat(v)) # cons '''
    def wrapper(*args, **kwargs):
        def body():
            return func(*args, **kwargs)
        return body
    return wrapper

################################
# STREAM_GENERATORS, MODIFIERS #
################################

''' 
A stream is a (in)finite cons with a lazyness attribute.
It's a type of `\->(v, stream)`, so it needs to be executed
to retrieve the head value form the stream.
'''

@lazy
def repeat(v):
    return (v, repeat(v))

@lazy
def iterate(v, f):
    return (v, iterate(f(v), f))

@lazy
def genstream_from(col, i=0):
    if len(col) <= i:
        return NIL_STREAM()
    return col[i], genstream_from(col, i+1)

@lazy
def genstream_it(it):
    v = next(it, NIL)
    if v==NIL:
        return (NIL, NIL_STREAM)
    else:
        return (v, genstream_it(it))

@lazy
def genstream_chain(*streams, i=0):
    if len(streams) <= i:
        return (NIL, NIL_STREAM)
    v, s = (streams[i])()
    if v == NIL:
        return genstream_chain(*streams, i=i+1)()
    new_streams = list(streams)
    new_streams[i] = s
    return v, genstream_chain(*new_streams, i=i)

def stream_chain_reduce(*streams):
    ''' How about make stream_chain by utilizing reduce '''
    return reduce(genstream_chain_two, streams, NIL_STREAM)

@lazy
def genstream_chain_two(stream1, stream2, i=0):
    if 2 <= i:
        return (NIL, NIL_STREAM)
    s = stream1 if i==0 else stream2
    v, s = s()
    if v == NIL:
        return genstream_chain_two(stream1, stream2, i+1)()
    stream1 = s if i==0 else stream1
    stream2 = s if i==1 else stream2
    return v, genstream_chain_two(stream1, stream2, i)

@lazy
def stream_filter(stream, pred):
    while True:
        val, stream = stream()
        if pred(val):
            return (val, stream_filter(stream, pred))

@lazy
def stream_take(stream, cnt):
    if cnt <= 0:
        return NIL_STREAM()
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
        if val==NIL:
            return (NIL, stream)
        return (fn(val), stream)

#################
# GLOBAL VALUES #
#################

NIL = object()
NIL_STREAM = repeat(NIL)

######################
# STREAM TERMINATORS #
######################

def stream_reduce(stream, f, z=None):
    while True:
        val, stream = stream()
        if val == NIL:
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
        if val == NIL:
            break
        print(val)
    print()

##############
# PREDICATES #
##############

def is_even(n):
    return n%2==0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0: return False
    return True

