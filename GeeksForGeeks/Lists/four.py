# Check if element exists in list in Python


def existing(lst, ele):
    # if ele in lst:
    #     return True
    # else:
    #     return False
    return ele in lst


print(existing([1, 2, 3, 4, 5, 6], 2))
print(existing([1, 2, 3, 4, 5, 6], 10))
