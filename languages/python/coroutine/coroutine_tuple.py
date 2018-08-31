#!/usr/bin/env python3

def test(x,y):
    print("coroutine starts")
    while True:
        x1, y1 = yield (x,y)
        x += x1
        y += y1


b = test(1,1)        # stdout: 
print(next(b))       # stdout: coroutine starts
                     # stdout: (1,1)
print(b.send((1,2))) # stdout: (2,3)
print(b.send((1,2))) # stdout: (3,5)
