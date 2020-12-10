from caching import Cache
import time

# One cache for many functions
cache = Cache(ttl=3600, maxsize=1024)

@cache
def pow(x, y):
    return x**y

@cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Caclulating Factorial of a Given Number
start_time = time.time()

print(factorial(10))
print(pow(10,5))

end_time = time.time()
print(f'Execution Time: {end_time-start_time}', )

# print(cache.clear())
print([item for item in cache.items()])