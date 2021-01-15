# Different ways to clear a list in Python

def first_method(lst):
    return lst.clear()


lst = [1, 2, 3, 4, 5, 6]
first_method(lst)
print(lst)


def second_method(lst):
    del lst[:]
    return lst


lst = [1, 2, 3, 4, 5, 6]
second_method(lst)
print(lst)
