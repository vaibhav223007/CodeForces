lst = []

for i in range(5):
    inputted_value = [int(x) for x in input().split()]
    lst.append(inputted_value)

moves = 0
index = 0
while index < len(lst):
    if 1 in lst[index]:
        lst_index = index
        break
    index += 1

if lst_index == 0 or lst_index == 4:
    moves += 2
elif lst_index == 1 or lst_index == 3:
    moves += 1

index_second = lst[lst_index].index(1)

if index_second == 0 or index_second == 4:
    moves += 2
elif index_second == 1 or index_second == 3:
    moves += 1

print(moves)
