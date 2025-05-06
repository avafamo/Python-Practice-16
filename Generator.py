def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(7)

print(next(counter))  # -> 1
print(next(counter))  # -> 2
print(next(counter))  # -> 3
print(next(counter))  # -> 4
print(next(counter))  # -> 5
print(next(counter))  # -> 6
print(next(counter))  # -> 7
print(next(counter))  # error
