#!/usr/bin/env python
# reference: https://rmarcus.info/blog/2016/12/14/monads.html

def step1(x):
  return "Hello " + x

def step2(x):
  return x + ", monads aren't that complicated."

def step3(x):
  return "***" + x + "***"
    
def prep01():
  def run():
    x = "friend"
    x = step1(x)
    x = step2(x)
    x = step3(x)
    return x

  print(run()) # ***Hello friend, monads aren't that complicated.***

def prep02():
  def wrap(x):
      return x

  def wrap_call(x, func):
      return func(x)

  def run():
    x = "friend"
    x = wrap(x)
    x = wrap_call(x, step1)
    x = wrap_call(x, step2)
    x = wrap_call(x, step3)
    return x
  
  print(run()) # ***Hello friend, monads aren't that complicated.***

def prep03():
  def wrap(x):
      return "[" + x + "]"

  def wrap_call(x, func):
      return "[" + func(x[1:-1]) + "]"

  def run():
    x = "friend"
    x = wrap(x)
    x = wrap_call(x, step1)
    x = wrap_call(x, step2)
    x = wrap_call(x, step3)
    return x

  print(run()) #[***Hello friend, monads aren't that complicated.***]


## wrap = ret
## wrap_call = bind

## ret(a : A) :: A -> B
## bind(b : B, f : A->A) :: B -> B

def monad01():
  def ret(x):
    return "[" + x + "]"

  def bind(x, func):
    return "[" +func(x[1:-1]) + "]"

  def run(ret, bind):
    x = "friend"
    x = ret(x)
    x = bind(x, step1)
    x = bind(x, step2)
    x = bind(x, step3)
    return x

  print(run(ret, bind)) #[***Hello friend, monads aren't that complicated.***]

def monad02_practical():
  def run(ret, bind):
    x = "friend"
    x = ret(x)
    x = bind(x, step1)
    x = bind(x, step2)
    x = bind(x, step3)
    return x

  def ret(x):
    print("Initial value:", x)
    return "[" + x + "]"
    
  def bind(x, func):
    print("Input to next step is:", x)
    result = func(x[1:-1])
    print("Result is:", result)
    return "[" + result + "]"
    
  print(run(ret, bind))

# why practical
# 1. By adding a few simple lines to ret and bind, we can print out the value of x before and after each step. 
# 2. Notice that without using a monad, we would have to write code for each step. 
# 3. Since normally we only want to add print statements like this to our code temporarily, monads let us just swap the ret and bind functions around to change between production and debugging.

def monad03_withrealtype():
  def ret(x):
    return {"value": x, "count": 0}

  def bind(x, func):
    return {"value": func(x["value"]), "count": x["count"] + 1}

  def run(ret, bind):
    x = "friend"
    x = ret(x)
    x = bind(x, step1)
    x = bind(x, step2)
    x = bind(x, step3)
    return x

  print(run(ret, bind))


if __name__=='__main__':
  prep01()
  prep02()
  prep03()
  monad01()
  monad02_practical()
  monad03_withrealtype()
