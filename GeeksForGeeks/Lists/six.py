# Reversing a List in Python

def Reversing(lst):
    return lst[::-1]


lst = [1, 2, 3, 4, 5, 6]
new_list = Reversing(lst)
print(new_list)


for ele in reversed(lst):
    print(ele)

print([ele for ele in reversed(lst)])

lst2 = [10, 20, 30, 40, 50]
lst2.reverse()
print(lst2)
