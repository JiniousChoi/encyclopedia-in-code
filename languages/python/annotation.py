#!/usr/bin/python3

def decorator(decoratee):
    def decorated(*args, **kwargs):
        print('logging before')
        decoratee(*args, **kwargs)
        print('logging after')
    return decorated


### part1
@decorator
def test(name):
    print(name)

test('jinsung')
print()

### part2
def test2(name):
    print(name)

test2 = decorator(test2)
test2('jinsung2')
print()

#########
def second_order_decorator(permission):
    def decorator(decoratee):
        def decorated(*args, **kwargs):
            #before
            print(permission)
            decoratee(*args, **kwargs)
            #after
        return decorated
    return decorator

def one_order_downed_decorator(f):
    return second_order_decorator('admin')(f)

### part3
@second_order_decorator('normal')
def test3(name):
    print(name)

test3('jinsung')
print()

### part4
@one_order_downed_decorator
def test4(name):
    print(name)

test4('jinsung2')
print()
