import time

# the decorator
def timing_decorator(func):
    def inner(*args, **kwargs):
        stat_time = time.time()
        result = func(*args, **kwargs)
        print(f" Funciton 'my_sum_operation{func.__name__}' executed in{time.time() - stat_time:.4f} seconds")
        return result
    return inner

@timing_decorator
def my_sum_operation1(n):
    total = 0
    for i in range(n):
        total += i
    return total

@timing_decorator
def my_sum_operation2(n1,n2):
    total = 0
    for i in range(max(n1,n2)):
        total += i
    return total

# call the decorated function
result1 = my_sum_operation1(10000000)
print(f"Result: {result1}")

result2 = my_sum_operation2(50000000,66666666)
print(f"Result: {result2}")