#!/usr/bin/env python3

def test(i):
    print("coroutine starts")
    while True:
        value = yield i
        i += value

b = test(5) // just created; main fn in control;
next(b)     // now corutine in control
            // execute print statement and then
            // yield val `i` to main fn
            // yield control back to caller
            // waiting to be fed again in pending mode
b.send(3)   // main fn feeds this coroutin with val `3`,
            // brought back to life, again in control,
            // execute i+= value, and then yield to main fn with val updated `i`
b.send(5)   // main fn feeds this coroutin with val `5`,
            // brought back to life, again in control,
            // execute i+= value, and then yield to main fn with val updated `i`
