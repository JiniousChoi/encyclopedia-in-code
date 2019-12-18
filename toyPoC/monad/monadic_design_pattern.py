#!/usr/bin/env python
# https://rmarcus.info/blog/2016/12/14/monads.html

import json
jdata = """{"a": {"b": {"c": {"d": {"e": 6}}}}}"""
data = json.loads(jdata)

# Step 1 - naive and risky approach
def risky(data):
  return data["a"]["b"]["c"]["d"]["e"]

# Step 2 - looks before leaping
def ask_for_permission(data):
  if "a" not in data:
    return None
  if "b" not in data["a"]:
    return None
  if "c" not in data["a"]["b"]:
    return None
  if "d" not in data["a"]["b"]["c"]:
    return None
  if "e" not in data["a"]["b"]["c"]["d"]:
    return None
  return data["a"]["b"]["c"]["d"]["e"]

# Step 3 - takes a leap first, and then apologies if an error occurs
def ask_for_forgiveness(jdata):
  try:
    return data["a"]["b"]["c"]["d"]["e"]
  except:
    return None

# Step 4 - monadic design pattern, yet a little verbose
def think_in_monad(data):
  def ret(x):
    return x
    
  def bind(data, field):
    if data == None or field not in data:
      return None
    return data[field]

  data = ret(data)
  data = bind(data, "a")
  data = bind(data, "b")
  data = bind(data, "c")
  data = bind(data, "d")
  data = bind(data, "e")
  return data
  
# Step 5 - arguably monadic design pattern, and even compact
class MonadicDict:
    def __init__(self, data):
      self.data = data
    
    def __getitem__(self, field):
      if self.data == None or field not in self.data:
        return MonadicDict(None)
      return MonadicDict(self.data[field])
      
    def get(self):
      return self.data

if __name__=='__main__':
  print(risky(data))
  print(ask_for_permission(data))
  print(ask_for_forgiveness(data))
  print(think_in_monad(data))
  print(MonadicDict(data)['a']['b']['c']['d']['e'].get())
