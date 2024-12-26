# The decorator
import time


def timing_decorator(func):
    def inner(*args, **kwargs):
        start_time = time.time() # start the time before calling the function
        result = func(*args, **kwargs) # executing the function
        end_time = time.time() # end time after function execution
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time: .4f} seconds")
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
# Call the decorated function
result1 = my_sum_operation1(1000000)
print(f"Result: {result1}")
result2 = my_sum_operation2(5000000, 66666666)
print(f"Result: {result2}")