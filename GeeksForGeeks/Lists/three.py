# Python | Ways to find length of list


def length(lst):
    return len(lst)


def length2(lst):
    count = 0
    for ele in lst:
        count += 1
    return count


lst = [1, 2, 3, 4, 5, 6]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(length(lst))
print(length2(lst2))
