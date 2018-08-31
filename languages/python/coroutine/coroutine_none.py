#!/usr/bin/env python3

def test(x):
    print("coroutine starts")
    while True:
        value = yield
        if value == None:
            break
        x += value
    print ('before exiting')
    yield x

b = test(0)
next(b) # stdout: coroutine starts

for i in [1,2,3,4,5,None]:
    print(b.send(i))

# stdout: None
# stdout: None
# stdout: None
# stdout: None
# stdout: None
# stdout: before exiting
# stdout: 15
