from functools import wraps


# decorator factory

def check_string_length(characterCount):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(name):
            if len(name) > characterCount:
                print("an error occured")
            else:
                func(name)
            return func

        return wrapper

    return inner_decorator


@check_string_length(5)
def show_name(name):
    print(name)


show_name('Ava')

# def show_decorator(is_show):
#     def inner_decorator(func):
#         @wraps(func)
#         def wrapper():
#             if is_show:
#                 func()
#             else:
#                 print("you dont have permission")
#
#         return wrapper
#
#     return inner_decorator
#
#
# @show_decorator(False)
# def go_to_admin_page():
#     print("this is admin page")
#
#
# go_to_admin_page()
