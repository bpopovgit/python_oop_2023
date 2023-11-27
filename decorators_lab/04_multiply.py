def multiply(n):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * n
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

