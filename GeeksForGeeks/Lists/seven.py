# Python program to find sum of elements in list

def summing(lst):
    return sum(lst)


print(summing([2, 2, 2, 2, 2]))


def summing2(lst):
    total = 0
    for ele in lst:
        total += ele
    return total


print(summing2([5, 5, 5, 5, 5]))
