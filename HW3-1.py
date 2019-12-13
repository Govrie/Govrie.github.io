#!/usr/bin/env python3 -tt
"""File: hello.py """

def lru_cache(function):
    cache = {}
    def wrapper(*args, **kwargs):
        key = list(args)
        key.append(tuple(zip(kwargs.keys(), kwargs.values())))
        key = tuple(key)
        if key in cache.keys():
            return cache[key]
        value = function(*args, **kwargs)
        cache[key] = value
        return value
    return wrapper

@lru_cache
def some_function(*args, **kwargs):
    print(args,'', kwargs) #print only new args and kwargs before evaluating some_function
    return sum(args)

print(some_function(5, 4, k=2)) #print  args and calculate sum
print(some_function(5, 4, k=2)) #print sum from cache
print(some_function(1, 2, l=7)) #print args and calculate sum
print(some_function(5, 4, k=2)) #print sum from cache
