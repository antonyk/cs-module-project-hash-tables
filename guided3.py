# build inverse square root lookup table
# 1 / sqrt(n)


import math
inv_sqrt = {}

def build_table():
  
  for i in range(1, 1000):
    inv_sqrt[i] = 1 / math.sqrt(i)

build_table()

print(inv_sqrt[4])
print(inv_sqrt[36])
print(inv_sqrt[2])


cache = {}

def build_lookup():
  for i in range(1000):
    cache[i] = num_reverse(i)

def num_reverse(n):
  if n in cache:
    return cache[n]
  else:
    n2 = list(str(n))
    n2.reverse()
    n2 = ''.join(n)
    n2 = int(n)
    cache[n] = int(n2)

  return int(n)

# build_lookup()


