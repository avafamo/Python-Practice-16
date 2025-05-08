from functools import wraps


def my_decorator(func):
    @wraps(func)
    def my_wrapper(*args, **kwargs):
        print(f"function name is {func.__name__}")
        return func(*args, **kwargs)

    return my_wrapper


@my_decorator
def say_hello(name, family):
    print(f"hello {name} {family}")


# say_hello('Ava', 'Mohseni')

print(say_hello.__name__)
print(say_hello.__doc__)
help(say_hello)
