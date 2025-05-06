# 0,1,1,2,3,5,8,13,21,...


def fib_list(max):  # 10
    nums = []  # [1,1]
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


fib_list(1000000)

def fib_generator(max):
    x = 0
    y = 1
    count = 0

    while count < max:
        x, y = y, x + y
        yield y
        count += 1


for num in fib_generator(1000000):
    print(num)
