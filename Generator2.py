# def nums():
#     for num in range(20):
#         yield num
#
#
# g = nums()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# myGenerator = (num for num in range(20))
#
# print(myGenerator)
#
# print(next(myGenerator))
# print(next(myGenerator))
# print(next(myGenerator))
# print(next(myGenerator))

print(sum(num for num in range(100000000)))
