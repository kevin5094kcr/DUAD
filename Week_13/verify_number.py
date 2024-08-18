def verify_if_num(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"The parameter {arg} is not a number")
        return func(*args, **kwargs)
    return wrapper

@verify_if_num
def add_numbers(a, b):
    return a + b

print(add_numbers(6, 6))        
print(add_numbers('six', 6))