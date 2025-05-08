def my_decorator(func):
    def say_bye(*args, **kwargs):
        print("this is working for me")
        func(*args, **kwargs)

    return say_bye


@my_decorator
def say_hello(name):
    print(f"hello {name}")


@my_decorator
def say_my_name(name, family):
    print(f"{name} {family}")


# say_hello('Ava')
say_my_name('Ava', 'Mohseni')

# sayHelloByDecorator = my_decorator(say_hello)

# sayHelloByDecorator()
