some_tuple = (1, 2, 3, 4, 5)

# unpacking

a, *b, c = some_tuple
print(a, b, c)

# i.e. sql query
[d] = [1]
print(d)


# unpacking in functions
def some_func(*rest):
    return rest


print(some_func(*range(1, 9)))

# nested unpacking
nested_tuple = (1, 2, 3, 4, (5, 6, 7))
_, _, _, _, (a, b, c) = nested_tuple
print(a, b, c)

# Convenient features of zero-based indexing:
# Easier to see the length of a slice:
some_slice = some_tuple[:2]  # will have a length of 2
print(len(some_slice))

# It’s easy to split a sequence in two parts at any index x,
# without overlapping: simply get my_list[:x] and my_list[x:].
easy_slice_first_half = some_tuple[:3]
easy_slice_second_half = some_tuple[3:]
print(easy_slice_first_half, easy_slice_second_half)

# add 3rd param to include a step => seq[start:stop:step]
step_slice = some_tuple[::2]
print(step_slice)

step_slice = some_tuple[::-1]
print(step_slice)

l = list(range(1, 10))
l[2:5] = [20, 30, 40]
print(l)

print(l * 5)

print('abcd' * 2)

# sorting
new_list = [19, 11, 4, 7, 89, 73, 1120, 33]
new_list.sort()  # new list is now sorted

new_list = new_list.sort()
print(new_list)  # None

list_of_strs = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(list_of_strs, key=len, reverse=True))
print(sorted(list_of_strs, reverse=True))

# changing immutable items of a tuple is possible
leaky_tuple = (1, 2, [1, 2, 3], 8)
leaky_tuple[2][0] = 9
print(leaky_tuple)
