## PYTHON DECORATORS

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper


@timer
def hello():
    print("Hello world")

@timer
def another_func():
    for num in range(100000000):
        num * num

hello()
another_func()