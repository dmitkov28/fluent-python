# print(__builtins__.__dict__)

d1 = {'a': 1, 'b': 2}
d2 = {'b': 8, 'c': 3}
print(d1 | d2)
d1 |= d2
print(d1)

