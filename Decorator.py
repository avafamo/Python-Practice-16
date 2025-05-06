from random import choice


def greet(person):
    def get_mood():
        msg = choice(('hello there ', 'go away ', 'goodbye '))
        res = msg + person
        return res

    return get_mood


res = greet('Ava')

print(res())

# def greet(person):
#     def get_mood():
#         msg = choice(('hello there ', 'go away ', 'goodbye '))
#         return msg
#
#     result = get_mood() + person
#     return result

# print(greet("Ava"))

# def sum(number, func):
#     total = 0
#     for num in range(1, number + 1):  # [1,2,3,4,5]
#         total += func(num)
#     return total
#
#
# def square(x):
#     return x * x
#
#
# print(sum(5, square))
#
# # 1 + 2 + 3 + 4 + 5 = 15
#
# # 1 + 4 + 9 + 16 + 25 = 55
