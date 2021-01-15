# Python program to interchange first and last elements in a list

def interchange(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


new_list = interchange([1, 2, 3, 4, 5])
print(new_list)

lst = [1, 2, 3, 4, 5]
a, *b, c = lst
print(a)
print(b)
print(c)

start, *middle, last = lst
lst = last, *middle, start
print(lst)
