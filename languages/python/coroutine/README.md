## generator
meaning of verb `yield`
1. to allow someone else to have control for it.
1. to produce a result or piece of information.

so, executing `yield val` statement is equal to allowing the caller to have back the control with the produced `val`, and going into pending mode.

```python
In [14]: def gen_test():
    ...:     print(1)
    ...:     yield 'a'
    ...:     print(2)
    ...:     yield 'b'
    ...:     print(3)
    ...:     

In [15]: a = gen_test()

In [16]: next(a)
1
Out[16]: 'a'

In [17]: next(a)
2
Out[17]: 'b'

In [18]: next(a)
3
```

## coroutine
```python
In [19]: def co_test():
    ...:     res = []
    ...:     while True:
    ...:         token = (yield)
    ...:         if token == 'EOL':
    ...:             print(res)
    ...:             break
    ...:         res.append(token)
    ...:         

In [20]: c = co_test()

In [21]: next(c)

In [22]: c.send('jin')

In [23]: c.send('wants')

In [24]: c.send('to go home')

In [25]: c.send('EOL')
['jin', 'wants', 'to go home']
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-25-8304862735f7> in <module>()
----> 1 c.send('EOL')

StopIteration: 


```

```python
In [26]: def co_test2(i):
    ...:     while True:
    ...:         value = yield i
    ...:         i += value
    ...:         

In [27]: c2 = co_test2(5)

In [28]: next(c2)
Out[28]: 5

In [29]: c2.send(3)
Out[29]: 8

In [30]: c2.send(2)
Out[30]: 10

In [31]: c2.send(20)
Out[31]: 30

In [32]: c2.close()

```
