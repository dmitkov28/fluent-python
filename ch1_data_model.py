from random import choice


class SomeCollection:
    def __init__(self):
        self._items = [x for x in range(55)]

    def __getitem__(self, item):
        return self._items[item]

    def __bool__(self):
        return False

    def __getattr__(self, item):
        return []

    @property
    def random_item(self):
        return choice(self._items)


my_collection = SomeCollection()

# print(my_collection.random_item)
# print(my_collection[::-1])
#
# for item in my_collection:
#     print(item)
#
# print(7 in my_collection )

# print(bool(my_collection))

print(getattr(my_collection, 'something'))