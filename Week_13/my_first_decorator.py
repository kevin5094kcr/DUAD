def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result
    return wrapper

@logger
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(5, 2))