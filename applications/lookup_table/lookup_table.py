'''
Lookup Table
For expensive operations, caching the results in a lookup table speeds future queries.
The lookup table can be built in advance by iterating over all values in the domain of the function and recording the results.
Or, more lazily, can be build as the individual values are passed in.

Modify the code in this directory to build a lookup table so that it can finish running in under a minute.

There's no test file for this. It's counting to 50,000, so if it finishes before you give up, then you're golden.
'''
import math
import random

cache = dict()

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    key = f'{x},{y}'
    v = cache.get(key)
    if not v:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[key] = v
    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
