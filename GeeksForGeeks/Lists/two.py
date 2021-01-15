# Python program to swap two elements in a list

def swapping(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


print(swapping([23, 65, 19, 90], 1, 3))
