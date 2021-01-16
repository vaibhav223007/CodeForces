number_of_rooms = int(input())
count = 0


for i in range(number_of_rooms):
    space = [int(x) for x in input().split()]
    # print(space)
    if (space[1] - space[0]) > 1:
        count += 1

print(count)
